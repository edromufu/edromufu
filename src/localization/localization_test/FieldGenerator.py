import cv2 as cv
import numpy as np
from numpy import sin, cos
import ParticleFilter as pf
import time


class FieldGenerator():

    # Atributos que definem as dimensões e características do campo.
    fieldLenght = 675       # Comprimento do campo
    fieldWidth = 450        # Largura do campo
    goalDepth = 60          # Profundidade do gol
    goalWidth = 260         # Largura do gol
    goalAreaDepth = 60      # Profundidade da área do gol
    goalAreaWidth = 300     # Largura da área do gol
    penaltySpot = 135       # Ponto de Penalty
    centralCircle = 110     # Diâmetro do Círculo central
    padding = 100           # Margem ao redor do campo de futebol.
    penaltyMArkDist = 135   # Distância da marca do penalty
    penaltyAreaDepth = 000  # Profundidade da área de Penalty
    penaltyAreaWidth = 000  # Largura da área de Penalty
    lineWidth = 5           # Largura da linha

    
    # Possuem uma tupla contendo as coordenadas (x, y), um nome e um código. x cresce para a esquerda e y para baixo
    # 0 = meio do campo      
    # 1 = marca de penalty     
    # 2 = interseção dupla    
    # 3 = interseção tripla     
    # 4 = trave esquerda,
    # 5 = trave direita
    # Define as coordenadas das interseções nos quatro cantos do campo.
    nwField = [(padding,padding),'nwField',2]                           # Interseção superior esquerda do campo
    neField = [(padding+fieldLenght,padding),'neField',2]               # Interseção superior direita do campo
    swField = [(padding,padding+fieldWidth),'swField',2]                # Interseção inferior direita do campo
    seField = [(padding+fieldLenght,padding+fieldWidth),'seField',2]    # Interseção inferior esquerda do campo

    # Define as coordenadas da linha central e do centro do campo.
    middleN = [(int(padding+fieldLenght/2),padding),'midleN',3]                 # Interseção superior da linha central
    middleS = [(int(padding+fieldLenght/2),padding+fieldWidth),'midleS',3]      # Interseção inferior da linha central
    middle = [(int(padding+fieldLenght/2),int(padding+fieldWidth/2)),'middle',0]  # Ponto central do campo

    # Define as coordenadas da interseção do círculo
    NCenterCircle = [(int(padding+fieldLenght/2),int(padding+(fieldWidth+centralCircle)/2)),'upCenterCircle',6]
    SCenterCircle = [(int(padding+fieldLenght/2),int(padding+(fieldWidth-centralCircle)/2)),'downCenterCircle',6]

    # Define as coordenadas das interseções da área do gol do lado esquerdo.
    nwLGoalArea = [(padding,int(padding+fieldWidth/2-goalAreaWidth/2)),'nwLGoalArea',3] # Interseção superior esquerda da área do gol esquerdo
    neLGoalArea = [(padding+goalAreaDepth,int(padding+fieldWidth/2-goalAreaWidth/2)),'neLGoalArea',2] # Interseção superior direita da área do gol esquerdo
    swLGoalArea = [(padding,int(padding+fieldWidth/2+goalAreaWidth/2)),'swLGoalArea',3] # Interseção inferior esquerda da área do gol esquerdo
    seLGoalArea = [(padding+goalAreaDepth,int(padding+fieldWidth/2+goalAreaWidth/2)),'seLGoalArea',2] # Interseção superior direita da área do gol esquerdo

    # Define as coordenadas das interseções da área do gol do lado direito.
    nwRGoalArea = [(padding+fieldLenght-goalAreaDepth,int(padding+fieldWidth/2-goalAreaWidth/2)),'nwRGoalArea',2]   # Interseção superior esquerda da área do gol direito
    neRGoalArea = [(padding+fieldLenght,int(padding+fieldWidth/2-goalAreaWidth/2)),'neRGoalArea',3] # Interseção superior direita da área do gol direito
    swRGoalArea = [(padding+fieldLenght-goalAreaDepth,int(padding+fieldWidth/2+goalAreaWidth/2)),'swRGoalArea',2]   # Interseção inferior esquerda da área do gol direito
    seRGoalArea = [(padding+fieldLenght,int(padding+fieldWidth/2+goalAreaWidth/2)),'seRGoalArea',3] # Interseção superior direita da área do gol direito

    # Define as coordenadas das interseções dos gols.
    nwLGoal = [(padding-goalDepth,int(padding+fieldWidth/2-goalWidth/2)),'nwLGoal'] # Não vai ser considerada, parte de trás superior do gol esquerdo
    neLGoal = [(padding,int(padding+fieldWidth/2-goalWidth/2)),'neLGoal',4] # Interseção da trave superior esquerda
    seLGoal = [(padding,int(padding+fieldWidth/2+goalWidth/2)),'seLGoal',5] # Interseção da trave inferior esquerda

    nwRGoal = [(padding+fieldLenght,int(padding+fieldWidth/2-goalWidth/2)),'nwRGoal',5] # Interseção da trave superior direita
    swRGoal = [(padding+fieldLenght,int(padding+fieldWidth/2+goalWidth/2)),'swRGoal',4] # Interseção da trave inferior direita
    seRGoal = [(padding+fieldLenght+goalDepth,int(padding+fieldWidth/2+goalWidth/2)),'seRGoal'] # Não vai ser considerada, parte de trás inferior do gol direito 

    # Define as coordenadas da marca de penalty
    LPenaltyMark = [(padding+penaltyMArkDist,int(padding+fieldWidth/2)),'LPenaltyMark',1]    # Ponto da marca do penalty esquerdo
    RPenaltyMark = [(padding+fieldLenght-penaltyMArkDist,int(padding+fieldWidth/2)),'RPenaltyMark',1]   # Ponto da marca do penalty direito

    # Define as coordenadas das interseções das áreas de penalty do lado esquerdo.
    nwLPenaltyArea = [(padding,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'nwLPenaltyArea',3]    # Interseção superior esquerda da área do gol direito
    neLPenaltyArea = [(padding+penaltyAreaDepth,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'neLPenaltyArea',2]   # Interseção superior direita da área do gol direito
    swLPenaltyArea = [(padding,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'swLPenaltyArea',3]    # Interseção inferior esquerda área do gol direito
    seLPenaltyArea = [(padding+penaltyAreaDepth,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'seLPenaltyArea',2]   # Interseção inferior direita da área do gol direito
    
    # Define as coordenadas das interseções das áreas de penalty do lado direito.
    nwRPenaltyArea = [(padding+fieldLenght-penaltyAreaDepth,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'nwRPenaltyArea',2]   # Interseção superior esquerda da área do gol direito
    neRPenaltyArea = [(padding+fieldLenght,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'neRPenaltyArea',3]    # Interseção superior direita da área do gol direito
    swRPenaltyArea = [(padding+fieldLenght-penaltyAreaDepth,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'swRPenaltyArea',2]   # Interseção inferior esquerda da área do gol direito
    seRPenaltyArea = [(padding+fieldLenght,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'seRPenaltyArea',3]    # Interseção inf direita da área do gol direito

    # Lista todas as interseções do campo.
    fieldIntersections = [
        nwField, neField, swField, seField, # Cantos do campo
        middleN, middleS,   # Linha central
        nwLGoalArea, neLGoalArea, swLGoalArea, seLGoalArea, # Área do gol esquerdo
        nwRGoalArea, neRGoalArea, swRGoalArea, seRGoalArea, # Área do gol direito
        neLGoal, seLGoal, nwRGoal, swRGoal, # Traves dos gols
        LPenaltyMark,RPenaltyMark,
        #nwLPenaltyArea, neLPenaltyArea, swLPenaltyArea, seLPenaltyArea, # Área do Penalty esquerdo
        #nwRPenaltyArea, neRPenaltyArea, swRPenaltyArea, seRPenaltyArea, # Área do Penalty direito
        middle, #Meio do campo
        NCenterCircle, SCenterCircle # Interseções do círculo central
    ]

    # Cria uma representação visual do campo.
    def generate():
        # Cria uma matriz vazia que representa o campo de futebol.
        field = np.zeros((FieldGenerator.padding*2+FieldGenerator.fieldWidth, # Comprimento da imagem
                          FieldGenerator.padding*2+FieldGenerator.fieldLenght)) # Largura da imagem
        
        # Desenha as bordas do campo.
        cv.rectangle(field, # Imagem
                     FieldGenerator.nwField[0], FieldGenerator.seField[0], # Canto superior esquerdo e canto inferior direito
                     255, 1) # Cor e Espessura

        # Desenha a linha central e o círculo central.
        cv.line(field, # Imagem
                FieldGenerator.middleN[0], FieldGenerator.middleS[0], # Ponto inicial e final
                255, 1) # Cor e Espessura
        cv.circle(field, # Imagem
                  FieldGenerator.middle[0], # (x,y) do centro
                  int(FieldGenerator.centralCircle/2), # Raio do círculo
                  255, 1) # Cor e Espessura

        # Desenha as áreas do gol.
        cv.rectangle(field, FieldGenerator.nwLGoalArea[0],FieldGenerator.seLGoalArea[0], 255, 1)
        cv.rectangle(field, FieldGenerator.nwRGoalArea[0],FieldGenerator.seRGoalArea[0], 255, 1)

        cv.rectangle(field, FieldGenerator.nwLGoal[0], FieldGenerator.seLGoal[0], 255, 1)
        cv.rectangle(field, FieldGenerator.nwRGoal[0], FieldGenerator.seRGoal[0], 255, 1)

        # Desenha as áreas de penalty.
        cv.rectangle(field, FieldGenerator.nwLPenaltyArea[0],FieldGenerator.seLPenaltyArea[0], 255, 1)
        cv.rectangle(field, FieldGenerator.nwRPenaltyArea[0],FieldGenerator.seRPenaltyArea[0], 255, 1)

        '''# Test
        poly = fu.getFOV(FieldGenerator.nwRGoalArea[0],0,np.pi*3/2, maxRange=180, minRange=60)
        print(poly)
        cv.polylines(field, np.int32([poly]), True, 255, 1)
        point = (600,400)
        polygon = fu.getPolygon(poly)
        print(fu.checkPointInPoly(polygon, point))
        cv.circle(field, point, 2, 255, 1)'''

        # Dilata as linhas para aumentar sua largura e retorna a imagem do campo.
        field = cv.dilate(field, np.ones((FieldGenerator.lineWidth,FieldGenerator.lineWidth)), iterations=1)

        return field
        
    # Converte a imagem do campo para colorida e desenha círculos coloridos nas interseções.
    def drawInField(field):
        coloredField = cv.cvtColor(field.astype('uint8'),cv.COLOR_GRAY2BGR) #Converte a imagem do campo de escala de cinza para BGR (colorida).
        
        # Desenha círculos coloridos nas interseções do campo. A cor é determinada pelo código de cor da interseção.
        for intersection in FieldGenerator.fieldIntersections:
            if intersection[2] == 2: color = [0,255,0]  # Verde
            elif intersection[2] == 3: color = [0,0,255] # Vermelho
            elif intersection[2] in (4,5): color = [255,0,0] # Azul
            else: color = [139,0,139] # Roxo?
            cv.circle(coloredField,intersection[0],5,color,5)

        return coloredField
    
    # Desenha múltiplas partículas no campo.
    def drawParticles(coloredField, particles, drawFov=False, fov=0, minRange=0, maxRange=3,neckAngle=0):
        # Chama drawParticle para cada partícula.
        for particle in particles:
            coloredField = FieldGenerator.drawParticle(coloredField,(particle[0],particle[1],particle[2],neckAngle),fov,minRange,maxRange,drawFov=drawFov)

        return coloredField
    
    # Desenha uma única partícula no campo, com opção de desenhar o campo de visão (FOV). 
    def drawParticle(coloredField, particle, fov, minRange, maxRange, drawFov=True, color=[255,0,0], robo=False):

        # Define o tamanho do círculo da partícula com base se é um robô ou não.
        if robo: size = 3
        else: size = 2
        
        # Desenha um círculo em coloredField representando a partícula na posição (particle[0], particle[1]).
        cv.circle(coloredField,(particle[0],particle[1]),size,color,size) 

        # Se drawFov for verdadeiro, desenha o campo de visão da partícula usando linhas e elipses.
        if drawFov:
            # Limites laterais mínimo e máximo do campo de visão 
            cv.line(coloredField, (int(particle[0]+minRange*np.cos((particle[2]+particle[3])*np.pi/180+fov/2)),int(particle[1]+minRange*np.sin((particle[2]+particle[3])*np.pi/180+fov/2))),(int(particle[0]+maxRange*np.cos((particle[2]+particle[3])*np.pi/180+fov/2)),int(particle[1]+maxRange*np.sin((particle[2]+particle[3])*np.pi/180+fov/2))), [150,0,0],size)
            cv.line(coloredField, (int(particle[0]+minRange*np.cos((particle[2]+particle[3])*np.pi/180-fov/2)),int(particle[1]+minRange*np.sin((particle[2]+particle[3])*np.pi/180-fov/2))),(int(particle[0]+maxRange*np.cos((particle[2]+particle[3])*np.pi/180-fov/2)),int(particle[1]+maxRange*np.sin((particle[2]+particle[3])*np.pi/180-fov/2))),[150,0,0],size)
            # Arcos que definem a distância minima e máxima do campo de visão
            cv.ellipse(coloredField, (particle[0],particle[1]), 
                       (minRange,minRange), 0,
                       int((particle[2]+particle[3])-180*fov/(np.pi*2)), 
                       int((particle[2]+particle[3])+180*fov/(np.pi*2)), 
                       [150,0,0], size)
            cv.ellipse(coloredField, (particle[0],particle[1]), 
                       (maxRange,maxRange), 0,
                       int((particle[2]+particle[3])-180*fov/(np.pi*2)), 
                       int((particle[2]+particle[3])+180*fov/(np.pi*2)), 
                       [150,0,0], size)  
         # Se drawFov for falso, desenha uma linha representando a direção da partícula.
        cv.line(coloredField,
                (particle[0],particle[1]),
                (int(particle[0]+size*3*np.cos((particle[2])*np.pi/180)),int(particle[1]+size*3*np.sin((particle[2])*np.pi/180))),
                color,
                size)

        return coloredField # Retorna a imagem do campo com a partícula desenhada.