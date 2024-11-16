import numpy as np


#newFootPosition -> coordenadas x tempo
def IKAnalitica(newFootRelPosition, currentFoot, robotik): 
    # newFootRelPosition: posição relativa entre o passo anterior até a posição desejada, com origem no COM
    # currentFoot -1(último elemento) para se referir ao pé direito e -2(penúltimo elemento) para se referir ao pé esquerdo
    # robotik: uma lista de objetos(Joints) que junta todas as informações do objeto/junta que estão no arquivo .json

    # Constantes das partes da robô
    
    #Vector = robotik[10].__mother2SelfVec
    #NormaVector = np.linalg.norm(Vector)

    a = 0.085
    #b = 0.11825
    #c = 0.11825
    d = 0.085
    e = 0.040

    #! Pegar valores do json
    com2hipUX = 0 # Distância do Hip UX até o COM em z
    hipUX2hipUY = -0.03598 # Distância do Hip UX até o Hiṕ UY em z
    ankleUY2ankleUX = -0.03467  # Distância do Ankle UY até a Ankle UX em z
    ankleUX2foot = -0.02004 # Distância do Ankle UX até a base do pé em z
 
    yCOM = 0.06206  # Distância do COM até o HipUX em y


    # Limites em ângulo
    max_alfa = 130*np.pi/180
    max_beta = 127*np.pi/180
    max_gama = 30*np.pi/180
    max_epsilon = 6*np.pi/180

    min_alfa = 90*np.pi/180
    min_beta = 90*np.pi/180
    min_gama = -30*np.pi/180
    min_epsilon = -6*np.pi/180

    vecb = robotik[3].__mother2SelfVec
    b = np.linalg.norm(vecb) # Calcula a norma/modulo do vector que expressa a distancia entre a junta mãe do joelho até a junta do joelho 


    vecc = robotik[4].__mother2SelfVec
    c = np.linalg.norm(vecc) # Calcula a norma/modulo do vector que expressa a distancia entre a junta do joelho até a junta do tornozelo




    # Separa as coordenadas da nova posição
    x = newFootRelPosition[0]
    y = newFootRelPosition[1]
    z = newFootRelPosition[2]


    # Eixo Y cresce para a esquerda da robô
    if currentFoot==-1: # Pé direito
        y=y+yCOM # Soma a distância do meio da perna direita (valor negativo de y) até o COM
    elif currentFoot==-2:    # Pé esquerdo
        y=y-yCOM # Subtrai a distância do meio da perna esquerda (valor positivo de y) até o COM
    else:
        y=0

    if y > yCOM:
        y=yCOM
        print(f"Y acima do limite estipulado, corrigindo para {y}")
    elif y < -yCOM:
        y=-yCOM
        print(f"Y abaixo do limite estipulado, corrigindo para {y}")

    

    # Cálculo de valores para a Cinemática Inversa

    # Subtrai as distâncias até o COM e o pé referentes as juntas UX, 
    # O valor recebido pela função será do COM ao pé, o cálculo refere-se do Hip ao Ankle
    zHip2AnkleUX = z + ankleUX2foot + com2hipUX
    
    z2Hip2AnkleUXmax = 0.34673 # Perna estendida, do Hip UY ao Ankle UY
    z2Hip2AnkleUXmin = 0.29630 # Perna dobrada ao máximo

    if y**2+zHip2AnkleUX**2 > z2Hip2AnkleUXmax**2:
        zHip2AnkleUX = np.sqrt(z2Hip2AnkleUXmax**2-y**2)
        print(f"Z acima do limite, corrigindo para {zHip2AnkleUX - ankleUX2foot - com2hipUX}")
        
    elif y**2+zHip2AnkleUX**2 < z2Hip2AnkleUXmin**2:
        zHip2AnkleUX = np.sqrt(z2Hip2AnkleUXmin**2-y**2)
        print(f"Z abaixo do limite, corrigindo para {zHip2AnkleUX - ankleUX2foot - com2hipUX}")


    z2Hip2AnkleUX = np.sqrt(zHip2AnkleUX**2+y**2)
    zHip2AnkleUY = z2Hip2AnkleUX + hipUX2hipUY + ankleUY2ankleUX
  
    H = np.sqrt((zHip2AnkleUY-e)**2+x**2)

    cos=-(b**2+c**2-H**2)/2*b*c
    
    #!    
    cos = np.clip(-(b**2 + c**2 - H**2) / (2 * b * c), -1, 1)


    if cos>1: cos=1 
    elif cos<-1: cos=-1

    theta = np.arccos(cos)

    ro = np.arcsin(c*np.sin(theta)/H)
    phi = np.arcsin(b*np.sin(theta)/H)

    # Ângulos da robo, iguais a 0 quando perna reta
    alfa = ro + np.arctan2(x,zHip2AnkleUY - e)           #angulo do joelho superior
    beta = phi + np.arctan2(zHip2AnkleUY-e,x)-np.pi*0.5   #angulo do joelho inferior


    if alfa > max_alfa: alfa = max_alfa
    elif alfa < min_alfa: alfa = min_alfa

    if beta > max_beta: beta = max_beta
    elif beta < min_beta: beta = min_beta

    gama = np.arctan2(y,zHip2AnkleUX)   # Angulo da cintura em torno de x
    epsilon = - gama         # Angulo do tornozelo em torno de x

    if gama > max_gama: gama = max_gama
    elif gama < min_gama: gama = min_gama

    if epsilon > max_epsilon: epsilon = max_epsilon
    elif epsilon < min_epsilon: epsilon = min_epsilon


    pot = [gama,alfa-np.pi/2,beta-np.pi/2,epsilon]
    
    return pot

IKAnalitica([-0.0186,-0.157, 0.2764-0.08],0,0)