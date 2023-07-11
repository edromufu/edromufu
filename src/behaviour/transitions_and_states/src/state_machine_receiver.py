#!/usr/bin/env python3
#coding=utf-8

import rospy
from state_machine import StateMachine

from modularized_bhv_msgs.msg import stateMachineMsg

class StateMachineReceiver(StateMachine):

    def __init__(self):
        """
        Construtor:
        - Inicializa o objeto responsável pelas transições
        - Construção do subscriber do ROS responsável pelo recebimento das variáveis
        """

        self.state_machine = StateMachine()
        rospy.Subscriber('/sensor_observer/state_machine_vars', stateMachineMsg, self.call_state_machine_update)
    
    #Callback do subscriber das variáveis interpretados pelos módulos de interpretação
    def call_state_machine_update(self, stateMachineVars):
        """
        -> Funcao:
        Chamar a atualização de estado sempre que uma variável é alterada, atraves de:
            - Extrair as variaveis da mensagem recebida na ordem estabelecida
            - Chamar o metodo do objeto da state machine com as variaveis 
        -> Input:
            - stateMachineVars: Variavel associada a mensagem recebida no topico do ROS, contem todas as
            informações enviadas pelo ROS packer, da qual são extraidas para atualização   
        """

        self.state_machine.request_state_machine_update(stateMachineVars.fallState, stateMachineVars.ballFound, 
        stateMachineVars.ballClose, stateMachineVars.ballRelativePosition, stateMachineVars.verAngleAccomplished, 
        stateMachineVars.headPossibleMovements, stateMachineVars.horMotorOutOfCenter)
    
if __name__ == '__main__':
    rospy.init_node('State_machine_node', anonymous=False)

    receiver = StateMachineReceiver()
    rospy.spin()


