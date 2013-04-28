# -*- coding: utf-8 -*-
from vrp.errors import NotEnoughVehiclesError

from vrp.utils import another
from vrp.models import Order

import random
import networkx as nx


PHEROMONE = 'pheromone_level'
WEIGHT = 'weight'
ALPHA = 0.8
BETA = 0.8
Q0 = 0.9
TAU0 = 1.0 / 784


#For all the functions: 'explored' is the nx.Graph object
#I'll keep an order in which a graph is traversed as a graph attribute path.


def solve_vrp(graph, start, ants, iter_num=1000):
    graph = init_with_pheromones(graph)
    best_solution = graph
    for i_ in xrange(iter_num):
        explored = nx.Graph(paths={})
        for ant in ants:
            explored.add_node(start)
            explored.graph['paths'][ant] = [start]
            ant.fill()
            explored = traverse(graph, ant, start, explored)
            if explored.number_of_nodes() == graph.number_of_nodes():
                best_solution = better_solution(best_solution, explored)
                # print total_cost(best_solution)
                break
        if explored.number_of_nodes() != graph.number_of_nodes():
            raise NotEnoughVehiclesError()
        for edge in graph.edges():
            local_pheromone_update(graph, edge)
        # print [round(t[2][PHEROMONE], 5) for t in graph.edges(data=PHEROMONE)]
        best_length = total_cost(best_solution)
        for edge in best_solution.edges():
            global_pheromone_update(graph, edge, best_length)

    return best_solution


def traverse(graph, ant, start, explored=None):
    if explored is None:
        explored = nx.Graph(paths={ant: [start]})
        explored.add_node(start)
    current = start
    while not ant.is_empty() and explored.number_of_nodes() != graph.number_of_nodes():
        nxt = next_node(graph, current, explored)
        explored.add_edge(current, nxt, weight=get_weight(graph, (current, nxt)))
        explored.graph['paths'][ant].append(nxt)
        ant.pour_off_or_empty(nxt.demand)
        print 'Ant: {}, capacity: {}'.format(ant, ant.capacity)
        current = nxt
    explored.add_edge(current, start, weight=get_weight(graph, (current, start)))
    explored.graph['paths'][ant].append(start)
    return explored


def next_node(graph, current, explored):
    q = random.random()
    if q < Q0:
        edges = sorted(
            [e for e in graph.edges(current)
                if another(e, current) not in explored],
            key=edges_by_tau(graph)
        )
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
    neighbs = [n for n in graph.neighbors(current) if n not in explored.nodes()]
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
    graph[a][b][PHEROMONE] = (1 - ALPHA) * old + ALPHA * TAU0


def global_pheromone_update(graph, edge, length):
    a, b = edge
    old = graph[a][b][PHEROMONE]
    graph[a][b][PHEROMONE] = (1 - ALPHA) * old + (ALPHA / length)


def tau(graph, r, s):
    return graph[r][s][PHEROMONE]


def eta(graph, r, s):
    u"""
        1/d. d is Euclidean distance.
    """
    return 1.0 / (graph[r][s]['weight'])


def edges_by_total_cost():
    return lambda x: total_cost(x)


def edges_by_tau(graph):
    return lambda t: tau(graph, t[0], t[1]) * (eta(graph, t[0], t[1]) ** BETA)


def total_cost(graph):
    return sum([t[2]['weight'] for t in graph.edges(data='weight')])

def _get_edge_attr(graph, edge_tuple, attr):
    return graph[edge_tuple[0]][edge_tuple[1]][attr]


def get_weight(graph, edge):
    return _get_edge_attr(graph, edge, WEIGHT)


def get_pheromone(graph, edge):
    return _get_edge_attr(graph, edge, PHEROMONE)


def better_solution(solution1, solution2):
    return solution1 if total_cost(solution1) < total_cost(solution2) else solution2