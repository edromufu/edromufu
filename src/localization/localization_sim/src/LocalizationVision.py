import cv2 as cv
import numpy as np
from Intersection import Intersection


class LocalizationVision:

    neighbourDistance = 40
    SIMULATION = 'SIMULATION'
    IMAGES = 'IMAGES'

    def __init__(self):
        self.finalLines = []
        self.finalIntersections = []
        self.ratio = 1

    def kernel(r):
        return np.fromfunction(lambda x, y: ((x-r)**2 + (y-r)**2 <= r**2)*1, (2*r+1, 2*r+1), dtype=int).astype(np.uint8)

    def setFrame(self, frame):
        self.frame = frame

    def formatFrame(self, size = [416,416]):

        # Cortando a imagem para ficar quadrada
        if size[0] == size[1]:
            if self.frame.shape[0] < self.frame.shape[1]:
                aux =   self.frame.shape[1] - self.frame.shape[0]
                self.frame = self.frame[0:self.frame.shape[0], int(aux/2):self.frame.shape[1]-int(aux/2)]
            else: 
                aux =   self.frame.shape[0] - self.frame.shape[1]
                self.frame = self.frame[int(aux/2):self.frame.shape[0]-int(aux/2), 0:self.frame.shape[1]]

        # Resizing
        self.ratio = self.frame.shape[0]
        self.frame = cv.resize(self.frame,(size[0],size[1]))
        self.ratio = self.ratio/self.frame.shape[0]      

    def getMasks(self):
        # Convertendo para escala de cinza e obtendo a máscara a partir de um threshold
        _,self.mask = cv.threshold(cv.cvtColor(self.frame,cv.COLOR_BGR2GRAY),220,255,cv.THRESH_BINARY)

        # Operação de fechamento com kernel maior (remover buracos)
        filter = LocalizationVision.kernel(int(16/self.ratio))
        self.mask = cv.dilate(self.mask, filter, iterations=1)
        self.mask = cv.erode(self.mask, filter, iterations=1)

        # Operação de fechamento com kernel menor (remover ruídos)
        filter = LocalizationVision.kernel(int(10/self.ratio))
        self.mask = cv.dilate(self.mask, filter, iterations=1)
        self.mask = cv.erode(self.mask, filter, iterations=1)

        # Máscara dilatada para conferir intersecções
        filter = LocalizationVision.kernel(int(16/self.ratio))
        self.dilatedMask = cv.dilate(self.mask, filter, iterations=2)
        self.dilatedMask = cv.erode(self.dilatedMask, filter, iterations=1)

    def findLines(self):
        # Obtendo as bordas da máscara
        edges = cv.Canny(self.mask,50,200)

        # Obtendo as linhas a partir das bordas
        lines = cv.HoughLines(edges,1,np.pi/180,int(80/self.ratio))

        # Filtrando
        self.finalLines = []
        thresholdRho = 30
        thresholdTheta = 0.2
        
        if type(lines) is np.ndarray:
            for i in range(len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                match = False

                for j in range(len(self.finalLines)):
                    rhoRef, thetaRef = self.finalLines[j]
                    if rho >= rhoRef-thresholdRho and rho <= rhoRef+thresholdRho and theta >= thetaRef-thresholdTheta and theta <= thetaRef+thresholdTheta:
                        self.finalLines.append((rhoRef,thetaRef))
                        self.finalLines.pop(j)
                        match = True
                        

                if not match:
                    self.finalLines.append((rho,theta))

    def findIntersections(self, filtering = True):
        # Interseccao => (x1,y1) = (x2,y2)
        # Interseccao em x, x = (rho2/sin(theta2) - rho1/sin(theta1)) / (-cos(theta1)/sin(theta1) + cos(theta2)/sin(theta2))
        # Interseccao em x, x = (b2 - b1) / (a1 - a2)
        # Para interseccao estar na imagem, 0 <= x <= xmax

        # Encontrando todas as interseccoes
        intersections = []
        lines = self.finalLines.copy()
        for i in range(len(lines)-1,0,-1):
            rho1, theta1 = lines[i]

            for j in range(len(lines)):
                rho2, theta2 = lines[j]
                if rho1 != rho2 and theta1 != theta2:
                    A = np.array([[np.cos(theta1), np.sin(theta1)],[np.cos(theta2), np.sin(theta2)]])
                    b = np.array([[rho1], [rho2]])
                    x, y = np.linalg.solve(A, b)
                    x, y = int(np.round(x)), int(np.round(y))
                    
                    if x >=0 and x <= self.frame.shape[0] and y >=0 and y <= self.frame.shape[1]:
                        intersection = Intersection(x,y,(rho1,theta1),(rho2,theta2))
                        intersections.append(intersection)
            
            lines.pop(i)

        # Filtrando e classfiicando interseccoes
        if filtering:
            intersections = list(set(intersections))
            self.finalIntersections = []
            for intersection in intersections:
                intersection.findNeighbours(LocalizationVision.neighbourDistance)
                p1Pertence, p2Pertence, p3Pertence, p4Pertence = intersection.checkNeighbours(self.dilatedMask)
                if ((p1Pertence or p3Pertence) and (p2Pertence or p4Pertence)): #Para ser uma interseccao, precisa de no minimo um ponto em cada reta
                    if p1Pertence and p2Pertence and p3Pertence and p4Pertence:
                        intersection.classificar(4)
                    elif (p1Pertence and p3Pertence) or (p2Pertence and p4Pertence):
                        intersection.classificar(3)
                    else:
                        intersection.classificar(2)
                    self.finalIntersections.append(intersection)
        else:
            self.finalIntersections = intersections

    def drawResults(self, drawLines = False, drawIntersections = False, drawNeighbours = False):
        self.resultColored = self.frame.copy()
        colorRed = (0,0,255) 
        colorBlue = (255,0,0)
        colorGreen = (0,255,0)

        if drawLines:
            for i in range(len(self.finalLines)):

                rho, theta = self.finalLines[i]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 2000*(-b)), int(y0 + 2000*(a)))
                pt2 = (int(x0 - 2000*(-b)), int(y0 - 2000*(a)))
                
                cv.line(self.resultColored, pt1, pt2, colorRed, 3)

        if drawNeighbours:
            for intersection in self.finalIntersections:
                if intersection.p1Check: cv.circle(self.resultColored,(intersection.p1[0],intersection.p1[1]),4,colorBlue,4)
                if intersection.p2Check: cv.circle(self.resultColored,(intersection.p2[0],intersection.p2[1]),4,colorBlue,4)
                if intersection.p3Check: cv.circle(self.resultColored,(intersection.p3[0],intersection.p3[1]),4,colorBlue,4)
                if intersection.p4Check: cv.circle(self.resultColored,(intersection.p4[0],intersection.p4[1]),4,colorBlue,4)
                
        if drawNeighbours and drawIntersections:
            for intersection in self.finalIntersections:
                if intersection.p1Check: cv.line(self.resultColored, (intersection.x,intersection.y), (intersection.p1[0],intersection.p1[1]), colorBlue, 3)
                if intersection.p2Check: cv.line(self.resultColored, (intersection.x,intersection.y), (intersection.p2[0],intersection.p2[1]), colorBlue, 3)
                if intersection.p3Check: cv.line(self.resultColored, (intersection.x,intersection.y), (intersection.p3[0],intersection.p3[1]), colorBlue, 3)
                if intersection.p4Check: cv.line(self.resultColored, (intersection.x,intersection.y), (intersection.p4[0],intersection.p4[1]), colorBlue, 3)
        
        if drawIntersections:
            for intersection in self.finalIntersections:
                cv.circle(self.resultColored,(intersection.x,intersection.y),5,colorBlue,5)
                '''cv.putText(self.resultColored, text= f'({intersection.x},{intersection.y})', org=(intersection.x,intersection.y),
            fontFace= cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0,0,0),
            thickness=2, lineType=cv.LINE_AA)'''

    def showResults(self, mask = False, resultColored = False, original = False, dilatedMask = False, source=SIMULATION):

        showing = False
        if mask:
            cv.imshow("Mask", self.mask)
            showing = True

        if resultColored:
            cv.imshow("Result", self.resultColored)
            showing = True

        if original:
            cv.imshow("Original", self.frame)
            showing = True

        if dilatedMask:
            cv.imshow("Dilated mask", self.dilatedMask)
            showing = True

        if showing:
            if source == LocalizationVision.IMAGES: cv.waitKey(0)
            else: cv.waitKey(1)
            #cv.destroyAllWindows()

    def tieBreaker(self):
        return cv.bitwise_and(self.resultColored,self.resultColored,mask=self.dilatedMask)

    def getIntersections(self):
        return self.finalIntersections