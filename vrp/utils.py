# -*- coding: utf-8 -*-

import math

PHEROMONE = 'pheromone_level'
WEIGHT = 'weight'


def euclidean_metric(a, b):
    u"""a and b are tuples (x, y)"""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def another(couple, current):
    return couple[0] if current == couple[1] else couple[1]


def parse_vrp_instance(filename):
    instance = {}
    with open(filename, 'r') as f:
        try:
            for i_ in xrange(6):
                k, v = map(lambda x: x.strip(), next(f).split(':', 1))
                instance[k] = v
            assert next(f).strip() == 'NODE_COORD_SECTION'
            instance['nodes'] = []
            n = int(instance['NAME'].split('-')[1][1:])  #Узнаем n - количество вершин.
            for i_ in xrange(n):
                id_, x, y = next(f).split()
                instance['nodes'].append({
                    'id': id_,
                    'x': x,
                    'y': y,
                })
            assert next(f).strip() == 'DEMAND_SECTION'
            for i in xrange(n):
                demand = next(f).split()[1]
                instance['nodes'][i]['demand'] = demand
        except Exception, e:
            print e
            return None
        return instance
