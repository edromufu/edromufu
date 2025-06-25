#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
from controller import Supervisor
from sensors_update import RobotSensors
from move_head import HeadMover
from robot_3D_moves import Robot3DMover
from sim_page_exec import RobotPagesExec


#No ROS2, herda-se um nó para maior encapsulamento e trazer as funções naturais de um nó ROS2
class BhvIndependentSim(Node):
    
    def __init__(self):
        """
        Construtor:
        - Faz a chamada de funções para definir as variáveis de node, field e ros de cada componente da simulação:
            -> Motores da cabeça;
            -> Acelerômetro;
            -> Câmera.
        """
        self.general_supervisor = Supervisor()

        self.robot_sensors = RobotSensors(self.general_supervisor)
        self.robot_head_requisitions = HeadMover(self.general_supervisor)
        self.robot_3D_move_requisitions = Robot3DMover(self.general_supervisor)
        self.robot_pages_requisitions = RobotPagesExec(self.general_supervisor)

       

    #Função para loopar os updates dos sensores durante a execução da simulação
    def start(self):
        while self.general_supervisor.step(32) != -1 and rclpy.ok():
                self.robot_sensors.callClock()
                self.robot_3D_move_requisitions.callClock()
                self.robot_head_requisitions.callClock()
                self.ballUpdate()

    def init_ball(self):
        self.ball = self.general_supervisor.getFromDef('ball')
        self.ball_trans_field = self.ball.getField("translation")
    
    def ballUpdate(self):
        [x, y, z] = self.ball_trans_field.getSFVec3f()

        if z < 2 and x <=0:
            self.ball.addForce([0,0,0.005],False)
        if z >= 2 and x <2.5:
            self.ball.addForce([0.005,0,0],False)
        if z >= -2 and x >=2.5:
            self.ball.addForce([0,0,-0.005],False)
        if z <= -2 and x >0:
            self.ball.addForce([-0.005,0,0],False)
    
def main():
    rclpy.init(args=args)
    
    simulator = BhvIndependentSim()
    
    try:
        simulator.start()
        rclpy.spin(simulator)
    except Exception as e:
        simulator.get_logger().error(f'Erro na simulação: {str(e)}')
    finally:
        simulator.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

