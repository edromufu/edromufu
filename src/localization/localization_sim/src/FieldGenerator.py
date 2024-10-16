import cv2 as cv
import numpy as np
from numpy import sin, cos
from Intersection import Intersection
import ParticleFilter as pf
import time


class FieldGenerator():

    fieldLenght = 900
    fieldWidth = 600
    goalDepth = 60
    goalWidth = 260
    goalAreaDepth = 100
    goalAreaWidth = 300
    penaltySpot = 150
    centralCircle = 150
    padding = 100
    penaltyAreaDepth = 200
    penaltyAreaWidth = 500
    lineWidth = 5

    #Intersections
    nwField = [(padding,padding),'nwField',2]
    neField = [(padding+fieldLenght,padding),'neField',2]
    swField = [(padding,padding+fieldWidth),'swField',2]
    seField = [(padding+fieldLenght,padding+fieldWidth),'seField',2]

    middleN = [(int(padding+fieldLenght/2),padding),'midleN',3]
    middleS = [(int(padding+fieldLenght/2),padding+fieldWidth),'midleS',3]
    middle = [(int(padding+fieldLenght/2),int(padding+fieldWidth/2)),'middle'] # Não é interseção

    nwLGoalArea = [(padding,int(padding+fieldWidth/2-goalAreaWidth/2)),'nwLGoalArea',3]
    neLGoalArea = [(padding+goalAreaDepth,int(padding+fieldWidth/2-goalAreaWidth/2)),'neLGoalArea',2]
    swLGoalArea = [(padding,int(padding+fieldWidth/2+goalAreaWidth/2)),'swLGoalArea',3]
    seLGoalArea = [(padding+goalAreaDepth,int(padding+fieldWidth/2+goalAreaWidth/2)),'seLGoalArea',2]

    nwRGoalArea = [(padding+fieldLenght-goalAreaDepth,int(padding+fieldWidth/2-goalAreaWidth/2)),'nwRGoalArea',2]
    neRGoalArea = [(padding+fieldLenght,int(padding+fieldWidth/2-goalAreaWidth/2)),'neRGoalArea',3]
    swRGoalArea = [(padding+fieldLenght-goalAreaDepth,int(padding+fieldWidth/2+goalAreaWidth/2)),'swRGoalArea',2]
    seRGoalArea = [(padding+fieldLenght,int(padding+fieldWidth/2+goalAreaWidth/2)),'seRGoalArea',3]

    nwLGoal = [(padding-goalDepth,int(padding+fieldWidth/2-goalWidth/2)),'nwLGoal'] # Não vai ser considerada
    neLGoal = [(padding,int(padding+fieldWidth/2-goalWidth/2)),'neLGoal',3]
    seLGoal = [(padding,int(padding+fieldWidth/2+goalWidth/2)),'seLGoal',3]

    nwRGoal = [(padding+fieldLenght,int(padding+fieldWidth/2-goalWidth/2)),'nwRGoal',3]
    swRGoal = [(padding+fieldLenght,int(padding+fieldWidth/2+goalWidth/2)),'swRGoal',3]
    seRGoal = [(padding+fieldLenght+goalDepth,int(padding+fieldWidth/2+goalWidth/2)),'seRGoal'] # Não vai ser considerada

    nwLPenaltyArea = [(padding,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'nwLPenaltyArea',3]
    neLPenaltyArea = [(padding+penaltyAreaDepth,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'neLPenaltyArea',2]
    swLPenaltyArea = [(padding,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'swLPenaltyArea',3]
    seLPenaltyArea = [(padding+penaltyAreaDepth,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'seLPenaltyArea',2]

    nwRPenaltyArea = [(padding+fieldLenght-penaltyAreaDepth,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'nwRPenaltyArea',2]
    neRPenaltyArea = [(padding+fieldLenght,int(padding+fieldWidth/2-penaltyAreaWidth/2)),'neRPenaltyArea',3]
    swRPenaltyArea = [(padding+fieldLenght-penaltyAreaDepth,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'swRPenaltyArea',2]
    seRPenaltyArea = [(padding+fieldLenght,int(padding+fieldWidth/2+penaltyAreaWidth/2)),'seRPenaltyArea',3]

    fieldIntersections = [
        nwField, neField, swField, seField,
        middleN, middleS,
        nwLGoalArea, neLGoalArea, swLGoalArea, seLGoalArea,
        nwRGoalArea, neRGoalArea, swRGoalArea, seRGoalArea,
        neLGoal, seLGoal, nwRGoal, swRGoal,
        nwLPenaltyArea, neLPenaltyArea, swLPenaltyArea, seLPenaltyArea,
        nwRPenaltyArea, neRPenaltyArea, swRPenaltyArea, seRPenaltyArea
    ]

    def generate():
        # Empty field
        field = np.zeros((FieldGenerator.padding*2+FieldGenerator.fieldWidth, FieldGenerator.padding*2+FieldGenerator.fieldLenght))
        
        # Draw borders
        cv.rectangle(field, FieldGenerator.nwField[0],FieldGenerator.seField[0], 255, 1)

        # Draw middle line
        cv.line(field, FieldGenerator.middleN[0], FieldGenerator.middleS[0], 255, 1)
        cv.circle(field, FieldGenerator.middle[0], int(FieldGenerator.centralCircle/2), 255, 1)

        # Draw goal area
        cv.rectangle(field, FieldGenerator.nwLGoalArea[0],FieldGenerator.seLGoalArea[0], 255, 1)
        cv.rectangle(field, FieldGenerator.nwRGoalArea[0],FieldGenerator.seRGoalArea[0], 255, 1)

        cv.rectangle(field, FieldGenerator.nwLGoal[0], FieldGenerator.seLGoal[0], 255, 1)
        cv.rectangle(field, FieldGenerator.nwRGoal[0], FieldGenerator.seRGoal[0], 255, 1)

        # Draw penalty area
        cv.rectangle(field, FieldGenerator.nwLPenaltyArea[0],FieldGenerator.seLPenaltyArea[0], 255, 1)
        cv.rectangle(field, FieldGenerator.nwRPenaltyArea[0],FieldGenerator.seRPenaltyArea[0], 255, 1)

        '''# Test
        poly = fu.getFOV(FieldGenerator.nwRGoalArea[0],0,np.pi*3/2, maxRange=180, minRange=60)
        print(poly)
        cv.polylines(field, np.int32([poly]), True, 255, 1)
        point = (600,400)
        polygon = fu.getPolygon(poly)
        print(fu.checkPointInPoly(polygon, point))
        cv.circle(field, point, 2, 255, 1)'''


        field = cv.dilate(field, np.ones((FieldGenerator.lineWidth,FieldGenerator.lineWidth)), iterations=1)
        return field
        
    def drawInField(field):
        coloredField = cv.cvtColor(field.astype('uint8'),cv.COLOR_GRAY2BGR)
        
        for intersection in FieldGenerator.fieldIntersections:
            if intersection[2] == 2: color = [0,255,0]
            elif intersection[2] == 3: color = [0,0,255]
            elif intersection[2] == 4: color = [255,0,0]
            cv.circle(coloredField,intersection[0],5,color,5)

        return coloredField
    
    def drawParticles(coloredField, particles, drawFov=False, fov=0, minRange=0, maxRange=3):
        for particle in particles:
            coloredField = FieldGenerator.drawParticle(coloredField,particle,fov,minRange,maxRange,drawFov=drawFov)

        return coloredField
    
    def drawParticle(coloredField, particle, fov, minRange, maxRange, drawFov=True, color=[255,0,0], robo=False):
        if robo: size = 3
        else: size = 2

        cv.circle(coloredField,(particle[0],particle[1]),size,color,size)

        if drawFov:
            cv.line(coloredField,(int(particle[0]+minRange*np.cos(particle[2]*np.pi/180+fov/2)),int(particle[1]+minRange*np.sin(particle[2]*np.pi/180+fov/2))),(int(particle[0]+maxRange*np.cos(particle[2]*np.pi/180+fov/2)),int(particle[1]+maxRange*np.sin(particle[2]*np.pi/180+fov/2))),[150,0,0],size)
            cv.line(coloredField,(int(particle[0]+minRange*np.cos(particle[2]*np.pi/180-fov/2)),int(particle[1]+minRange*np.sin(particle[2]*np.pi/180-fov/2))),(int(particle[0]+maxRange*np.cos(particle[2]*np.pi/180-fov/2)),int(particle[1]+maxRange*np.sin(particle[2]*np.pi/180-fov/2))),[150,0,0],size)
            cv.ellipse(coloredField, (particle[0],particle[1]), (minRange,minRange), particle[2]*np.pi/180, int(particle[2]-180*fov/(np.pi*2)), int(particle[2]+180*fov/(np.pi*2)), [150,0,0], size)
            cv.ellipse(coloredField, (particle[0],particle[1]), (maxRange,maxRange), particle[2]*np.pi/180, int(particle[2]-180*fov/(np.pi*2)), int(particle[2]+180*fov/(np.pi*2)), [150,0,0], size)
        else:
            cv.line(coloredField,(particle[0],particle[1]),(int(particle[0]+size*3*np.cos(particle[2]*np.pi/180)),int(particle[1]+size*3*np.sin(particle[2]*np.pi/180))),color,size)

        return coloredField