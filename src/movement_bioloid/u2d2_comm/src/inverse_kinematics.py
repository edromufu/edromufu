
import os
import math
import time
from dynamixel_sdk_comm_no_ros import u2d2Control
import sympy as sp

pi = math.pi

defasagem_x = 0
defasagem_y = 0
defasagem_z = 0

hip2knee_z = 7.6
knee2ankle_z = 7.1
hip2knee_x = 1.6
knee2ankle_x = 2.2

def pos2rad(pos):
    if type(pos) == type([0]): 
        rad = []
        for i in pos:
            rad.append((((i-512)/1024) * 300) * pi/180)
    else: 
        rad = (((pos-512)/1024) * 300) * pi/180
    
    return rad

def rad2pos(rad):
    return int((rad*180*1024)/(300*pi)+512)

def pos2deg(pos):
    if type(pos) == type([0]): 
        deg = []
        for i in pos:
            deg.append(((i-512)/1024) * 300)
    else: 
        deg = ((pos-512)/1024) * 300
    
    return deg

def deg2rad(deg):
    return deg * pi/180

def leftFoot(positions):

    positions[17] = rad2pos(pos2rad(positions[11])-pos2rad(positions[13]))
    positions[15] = positions[9]
    return positions

def rightFoot(x,y,z, positions):
    return positions

def kinematics(positions):

    positions = pos2rad(positions)
    x = math.sin(positions[11])*(hip2knee_z + math.cos(-positions[13])*knee2ankle_z) + math.cos(positions[11])*math.sin(-positions[13])*knee2ankle_z 
    y = math.sin(positions[9])*(hip2knee_z + math.cos(positions[13])*knee2ankle_z)
    z = math.cos(positions[9])*math.cos(positions[11])*(hip2knee_z + math.cos(positions[13])*knee2ankle_z)

    return [x,y,z]

def inverseKinematics(x,y,z):

    #Sympy muito lento, tentar Scipy

    motor9 = sp.Symbol('motor9', real = True)
    motor11 = sp.Symbol('motor11', real = True)
    motor13 = sp.Symbol('motor13', real = True)

    eq1 = sp.Eq(sp.sin(motor11)*(hip2knee_z + sp.cos(-motor13)*knee2ankle_z) + sp.cos(motor11)*sp.sin(-motor13)*knee2ankle_z, x)
    eq2 = sp.Eq(sp.sin(motor9)*(hip2knee_z + sp.cos(motor13)*knee2ankle_z), y)
    eq3 = sp.Eq(sp.cos(motor9)*sp.cos(motor11)*(hip2knee_z + sp.cos(motor13)*knee2ankle_z), z)

    sp.solve([eq1,eq2,eq3],motor9,motor11,motor13)

    return motor9,motor11,motor13

if __name__ == '__main__':

    u2d2 = u2d2Control()
    positions = u2d2.feedback()
    
    
    #positions = 20 * [512]
    #u2d2.data2motors(positions)

    #positions = u2d2.feedback()
    x,y,z = kinematics(positions)
    inversa = inverseKinematics(x,y,z+2)

    #positions = leftFoot(positions)
    #positions = rightFoot(x,y,z,positions)
    
    print(positions)
    print(kinematics(positions))
    print(f'{positions[9]} {positions[11]} {positions[13]}')
    print(inversa)

