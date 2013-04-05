# -*- coding: utf-8 -*-

import networkx as nx
import itertools
from vrp.models import Station


def complete_map(nodes):
    cg = nx.Graph()
    for node1, node2 in itertools.permutations(nodes, 2):
        cg.add_edge(
            node1,
            node2,
            weight=Station.distance(node1, node2)
        )
    return cg


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


def clients_map_from_instance(filename):
    nodes = parse_vrp_instance(filename)['nodes']
    return complete_map([Station.get_or_create(node['x'], node['y']) for node in nodes])