import logging
from thesis.utils import another

import networkx as nx
import random
from vrp.models import Order


PHEROMONE = 'pheromone_level'
WEIGHT = 'weight'
ALPHA = 0.5
BETA = 0.5
Q0 = 0.5
TAU0 = 1.0 / 400


#For all the functions: 'explored' is the nx.Graph object
#I'll keep an order in which a graph is traversed as a graph attribute path.


def solve_vrp(graph, start, vehicles, iter_num=10):
    graph = init_with_pheromones(graph)
    best_paths = []

    for i_ in xrange(iter_num):
        for v in vehicles:
            explored = nx.Graph(path=[])
            current = start
            while explored.nodes() != graph.nodes():
                print current
                if v.is_empty():
                    current = start
                    v.fill()
                    continue
                nxt = next_node(graph, current, explored)
                explored.add_node(nxt)
                explored.graph['path'].append(nxt)
                v.pour_off_or_empty(order_capacity(graph, current))
                current = nxt
            return explored

    return sorted(best_paths, key=edges_by_weight())[0]


def next_node(graph, current, explored):
    q = random.random()
    if q < Q0:
        edges = sorted(
            [e for e in graph.edges(current)
                if another(e, current) not in explored],
            key=edges_by_tau(graph)
        )
        # print explored.edges()
        # print current
        # print edges
        return another(edges[-1], current)
    else:
        return random_neighbour(graph, current, explored)


def random_neighbour(graph, current, explored):
    distr = neighb_distribution(graph, current, explored)
    r = random.random()
    for k, v in distr.iteritems():
        if r < v:
            return k


def neighb_distribution(graph, current, explored):
    neighbs = [n for n in graph.neighbors(current) if n not in explored]
    total = 0
    distr = {}
    for node in neighbs:
        p = step_probability(graph, current, node, explored)
        total += p
        distr[node] = total
    return distr


def step_probability(graph, r, s, explored):
    if not explored.has_edge(r, s):
        r_neighbs = [n for n in graph.neighbors(r) if n not in explored]
        return (tau(graph, r, s) * eta(graph, r, s) ** BETA) / \
            sum([tau(graph, r, x) * eta(graph, r, x) ** BETA for x in r_neighbs])
    else:
        return 0


def init_with_pheromones(graph):
    graph = nx.Graph(graph)
    for edge in graph.edges():
        a, b = edge
        graph[a][b][PHEROMONE] = TAU0
    return graph


def local_pheromone_update(graph, edge):
    a, b = edge
    old = graph[a][b][PHEROMONE]
    graph[a][b][PHEROMONE] = (1 - ALPHA) * old + TAU0


def tau(graph, r, s):
    return graph[r][s][PHEROMONE]


def eta(graph, r, s):
    u"""
        1/d. d is Euclidean distance.
    """
    return 1.0 / (graph[r][s]['weight'])


def edges_by_weight():
    return lambda x: sum([t[2]['weight'] for t in x.edges(data='weight')])


def edges_by_tau(graph):
    return lambda t: tau(graph, t[0], t[1]) * eta(graph, t[0], t[1]) ** BETA


def order_capacity(graph, node):
    return graph.node[node][Order.CAPACITY]