import numpy as np
import matplotlib.path as mplPath

def getFOV(p0, heading, theta, maxRange, minRange=0):
    p1 = (p0[0]+int(minRange*np.cos(heading+theta/2)),p0[1]+int(minRange*np.sin(heading+theta/2)))
    p2 = (p0[0]+int(minRange*np.cos(heading-theta/2)),p0[1]+int(minRange*np.sin(heading-theta/2)))
    p3 = (p0[0]+int(maxRange*np.cos(heading-theta/2)),p0[1]+int(maxRange*np.sin(heading-theta/2)))
    p4 = (p0[0]+int(maxRange*np.cos(heading+theta/2)),p0[1]+int(maxRange*np.sin(heading+theta/2)))

    

    return [p1,p2,p3,p4]

def getPolygon(vertices):
    polygon = mplPath.Path(np.array(vertices))
    return polygon

def checkPointInPoly(polygon, point):
    return polygon.contains_point(point)