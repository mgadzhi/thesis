# -*- coding: utf-8 -*-
from vrp.new_models import Station, Depot


def parse_vrp_instance(filename):
    instance = {}
    depot = None
    with open(filename, 'r') as f:
        try:
            for i_ in xrange(6):
                k, v = map(lambda x: x.strip(), next(f).split(':', 1))
                instance[k] = v
            assert next(f).strip() == 'NODE_COORD_SECTION'
            instance['nodes'] = []
            n = int(instance['NAME'].split('-')[1][1:])  #Узнаем n - количество вершин.
            #Parse depot - node with id 0.
            id_, x, y = (int(s) for s in next(f).split())
            depot = Depot(id_, x, y)
            #Parse stations
            for i_ in xrange(n - 1):
                id_, x, y = (int(s) for s in next(f).split())
                instance['nodes'].append(Station(id_, x, y))
            assert next(f).strip() == 'DEMAND_SECTION'
            #We don't need demand for depot
            assert int(next(f).split()[1]) == 0
            #Parse demands
            for i in xrange(n - 1):
                demand = int(next(f).split()[1])
                instance['nodes'][i].demand = demand
        except Exception, e:
            print e
            return None
    return instance, depot
