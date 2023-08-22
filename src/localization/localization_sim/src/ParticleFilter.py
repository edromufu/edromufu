import numpy as np
from filterpy.monte_carlo import systematic_resample
from numpy.random import randn, uniform
from math import dist
import scipy.stats

def create_uniform_particles(xRange, yRange, headingRange, N):
    particles = np.empty((N, 3))
    particles[:, 0] = uniform(xRange[0], xRange[1], size=N)
    particles[:, 1] = uniform(yRange[0], yRange[1], size=N)
    particles[:, 2] = uniform(headingRange[0], headingRange[1], size=N)
    particles[:, 2] %= 360
    return particles.astype(int)

def create_gaussian_particles(mean, standardDeviation, N):
    particles = np.empty((N, 3))
    particles[:, 0] = mean[0] + (randn(N) * standardDeviation[0])
    particles[:, 1] = mean[1] + (randn(N) * standardDeviation[1])
    particles[:, 2] = mean[2] + (randn(N) * standardDeviation[2])
    particles[:, 2] %= 360
    return particles.astype(int)

def predict(particles, passo, erro):
    N = len(particles)
    particles[:, 2] += (passo[1] + (randn(N) * erro[1])).astype(int)
    particles[:, 2] %= 360

    dist = passo[0] + (randn(N) * erro[0])
    particles[:, 0] += (np.cos(particles[:, 2]) * dist).astype(int)
    particles[:, 1] += (np.sin(particles[:, 2]) * dist).astype(int)

    return particles

def checkFOV(particle, fov, minRange, maxRange, intersections):
    seen = []
    for intersection in intersections:
        distance = dist((particle[0],particle[1]),intersection[0])
        distX = particle[0] - intersection[0][0]
        distY = particle[1] - intersection[0][1]
        distance = (distX**2 + distY**2)**0.5
        
        if distance <= maxRange and distance >= minRange:
            '''if angle <= (particle[2]*np.pi/180+fov/2):
            if angle >= (particle[2]*np.pi/180-fov/2):'''

            if distX == 0 and distY<0:
                angle = np.pi/2
            elif distX == 0 and distY>0:
                angle = -np.pi/2
            elif distY == 0 and distX<0:
                angle = 0
            elif distY == 0 and distX>0:
                angle = np.pi
            elif distX<0:
                angle = np.arctan(distY/distX)
            elif distX>0:
                angle = np.arctan(distY/distX) - np.pi*np.sign(np.arctan(distY/distX))
            else: 
                pass

            angle = (angle + 2*np.pi)%(2*np.pi)

            limLeft = (particle[2]*np.pi/180+fov/2)%(2*np.pi)
            limRight = (particle[2]*np.pi/180-fov/2)%(2*np.pi)
            if limLeft >= limRight and angle <= limLeft and angle >= limRight:
                seen.append(intersection)
            elif limLeft < limRight and (angle <= limLeft or angle >= limRight):
                seen.append(intersection)

    return seen

def testParticles(particles, fov, minRange, maxRange, intersections, answer, weights = None):
    if weights == None: 
        weights = [1]*len(particles)

    for i, particle in enumerate(particles):
        particleAnswer = []
        particleAnswer = checkFOV(particle, fov, minRange, maxRange, intersections)
        
        if len(answer) != 0:
            checking = compareIntersectionLists(answer,particleAnswer)/len(answer)
        elif len(particleAnswer) != 0:
            checking = 1/(1+len(particleAnswer))
        else:
            checking = 1
        weights[i] *= checking


    weights = np.divide(weights,sum(weights))
    return weights

def resample_from_index(particles, weights):
    N = len(particles)
    indexes = systematic_resample(weights)

    # resample according to indexes
    particles[:] = particles[indexes]
    weights.fill(1.0 / N)

    return particles,weights



def neff(weights):
    return 1. / np.sum(np.square(weights))

def moveRobot(robot, passo):
    robot[2] += passo[1]
    robot[0] += int(passo[0]*np.cos(robot[2]*np.pi/180))
    robot[1] += int(passo[0]*np.sin(robot[2]*np.pi/180))
    return robot


def estimate(particles, weights):
    """returns mean and variance of the weighted particles"""

    pos = particles[:, 0:2]
    mean = np.average(pos, weights=weights, axis=0).astype(int)
    var  = np.average((pos - mean)**2, weights=weights, axis=0)
    return mean, var

def compareIntersectionLists(list1, list2):
    result = 0
    for intersection1 in list1:
        for intersection2 in list2:
            if intersection1[2] == intersection2[2]:
                result += 1
                list2.remove(intersection2)
    return result