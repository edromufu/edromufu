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
    h_pe = 0.05656 #Distância da base do pé até o eixo do tornozelo
    h_torso = 0.0525 #Distância da base do tronco até o eixo da cintura

    #! Pegar valores do json, corrigir um dos pares de h de acordo com o vermelho e renomear as var
    h_peY=0  # Distância do Ankle UY até a Ankle UX   #! ankleUX2UY
    h_peX=0  # Distância do Ankle UX até a base do pé  #! ground2AnkleUX
    h_troncoX=0 # Distância do Hip UX até o Hip UY #! hipUY2UX
    h_troncoY=0 # Distância do Hip UY até o COM #!com2hipUY

    

    # Limites em ângulo
    max_alfa = 130
    max_beta = 127
    max_gama = 30
    max_epsilon = 6

    min_alfa = 90
    min_beta = 90
    min_gama = -30
    min_epsilon = -6

    vecb = robotik[3].__mother2SelfVec
    b = np.linalg.norm(vecb) # Calcula a norma/modulo do vector que expressa a distancia entre a junta mãe do joelho até a junta do joelho 


    vecc = robotik[4].__mother2SelfVec
    c = np.linalg.norm(vecc) # Calcula a norma/modulo do vector que expressa a distancia entre a junta do joelho até a junta do tornozelo
    
    #! yCom distância do COM as pernas, pegar do json
    yCOM = 0


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

    #! Limites do y, ysep=ycom
    if y > ysep:
        y=ysep
        print(f"Y acima do limite estipulado, corrigindo para {y}")
    elif y < -ysep:
        y=-ysep
        print(f"Y abaixo do limite estipulado, corrigindo para {y}")

    

    # Cálculo de valores para a Cinemática Inversa

    #! Terminar
    #! zHip2AnkleUX, o z do desenho
    z_relativo= z-h_troncoX-h_peX

    #! z2Hip2AnkleUX, o z' do desenho debaixo
    z2 = np.sqrt(z_relativo**2+y**2)

    #! z2Hip2AnkleUY, o z' do desenho de cima
    zlinha_relativo=z2-h_troncoY-h_peY

    #! limites do z
    #! z debaixo, z'max debaixo e z'min debaixo que dependem do z' de cima
    if y**2+z**2 > z_linhaMax**2:
        z = np.sqrt(z_linhaMax**2-y**2)
        print(f"Z acima do limite, corrigindo para {z}")
        
    elif y**2+z**2 < z_linhaMin**2:
        z = np.sqrt(z_linhaMin**2-y**2)
        print(f"Z abaixo do limite, corrigindo para {z}")


    H = np.sqrt((z2-e)**2+x**2)

    cos=-(b**2+c**2-H**2)/2*b*c

    if cos>1: cos=1 
    elif cos<-1: cos=-1

    theta = np.arccos(cos)

    ro = np.arcsin(c*np.sin(theta)/H)
    phi = np.arcsin(b*np.sin(theta)/H)

    # Ângulos da robo, iguais a 0 quando perna reta
    alpha = ro + np.arctan2(x,z2 - e)           #angulo do joelho superior
    beta = phi + np.arctan2(z2-e,x)-np.pi*0.5   #angulo do joelho inferior


    #! Converter max angulos para radianos
    if alfa > max_alfa: alfa = max_alfa
    elif alfa < min_alfa: alfa = min_alfa

    if beta > max_beta: beta = max_beta
    elif beta < min_beta: beta = min_beta

    #! Usar o z do desenho debaixo
    gama = np.arctan2(y,z)   #angulo da cintura em torno de x
    epsilon = - gama         #anuglo do tornozelo em torno de x


    #! Terminar
    # Subtrai as distâncias até o COM e o pé referentes as juntas UX, 
    # O valor recebido pela função será do COM ao pé, o cálculo refere-se do Hip ao Ankle
    z=Z-h_peX-h_troncoX

    #! converter max angulos para radianos
    if gama > max_gama: gama = max_gama
    elif gama < min_gama: gama = min_gama

    if epsilon > max_epsilon: epsilon = max_epsilon
    elif epsilon < min_epsilon: epsilon = min_epsilon






    print("angulos",np.rad2deg(alpha+np.pi*0.5),np.rad2deg(beta+np.pi*0.5),np.rad2deg(gama),np.rad2deg(epsilon),sep='\n')
    
    '''
    HipUY = - alpha ?
    HipUX = gama
    KneeSuperiorUY = alpha
    KneeInferiorUY = beta
    AnkleUX = epsilon
    AnkleUY = - beta ?
    '''
   
    #return 

IKAnalitica([-0.0186,-0.157, 0.2764-0.08],0,0)


'''
#alpha e gama subtraem 90º
angulos
39.86991548933679
-7.256445781353683
90.0
-90.0


angulos
32.268357994500555
0.5145575910333139
21.173074012510135
-21.173074012510135

#Não subtrai 90º
angulos
111.1426976946338
121.19724156534168
-38.63845579066379
38.63845579066379
'''