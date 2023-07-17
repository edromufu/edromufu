from numpy import sin, cos

class Intersection:


    def __init__(self, x, y, reta1, reta2):
        self.x = x
        self.y = y
        self.reta1 = reta1
        self.reta2 = reta2
        self.classe = None
        self.label = None

    def vizinhos(self, distancia):
        vizinho1 = (int(self.x + distancia*(-sin(self.reta1[1]))), int(self.y + distancia*(cos(self.reta1[1]))))
        vizinho2 = (int(self.x + distancia*(-sin(self.reta2[1]))), int(self.y + distancia*(cos(self.reta2[1]))))
        vizinho3 = (int(self.x - distancia*(-sin(self.reta1[1]))), int(self.y - distancia*(cos(self.reta1[1]))))
        vizinho4 = (int(self.x - distancia*(-sin(self.reta2[1]))), int(self.y - distancia*(cos(self.reta2[1]))))


        return vizinho1, vizinho2, vizinho3, vizinho4

    def classificar(self,classe):
        self.classe = classe

    def nomear(self,label):
        self.label = label

    def __str__(self):
        string = f'X = {self.x}\nY = {self.y}\nClasse = {self.classe}'
        return string