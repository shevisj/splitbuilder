import math
from pprint import pprint

def calc_points(r=19800, numPoints=10):
    points = []
    for index in range(numPoints):
        points.append([round(r*math.cos((index*2*math.pi)/numPoints)),round(r*math.sin((index*2*math.pi)/numPoints))])
    return points

pprint(calc_points())