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
            current = start
            explored = nx.Graph(path=[current])
            while explored.nodes() != graph.nodes():
                #If vehicle's tank is empty, we must return to the start
                if v.is_empty():
                    move_to(explored, current, start, **{
                        WEIGHT: get_weight(graph, (current, start)),
                        PHEROMONE: get_pheromone(graph, (current, start)),
                    })
                    current = start
                    v.fill()
                    continue
                nxt = next_node(graph, current, explored)
                move_to(explored, current, nxt, **{
                    WEIGHT: get_weight(graph, (current, nxt)),
                    PHEROMONE: get_pheromone(graph, (current, nxt)),
                })
                v.pour_off_or_empty(order_capacity(graph, current))
                current = nxt
            #When the loop's finished we must manually add an edge
            #from the last explored node to the start
            last = explored.graph['path'][-1]
            move_to(explored, last, start, **{
                WEIGHT: get_weight(graph, (last, start)),
                PHEROMONE: get_pheromone(graph, (last, start)),
            })
            print '-' * 42
            print explored.graph['path']
            print total_cost(explored)
            print '-' * 42
            best_paths.append(explored)

    return sorted(best_paths, key=edges_by_total_cost())[0]


def traverse(graph, vehicle, start, explored=None):
    if explored is None:
        explored = nx.Graph()
    current = start
    while not vehicle.is_empty():
        nxt = next_node(graph, current, explored)
        move_to(explored, current, nxt, **{
            WEIGHT: get_weight(graph, (current, nxt)),
            PHEROMONE: get_pheromone(graph, (current, nxt))
        })
        vehicle.pour_off_or_empty(order_capacity(graph, current))
        current = nxt
    move_to(explored, current, start, **{
        WEIGHT: get_weight(graph, (current, start)),
        PHEROMONE: get_pheromone(graph, (current, start))
    })
    return explored


#TODO: Refactor this non-pure function
def move_to(graph, from_, to_, **kwargs):
    graph.add_edge(
        from_,
        to_,
        **kwargs
    )
    graph.graph['path'].append(to_)


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


def edges_by_total_cost():
    return lambda x: total_cost(x)


def edges_by_tau(graph):
    return lambda t: tau(graph, t[0], t[1]) * eta(graph, t[0], t[1]) ** BETA


def total_cost(graph):
    return sum([t[2]['weight'] for t in graph.edges(data='weight')])


def order_capacity(graph, node):
    return graph.node[node][Order.CAPACITY]


def _get_edge_attr(graph, edge_tuple, attr):
    return graph[edge_tuple[0]][edge_tuple[1]][attr]


def get_weight(graph, edge):
    return _get_edge_attr(graph, edge, WEIGHT)

def get_pheromone(graph, edge):
    return _get_edge_attr(graph, edge, PHEROMONE)