from ParticleFilter import ParticleFilter as pf
from FieldGenerator import FieldGenerator as fg

from numpy.random import randn, uniform
import numpy as np
import time
import cv2 as cv

def runVision(robot, particleFilter):

    intersections = particleFilter.checkFOV(robot)
    return intersections

def runParticleFilter(particleFilter, robotVision, robotVariaton, desvioPos, desvioAngle):
    # Atualiza a posicao das particulas de acordo com o robo
    particleFilter.predict(robotVariaton,(desvioPos,desvioAngle))

    # Testa o input das particulas (update)
    particleFilter.testParticles(robotVision)

    # Verifica se é necessario resample
    if particleFilter.neff() < (N/2):
        particleFilter.resample_from_index()

    # Calcula a media e variancia
    particleFilter.estimate()


def show2Dfield(robot,particles):
    field = fg.generate()
    field = fg.drawInField(field)
    field = fg.drawParticles(field, particles, drawFov=False, fov=fov, minRange=minRange, maxRange=maxRange)
    field = fg.drawParticle(field, robot, fov, minRange, maxRange, drawFov=False, color=[0,100,200],robo=True)
    return field

def feedbackMovement(robot, desvioPos, desvioAngle):
    initPasso = [0,30]
    passo = [int(initPasso[0]+desvioPos*randn(1)),int(initPasso[1]+desvioAngle*randn(1))]
    robot = pf.moveRobot(robot,passo)
    return robot


if __name__ == '__main__':
    
    # Parametros para o filtro de particulas
    N = 1000
    fov = np.pi/4
    minRange = 30
    maxRange = 120

    # Parametros para a robo simulada
    desvioPos = 5
    desvioAngle = 5
    initX = 200
    initY = 200
    initHeading = 0
    robot = [int(initX+desvioPos*randn(1)), 
             int(initY+desvioPos*randn(1)), 
             int(initHeading+desvioAngle*randn(1))]
    robot[2] = (robot[2]+360)%360

    particleFilter = pf(N,fov,minRange,maxRange,fg.fieldIntersections, 
                        previousPositionKnown=True, mean = [robot[0],robot[1],robot[2]], standardDeviation = [desvioPos*10,desvioPos*10,desvioAngle*10])

    robotFound = False
    showField = True

    start_time = time.time()

    while robotFound == False:
        # Obtem as intersecoes identificadas pela visao
        robotVision = runVision(robot,particleFilter)

        # Obtem o feedback da variacao da posicao e direcao do movimento
        previousPosition = np.copy(robot)
        robot = feedbackMovement(robot, desvioPos, desvioAngle)
        robotVariaton = np.subtract(robot,previousPosition)

        # Itera no filtro de particulas
        runParticleFilter(particleFilter, robotVision, robotVariaton, desvioPos, desvioAngle)

        if (particleFilter.deviation[0]+particleFilter.deviation[1]<50):
            robotFound = True

        if showField:
            field = show2Dfield(robot,particleFilter.particles)
            cv.imshow("2D Particle filter",cv.flip(field,0))
            cv.waitKey(10)
    
    end_time = time.time()

    print(f'Convergiu para ({particleFilter.mean[0]},{particleFilter.mean[1]}) com  {end_time - start_time} segundos')
    print(f'Posicao real em ({robot[0],robot[1]})')
    if showField:
        cv.circle(field,(int(particleFilter.mean[0]),int(particleFilter.mean[1])),15,[0,100,200],3)
        cv.imshow("2D Particle filter",cv.flip(field,0))
        cv.waitKey(0)
        cv.destroyAllWindows()

