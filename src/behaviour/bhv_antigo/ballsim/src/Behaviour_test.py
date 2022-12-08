#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import time
import rospy
import os 

from vision_msgs.msg import Webotsmsg
from pygame.locals import *

pygame.init()

class Ballsim(object):
    def __init__(self):
        self.found = True
        self.imageWidth = 160
        self.imageHeight = 160

        self.FPS = 30
        self.fpsClock = pygame.time.Clock()

        ##Tamanho do display
        self.size = (640, 480)

        ##Cria o display
        self.DISPLAYSURF=pygame.display.set_mode(self.size)

        ##Título do display
        pygame.display.set_caption('Behaviour_test')

        ##Carregando a imagem do fundo
        pasta_img = os.path.join(os.path.expanduser('~'), 'edrom/src/behaviour/ballsim/img')
        pasta_atual = os.getcwd()
        os.chdir(pasta_img)
        self.background = pygame.image.load('background.jpg')

        ##Carrega a imagem que vai mexer
        self.coord = pygame.image.load('bola2.png')
        os.chdir(pasta_atual)

        ##quando key=None a imagem ficará parada
        self.key=None

        ''' coord_x e coord_y são as coordenadas iniciais da imagem que iremos movimentar, onde 
            (0,0) é o canto superior esquerdo e os eixos crescem para a direita e para baixo'''
        self.coord_x = 0
        self.coord_y = 0

        #Subscrevendo o tópico da Visão
        self.pub = rospy.Publisher('objects_sim', Webotsmsg, queue_size=100)

        self.execute()

    def execute(self):
        while not rospy.is_shutdown():
            ##'Desenha' o display
            self.DISPLAYSURF.blit(self.background,(0,0))
            self.DISPLAYSURF.blit(self.coord,(self.coord_x,self.coord_y))

            ''' event é uma propriedade da biblioteca;
                ".get" pega um evento da fila, todo evento é um objeto 
                que possui o atributo type.
                keydown e keyup são os eventos quando as teclas estão 
                sendo pressionadas e quando são soltas.'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.key = event.key
                    if self.key == pygame.K_i or self.key == pygame.K_o:
                        self.scale()
                    elif self.key == pygame.K_0:
                        self.center()
                    else:
                        ##atualiza as coordenadas
                        self.coord_x, self.coord_y = self.move()
                        
                if event.type == pygame.KEYUP:
                    if (event.key == self.key):
                        self.key = None
            
            #Atualiza o found
            if(self.coord_x < -self.imageWidth or self.coord_y < -self.imageHeight or self.coord_x > self.size[0] or self.coord_y > self.size[1]):
                self.found = False
            else:
                self.found = True

            pygame.display.update()
            self.fpsClock.tick(self.FPS)
            self.publish()

    def scale(self):
        if self.key == pygame.K_i:
            self.imageHeight += 50
            self.imageWidth += 50
            self.coord = pygame.transform.scale(self.coord, (self.imageWidth, self.imageHeight))
        elif self.key == pygame.K_o:
            self.imageHeight -= 50
            self.imageWidth -= 50
            try:
                self.coord = pygame.transform.scale(self.coord, (self.imageWidth, self.imageHeight))
            except Exception:
                self.imageHeight += 50
                self.imageWidth += 50
                pass

    def center(self):
        self.coord_x = int((self.size[0]/2)) - int((self.imageWidth)/2)
        self.coord_y = int((self.size[1]/2)) - int((self.imageHeight)/2)

    def move(self):
        ''' pygame tem as constantes padrões pras teclas;
            essas que eu usei são correspondentes as setinhas do teclado '''
        if self.key:
            if self.key == pygame.K_UP:
                self.coord_y -= 20
                
            elif self.key == pygame.K_DOWN:
                self.coord_y += 20
                
            if self.key == pygame.K_LEFT:
                self.coord_x -= 20
                
            elif self.key == pygame.K_RIGHT:
                self.coord_x += 20
                
        return self.coord_x, self.coord_y
    
    def publish(self):
        msg = Webotsmsg()
        msg.ball.roi_height = self.imageHeight
        msg.ball.roi_width = self.imageWidth
        msg.ball.x = self.coord_x + int((self.imageWidth)/2) - int((self.size[0]/2))
        msg.ball.y = self.coord_y + int((self.imageHeight)/2) - int((self.size[1]/2))
        msg.ball.found = self.found
        msg.searching = True

        self.pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('Ballsim', anonymous=True)

    ballsim = Ballsim()

    rospy.spin()
