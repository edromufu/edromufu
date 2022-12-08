# -*- coding: utf-8 -*-

from transitions import Machine
import random
import time

class Attacker(object):

    states = ['S_Stand_still', 'S_Search_ball', 'S_Walking', 'S_Kick', 
                'S_Getting_up', 'S_Live', 'S_Impossible', 'S_Body_alignment']

    #Definição das funções com retorno de variável que serão chamadas nas conditions das transições,  
    #pois pytransitions aciona somente funções
    def robot_in_game(self) : return self.game_controller
    def robot_falling(self) : return self.falling
    def finish_kicking(self) : return self.finish_kicking
    def moving(self) : return self.moving
    def searching(self) : return self.searching
    def ball_found(self) : return self.ball
    def ball_kickable(self) : return self.ball_close
    def ball_centered(self) : return self.ball_centered
    def motor_limit_reached(self) : return self.motor_limit_reached
    def impossible(self) : return self.impossible

    #Função para tornar o game_controller falso sempre que sair do Estado S_Stand_Still
    def game_started(self): 
        self.game_controller = False

    #Função necessária para ocorrer as transições do pytransitions
    def switch_state(self):
        if self.goto_Stand_still():
            return True

        elif self.goto_Search_ball():
            return True

        elif self.goto_Walking():
            return True

        elif self.goto_Kick():
            return True

        elif self.goto_Getting_up():
            return True

        elif self.goto_Body_alignment():
            return True

        else:
            return False

    #Função para feedback visual das variáveis durante testes
    def print_variables(self):
        print('falling: ' + str(self.falling))
        print('finish_kicking: ' + str(self.finish_kicking))
        print('searching: ' + str(self.searching))
        print('ball: ' + str(self.ball))
        print('ball_close: ' + str(self.ball_close))
        print('ball_centered: ' + str(self.ball_centered))
        print('moving: ' + str(self.moving))
        print('game_controller: ' + str(self.game_controller))
        print('motor_limit_reached: ' + str(self.motor_limit_reached))

    #Função para "ciclar" a máquina de Estados
    def clock(self):
        self.switch_state()

        print("-----------------------------------------------------")
        self.print_variables()
        print(" ")
        print("Estado atual: " + str(self.state))
        print("-----------------------------------------------------")
        print(" ")

    #Função para inicialização das variáveis necessárias para as transições
    def zero(self):
        self.falling = False
        self.finish_kicking = False # Receber do Movimento quando a ação de chutar for bem-sucedida
        self.searching = False # Receber um booleano da Visão quando a rede neural começar a analisar
        self.ball = False
        self.ball_close = False
        self.ball_centered = False # Receber um booleano da Visão quando a bola estiver numa área centralizada
        self.moving = False
        self.game_controller = False
        self.impossible = False

    def __init__(self):
        self.zero()

        self.machine = Machine(self, Attacker.states, 'S_Live')

        #Transições para o S_Stand_still
        self.machine.add_transition('goto_Stand_still', '*', 'S_Stand_still',
            conditions=['robot_in_game'],
            unless=['robot_falling'],
            after=['game_started'])

        self.machine.add_transition('goto_Stand_still', 'S_Kick', 'S_Stand_still',
            conditions=['finish_kicking'],
            unless=['robot_falling', 'moving'])

        self.machine.add_transition('goto_Stand_still', 'S_Getting_up', 'S_Stand_still',
            unless=['robot_falling', 'moving'])
        
        #Transições para o S_Search_ball
        self.machine.add_transition('goto_Search_ball', 'S_Stand_still', 'S_Search_ball',
            conditions=['searching'],
            unless=['robot_falling', 'moving'])

        self.machine.add_transition('goto_Search_ball', 'S_Body_alignment', 'S_Search_ball',
            conditions=['searching'],
            unless=['robot_falling', 'moving', 'motor_limit_reached'])

        #Transições para o S_Walking
        self.machine.add_transition('goto_Walking', 'S_Search_ball', 'S_Walking',
            conditions=['ball_found', 'ball_centered'],
            unless=['robot_falling', 'ball_kickable'])
            
        #Transições para o S_Kick
        self.machine.add_transition('goto_Kick', 'S_Search_ball', 'S_Kick', 
            conditions=['ball_found', 'ball_kickable'],
            unless=['robot_falling'])
        
        self.machine.add_transition('goto_Kick', 'S_Walking', 'S_Kick',
            conditions=['ball_found', 'ball_kickable'],
            unless=['robot_falling'])

        #Transições para o S_Getting_up
        self.machine.add_transition('goto_Getting_up', '*', 'S_Getting_up',
            conditions=['robot_falling'])

        #Transições para o S_Body_alignment        
        self.machine.add_transition('goto_Body_alignment', 'S_Search_ball', 'S_Body_alignment',
            conditions=['motor_limit_reached'],
            unless=['robot_falling'])

        #Transições para o S_Impossible
        self.machine.add_transition('goto_Stand_still', '*', 'S_Impossible',
            conditions=['impossible'])

        self.machine.add_transition('goto_Walking', '*', 'S_Impossible',
            conditions=['impossible'])

        self.machine.add_transition('goto_Kick', '*', 'S_Impossible',
            conditions=['impossible'])

        self.machine.add_transition('goto_Getting_up', '*', 'S_Impossible',
            conditions=['impossible'])
        
        self.machine.add_transition('goto_Search_ball', '*', 'S_Impossible',
            conditions=['impossible'])

        self.machine.add_transition('goto_Body_alignment', '*', 'S_Impossible',
            conditions=['impossible'])