import math

__author__ = 'gadzhi'


PHEROMONE = 'pheromone_level'
WEIGHT = 'weight'


def euclidean_metric(a, b):
    u"""a and b are tuples (x, y)"""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def another(couple, current):
    return couple[0] if current == couple[1] else couple[1]
