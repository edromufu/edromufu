import numpy as np
from numpy.random import randn, uniform
from math import dist

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
    particles[:, 2] %= 2 * np.pi
    return particles

def checkFOV(particle, fov, minRange, maxRange, intersections):
    seen = []
    for intersection in intersections:
        distance = dist((particle[0],particle[1]),intersection[0])
        distX = particle[0] - intersection[0][0]
        distY = particle[1] - intersection[0][1]
        distance = (distX**2 + distY**2)**0.5
        if distX<0: 
            angle = np.arctan(distY/distX)
        elif distX>0:
            angle = np.arctan(distY/distX) - np.pi*np.sign(np.arctan(distY/distX))
        elif distY<0: 
            angle = np.pi/2
        else: 
            angle = -np.pi/2

        angle = (angle + 2*np.pi)%(2*np.pi)
        
        if distance <= maxRange and distance >= minRange:
            '''if angle <= (particle[2]*np.pi/180+fov/2):
            if angle >= (particle[2]*np.pi/180-fov/2):'''
            limLeft = (particle[2]*np.pi/180+fov/2)%(2*np.pi)
            limRight = (particle[2]*np.pi/180-fov/2)%(2*np.pi)
            print(angle)
            print(limLeft)
            print(limRight)
            if limLeft >= limRight and angle <= limLeft and angle >= limRight:
                seen.append(intersection)
            elif limLeft < limRight and (angle <= limLeft or angle >= limRight):
                seen.append(intersection)
            print('---')

    return seen