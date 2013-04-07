# -*- coding: utf-8 -*-
from vrp.models import Station


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
                instance['nodes'].append(Station.get_or_create(x, y))
            assert next(f).strip() == 'DEMAND_SECTION'
            for i in xrange(n):
                demand = next(f).split()[1]
                instance['nodes'][i].set_demand(demand)
        except Exception, e:
            print e
            return None
    return instance
