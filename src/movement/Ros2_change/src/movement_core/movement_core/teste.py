import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import sys
import numpy as np

class IKPublisher(Node):
    def __init__(self):
        super().__init__('ik_publisher')
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        self.timer_ = self.create_timer(0.1, self.publish_solution)

        self.current_joint_states = JointState()
        self.current_joint_states.name = ["R_SHLD","L_SHLD","RHIP_UX","RHIP_UY1"]  #! Nome das juntas
        #"RUKNEE_1", "RLKNEE_1","RANKLE_UY1""RHIP_UY2","RUKNEE_2""RLKNEE_2""RANKLE_UY2""RHIP_UY3""RUKNEE_3""RLKNEE_3""RANKLE_UY3""RANKLE_UX""LHIP_UX""LHIP_UY1""LUKNEE_1""LLKNEE_1""LANKLE_UY1""LHIP_UY2""LUKNEE_2""LLKNEE_2""LANKLE_UY2""LHIP_UY3""LUKNEE_3""LLKNEE_3""LANKLE_UY3""LANKLE_UY"
        self.current_joint_states.position = [0.0, 0.0, 0.0]  # Posições iniciais das juntas
        self.ik_active = False

        self.declare_parameter('current_foot', -1)
        self.current_foot = self.get_parameter('current_foot').get_parameter_value().integer_value

    def publish_solution(self):
        if self.ik_active:
            self.current_joint_states.header.stamp = self.get_clock().now().to_msg()
            self.publisher_.publish(self.current_joint_states)

    def process_input(self, input_vector):
        # Chame sua função IKAnalitica aqui
        if self.current_foot != -1 and self.current_foot != -2: self.current_foot=-1
        self.current_joint_states.position = self.IKAnalitica(input_vector,self.current_foot)
        self.ik_active = True

    def IKAnalitica(self,newFootRelPosition, currentFoot): 

        a = 0.085
        b = 0.11825
        c = 0.11825
        d = 0.085
        e = 0.040

        #! Pegar valores do json
        com2hipUX = 0 # Distância do Hip UX até o COM em z
        hipUX2hipUY = -0.03598 # Distância do Hip UX até o Hiṕ UY em z
        ankleUY2ankleUX = -0.03467  # Distância do Ankle UY até a Ankle UX em z
        ankleUX2foot = -0.02004 # Distância do Ankle UX até a base do pé em z
    
        yCOM = 0.06206  # Distância do COM até o HipUX em y

        max_alfa = 130*np.pi/180
        max_beta = 127*np.pi/180
        max_gama = 30*np.pi/180
        max_epsilon = 6*np.pi/180

        min_alfa = 90*np.pi/180
        min_beta = 90*np.pi/180
        min_gama = -30*np.pi/180
        min_epsilon = -6*np.pi/180


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
        
        return [gama,alfa,beta,epsilon]

def main(args=None):
    rclpy.init(args=args)
    ik_publisher = IKPublisher()

    while rclpy.ok():
        input_str = input("Digite o vetor [x, y, z]: ")
        try:
            input_vector = list(map(float, input_str.strip('[]').split(',')))
            ik_publisher.process_input(input_vector)
        except:
            print("Entrada inválida! Por favor, digite no formato [x, y, z]")

        rclpy.spin_once(ik_publisher, timeout_sec=0.1)

    ik_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

            