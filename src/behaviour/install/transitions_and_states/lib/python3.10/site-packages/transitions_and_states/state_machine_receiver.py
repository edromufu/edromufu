#!/usr/bin/env python3
#coding=utf-8

import rclpy
import os, sys
from state_machine import StateMachine
from modularized_bhv_msgs.msg import StateMachineMsg  # Mensagem do ROS

edrom_dir = '/home/' + os.getlogin() + '/edromufu/src/'

sys.path.append(edrom_dir + 'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters


class StateMachineReceiver(StateMachine):

    def __init__(self, node):
        """
        Construtor:
        - Inicializa o objeto responsável pelas transições
        - Constrói o subscriber do ROS responsável pelo recebimento das variáveis
        """
        super().__init__()  # Inicializa a classe StateMachine

        self.node = node  # Recebe a instância do node
        self.parameters = BehaviourParameters()

        # Subscriber para o tópico de variáveis da StateMachine
        self.node.create_subscription(StateMachineMsg, self.parameters.stateMachineTopic, self.call_state_machine_update, 10)
    
    # Callback do subscriber das variáveis interpretadas pelos módulos de interpretação
    def call_state_machine_update(self, stateMachineVars):
        """
        -> Função:
        Atualiza o estado sempre que uma variável é alterada, através de:
            - Extrair as variáveis da mensagem recebida na ordem estabelecida
            - Chamar o método do objeto da state machine com as variáveis 
        -> Input:
            - stateMachineVars: Variável associada à mensagem recebida no tópico do ROS, contendo todas as
            informações enviadas pelo ROS packer, que são extraídas para atualização   
        """
        self.request_state_machine_update(stateMachineVars.ballPosition, stateMachineVars.ballClose, 
                                          stateMachineVars.ballFound, stateMachineVars.fallState,
                                          stateMachineVars.horMotorOutOfCenter, stateMachineVars.headKickCheck)


def main(args=None):
    rclpy.init(args=args)
    
    # Inicializa o node no ROS 2
    node = rclpy.create_node('State_machine_node')

    # Cria a instância do receptor da StateMachine
    receiver = StateMachineReceiver(node)

    # Mantém o node ativo
    rclpy.spin(node)

    receiver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
