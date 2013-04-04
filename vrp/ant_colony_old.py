import random
from vrp import utils

__author__ = 'gadzhi'

import networkx as nx


class AntColony(object):
    PHEROMONE = 'pheromone_level'
    WEIGHT = 'weight'
    ALPHA = 0.5
    BETA = 0.5
    Q0 = 0.5
    TAU0 = 1.0 / 400

    @classmethod
    def solve_tsp(cls, graph, start, iter_num=10, ants_num=10):
        graph = cls.init_with_pheromones(graph)

        best_paths = []
        for i_ in range(iter_num):
            ants_paths = []
            for ant_ in xrange(ants_num):
                ants_paths.append(cls.traverse(graph, start))
            best_paths.append(sorted(ants_paths, key=lambda x: sum([t[2]['weight'] for t in x.edges(data='weight')]))[0])
        return sorted(best_paths, key=utils.order_key())[0]

    @classmethod
    def solve_vrp(cls, graph, start, vehicles, iter_num=10):
        graph = cls.init_with_pheromones(graph)
        best_paths = []

        #TODO: WRITE THE CODE, BLJAD!
        for i_ in xrange(iter_num):
            for v in vehicles:
                path = []
                current = start
                while set(path) != set(graph.nodes()):
                    while not v.is_empty():
                        next_node = cls.next_node(graph, current,)

        return sorted(best_paths, key=cls.order_key())[0]

    @classmethod
    def traverse(cls, graph, start):
        path = nx.Graph()
        current_node = start
        path.add_node(current_node)
        while path.number_of_nodes() != graph.number_of_nodes():
            next_node = cls.next_node(graph, start, current_node, path)
            path.add_edge(
                current_node,
                next_node,
                weight=graph[current_node][next_node]['weight'],
                pheromone_level=graph[current_node][next_node][cls.PHEROMONE]
            )
            current_node = next_node
        path.add_edge(
            start,
            current_node,
            weight=graph[start][current_node]['weight'],
            pheromone_level=graph[start][current_node][cls.PHEROMONE],
        )
        return path

    @classmethod
    def next_node(cls, graph, current_node, explored):
        q = random.random()
        if q < cls.Q0:
            edges = sorted(
                [t for t in graph.edges(data=(cls.PHEROMONE, cls.WEIGHT))
                    if (t[0] == current_node or t[1] == current_node)
                    and utils.another((t[0], t[1]), current_node) not in explored.nodes()],
                key=lambda t: cls.tau(graph, t[0], t[1]) * cls.eta(graph, t[0], t[1]) ** cls.BETA
            )
            return utils.another(edges[-1], current_node)
        else:
            return cls.random_neighbour(graph, current_node, explored)

    @classmethod
    def random_neighbour(cls, graph, current_node, explored=None):
        if explored is None:
            explored = nx.Graph()
            explored.add_node(current_node)
        distr = cls.neighb_distribution(graph, current_node, explored)
        r = random.random()
        for k, v in distr.iteritems():
            if r < v:
                return k

    @classmethod
    def neighb_distribution(cls, graph, current, explored=None):
        if explored is None:
            explored = nx.Graph()
            explored.add_node(current)
        neighbs = [v for v in utils.neighb_nodes(graph, current) if not explored.has_node(v)]
        total = 0
        distr = {}
        for node in neighbs:
            p = cls.step_probability(graph, current, node, explored)
            total += p
            distr[node] = total
        return distr

    @classmethod
    def step_probability(cls, graph, r, s, explored):
        if not explored.has_edge(r, s):
            r_neighbs = [v for v in utils.neighb_nodes(graph, r) if not explored.has_node(v)]
            return (cls.tau(graph, r, s) * cls.eta(graph, r, s) ** cls.BETA) / \
                sum([cls.tau(graph, r, x) * cls.eta(graph, r, x) ** cls.BETA for x in r_neighbs])
        else:
            return 0


    @classmethod
    def init_with_pheromones(cls, graph):
        graph = nx.Graph(graph)
        for edge in graph.edges():
            a, b = edge
            graph[a][b][cls.PHEROMONE] = cls.TAU0
        return graph

    @classmethod
    def local_pheromone_update(cls, graph, edge):
        a, b = edge
        old = graph[a][b][cls.PHEROMONE]
        graph[a][b][cls.PHEROMONE] = (1 - cls.ALPHA) * old + cls.TAU0

    @classmethod
    def tau(cls, graph, r, s):
        return graph[r][s][cls.PHEROMONE]

    @classmethod
    def eta(cls, graph, r, s):
        u"""
            1/d. d is Euclidean distance.
        """
        return 1.0 / (graph[r][s]['weight'])

    @classmethod
    def order_key(cls):
        return lambda x: sum([t[2]['weight'] for t in x.edges(data='weight')])