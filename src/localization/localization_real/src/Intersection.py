from numpy import sin, cos

class Intersection:


    def __init__(self, x, y, reta1, reta2):
        self.x = x
        self.y = y
        self.reta1 = reta1
        self.reta2 = reta2
        self.classe = None
        self.label = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.p1Check = False
        self.p2Check = False
        self.p3Check = False
        self.p4Check = False

    def vizinhos(self, distancia):
        vizinho1 = (int(self.x + distancia*(-sin(self.reta1[1]))), int(self.y + distancia*(cos(self.reta1[1]))))
        vizinho2 = (int(self.x + distancia*(-sin(self.reta2[1]))), int(self.y + distancia*(cos(self.reta2[1]))))
        vizinho3 = (int(self.x - distancia*(-sin(self.reta1[1]))), int(self.y - distancia*(cos(self.reta1[1]))))
        vizinho4 = (int(self.x - distancia*(-sin(self.reta2[1]))), int(self.y - distancia*(cos(self.reta2[1]))))


        return (vizinho1, vizinho2, vizinho3, vizinho4)

    def findNeighbours(self, distancia):
        self.p1 = (int(self.x + distancia*(-sin(self.reta1[1]))), int(self.y + distancia*(cos(self.reta1[1]))))
        self.p2 = (int(self.x + distancia*(-sin(self.reta2[1]))), int(self.y + distancia*(cos(self.reta2[1]))))
        self.p3 = (int(self.x - distancia*(-sin(self.reta1[1]))), int(self.y - distancia*(cos(self.reta1[1]))))
        self.p4 = (int(self.x - distancia*(-sin(self.reta2[1]))), int(self.y - distancia*(cos(self.reta2[1]))))

    def checkNeighbours(self, mask):
        ymax, xmax = mask.shape
        
        if (self.p1[1] >= 0 and self.p1[1] < ymax) and (self.p1[0] >= 0 and self.p1[0] < xmax):
            self.p1Check = (mask[self.p1[1]][self.p1[0]] == 255)
        if (self.p2[1] >= 0 and self.p2[1] < ymax) and (self.p2[0] >= 0 and self.p2[0] < xmax):
            self.p2Check = (mask[self.p2[1]][self.p2[0]] == 255)
        if (self.p3[1] >= 0 and self.p3[1] < ymax) and (self.p3[0] >= 0 and self.p3[0] < xmax):
            self.p3Check = (mask[self.p3[1]][self.p3[0]] == 255)
        if (self.p4[1] >= 0 and self.p4[1] < ymax) and (self.p4[0] >= 0 and self.p4[0] < xmax):    
            self.p4Check = (mask[self.p4[1]][self.p4[0]] == 255)

        return self.p1Check, self.p2Check, self.p3Check, self.p4Check

    def classificar(self,classe):
        self.classe = classe

    def nomear(self,label):
        self.label = label

    def __str__(self):
        string = f'X = {self.x}\nY = {self.y}\nClasse = {self.classe}'
        return string