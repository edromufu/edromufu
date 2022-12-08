# -*- coding: utf-8 -*-

from transitions import Machine
import random
import time

class Goalie(object):

    states = ['S_Stand_still', 'S_Defend','S_Getting_up',
                'S_Repositioning', 'S_Live', 'S_Impossible']

    #Definição das funções com retorno de variável que serão chamadas nas conditions das transições,  
    #pois pytransitions aciona somente funções
    def robot_in_game(self) : return self.game_controller
    def robot_falling(self) : return self.falling
    def moving(self) : return self.moving
    def searching(self) : return self.searching
    def ball_found(self) : return self.ball
    def ball_close(self) : return self.ball_close
    def impossible(self) : return self.impossible

    #Função para tornar o game_controller falso sempre que sair do Estado Stand_still
    def game_started(self): 
        self.game_controller = False

    #Função necessária para ocorrer as transições do pytransitions
    def switch_state(self):
        if self.goto_Stand_still():
            return True

        elif self.goto_Defend():
            return True

        elif self.goto_Getting_up():
            return True

        elif self.goto_Repositioning():
            return True    

        else:
            return False

    #Função para feedback visual das variáveis durante testes
    def print_variables(self):
        print('falling: ' + str(self.falling))
        print('searching: ' + str(self.searching))
        print('ball: ' + str(self.ball))
        print('ball_close: ' + str(self.ball_close))
        print('moving: ' + str(self.moving))
        print('game_controller: ' + str(self.game_controller))

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
        self.searching = False # Receber um booleano da Visão quando a rede neural começar a analisar
        self.ball = False
        self.ball_close = False
        self.moving = False
        self.game_controller = False
        self.impossible = False

    def __init__(self):
        self.zero()

        self.machine = Machine(self, Goalie.states, 'S_Live')

        #!---------------------TRANSIÇÕES PARA S_Stand_still---------------------
        self.machine.add_transition('goto_Stand_still', '*', 'S_Stand_still',
            conditions=['robot_in_game'],
            unless=['robot_falling'],
            after=['game_started'])

        self.machine.add_transition('goto_Stand_still', 'S_Getting_up', 'S_Stand_still',
            unless=['robot_falling', 'moving'])

        self.machine.add_transition('goto_Stand_still', 'S_Repositioning', 'S_Stand_still',
            unless=['robot_falling', 'moving'])
        
        self.machine.add_transition('goto_Stand_still', 'S_Defend', 'S_Stand_still',
            unless=['robot_falling'])
        
        #!---------------------TRANSIÇÕES PARA S_Repositioning---------------------
        self.machine.add_transition('goto_Repositioning', 'S_Defend', 'S_Repositioning',
            conditions=['robot_falling'])

        #!---------------------TRANSIÇÕES PARA S_Defend---------------------
        self.machine.add_transition('goto_Defend', 'S_Stand_still', 'S_Defend',
            conditions=['ball_close'],
            unless=['robot_falling', 'moving'])

        #!---------------------TRANSIÇÕES PARA S_Getting_up---------------------
        self.machine.add_transition('goto_Getting_up', '*', 'S_Getting_up',
            conditions=['robot_falling'])

        #!---------------------TRANSIÇÕES PARA S_Impossible---------------------
        self.machine.add_transition('goto_Stand_still', '*', 'S_Impossible',
            conditions=['impossible'])

        self.machine.add_transition('goto_Defend', '*', 'S_Impossible',
            conditions=['impossible'])

        self.machine.add_transition('goto_Getting_up', '*', 'S_Impossible',
            conditions=['impossible'])

        self.machine.add_transition('goto_Repositioning', '*', 'S_Impossible',
            conditions=['impossible'])    