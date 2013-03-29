__author__ = 'gadzhi'


def edges_by_weight():
    return lambda x: sum([t[2]['weight'] for t in x.edges(data='weight')])


def edges_by_tau():
    return lambda t: tau(graph, t[0], t[1]) * eta(graph, t[0], t[1]) ** BETA