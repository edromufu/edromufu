import cv2 as cv
import numpy as np
from Intersection import Intersection


class LocalizationVision:



    def __init__(self):
        self.finalLines = []
        self.finalIntersections = []
        

    def kernel(r):
        return np.fromfunction(lambda x, y: ((x-r)**2 + (y-r)**2 <= r**2)*1, (2*r+1, 2*r+1), dtype=int).astype(np.uint8)

    def formatFrame(self, frame, size = [416,416]):
        self.frame = frame

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

    def getIntersections(self, filtering = True):
        # Interseccao => (x1,y1) = (x2,y2)
        # Interseccao em x, x = (rho2/sin(theta2) - rho1/sin(theta1)) / (-cos(theta1)/sin(theta1) + cos(theta2)/sin(theta2))
        # Interseccao em x, x = (b2 - b1) / (a1 - a2)
        # Para interseccao estar na imagem, 0 <= x <= xmax

        # Encontrando todas as interseccoes
        intersections = []
        for i in range(len(self.finalLines)-1,0,-1):
            rho1, theta1 = self.finalLines[i]

            for j in range(len(self.finalLines)):
                rho2, theta2 = self.finalLines[j]
                if rho1 != rho2 and theta1 != theta2:
                    A = np.array([[np.cos(theta1), np.sin(theta1)],[np.cos(theta2), np.sin(theta2)]])
                    b = np.array([[rho1], [rho2]])
                    x, y = np.linalg.solve(A, b)
                    x, y = int(np.round(x)), int(np.round(y))
                    
                    if x >=0 and x <= original.shape[0] and y >=0 and y <= original.shape[1]:
                        intersection = Intersection(x,y,(rho1,theta1),(rho2,theta2))
                        intersections.append(intersection)
            
            finalLines.pop(i)

        # Filtrando e classfiicando interseccoes
        if filtering:
            intersections = list(set(intersections))
            self.finalIntersections = []
            for intersection in intersections:
                p1, p2, p3, p4 = intersections.vizinhos(15) #p1 e p3 pertencem a uma reta, p2 e p4 a outra
                p1Pertence = (self.dilatetedMask[p1[0]][p1[1]] == 255)
                p2Pertence = (self.dilatetedMask[p2[0]][p2[1]] == 255)
                p3Pertence = (self.dilatetedMask[p3[0]][p3[1]] == 255)
                p4Pertence = (self.dilatetedMask[p4[0]][p4[1]] == 255)
                if (p1Pertence or p3Pertence) and (p2Pertence or p4Pertence): #Para ser uma interseccao, precisa de no minimo um ponto em cada reta
                    if p1Pertence and p3Pertence and p2Pertence and p4Pertence:
                        intersection.classificar(4)
                    elif (p1Pertence and p3Pertence) or (p2Pertence and p4Pertence):
                        intersection.classificar(3)
                    else:
                        intersection.classificar(2)
                    self.finalIntersections.append(intersection)
        else:
            self.finalIntersections = intersections

    def getMasks(self):
        # Convertendo para escala de cinza e obtendo a máscara a partir de um threshold
        ret,self.mask = cv.threshold(cv.cvtColor(self.frame,cv.COLOR_BGR2GRAY),220,255,cv.THRESH_BINARY)

        # Operação de fechamento com kernel maior (remover buracos)
        filter = LocalizationVision.kernel(int(16/self.ratio))
        self.frame = cv.dilate(self.frame, filter, iterations=1)
        self.frame = cv.erode(self.frame, filter, iterations=1)

        # Operação de fechamento com kernel menor (remover ruídos)
        filter = LocalizationVision.kernel(int(10/self.ratio))
        self.frame = cv.dilate(self.frame, filter, iterations=1)
        self.frame = cv.erode(self.frame, filter, iterations=1)

        # Máscara dilatada para conferir intersecções
        filter = kernel(int(16/self.ratio))
        self.dilatetedMask = cv.dilate(self.mask, filter, iterations=1)

    def getLines(self):
        # Obtendo as bordas da máscara
        edges = cv.Canny(self.mask,50,200)

        # Obtendo as linhas a partir das bordas
        lines = cv.HoughLines(edges,1,np.pi/180,int(80/self.ratio))

        # Filtrando
        self.finalLines = []
        thresholdRho = 30
        thresholdTheta = 0.2

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

    def drawResults(self):
        self.resultColored = self.frame.copy()
        colorRed = (0,0,255) 
        colorBlue = (255,0,0)

        for i in range(len(self.finalLines)):

            rho, theta = self.finalLines[i]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 2000*(-b)), int(y0 + 2000*(a)))
            pt2 = (int(x0 - 2000*(-b)), int(y0 - 2000*(a)))
            
            cv.line(self.resultColored, pt1, pt2, colorRed, 3)

        for intersection in self.finalIntersections:
            cv.circle(self.resultColored,(intersection.x,intersection.y),3,colorBlue,3)

    def showResults(self, mask = False, resultColored = False, original = True):

        if mask:
            cv.imshow("Mask", self.mask)

        if resultColored:
            cv.imshow("Result", self.resultColored)

        if original:
            cv.imshow("Original", self.frame)


        cv.waitKey(0)
        cv.destroyAllWindows()
