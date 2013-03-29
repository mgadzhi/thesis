import networkx as nx
import time
from thesis.utils import another


class Solver(object):
    WEIGHT = 'weight'

    @classmethod
    def greedy(cls, graph, start):
        u"""
            Suggests that graph is complete (Contains all possible edges)
        """
        current_node = start
        path = nx.Graph()
        path.add_node(current_node)
        cost = 0

        while path.number_of_nodes() < graph.number_of_nodes():
            edges = sorted(
                [t for t in graph.edges(data=cls.WEIGHT)
                    if (t[0] == current_node or t[1] == current_node)],
                key=lambda t: t[2][cls.WEIGHT]
            )
            try:
                best_choice = cls.choice(
                    edges,
                    start,
                    path,
                    current_node
                )
            except NoGreedySolution:
                return cls._no_solution()
            except FinishGreedySearch, e:
                best_choice = e.last_edge
            print best_choice
            path.add_edge(
                best_choice[0],
                best_choice[1],
                weight=best_choice[2][cls.WEIGHT]
            )
            cost += best_choice[2][cls.WEIGHT]
            current_node = best_choice[0] if best_choice[0] != current_node\
                else best_choice[1]
        if not graph.has_edge(current_node, start):
            return cls._no_solution()
        else:
            path.add_edge(
                current_node,
                start,
                weight=graph[current_node][start][cls.WEIGHT])
            cost += graph[current_node][start][cls.WEIGHT]
        return {
            'path': path,
            'cost': cost
        }

    @classmethod
    def _no_solution(cls):
        return {
            'path': nx.Graph(),
            'cost': 0
        }

    @classmethod
    def choice(cls, edges, start_node, path, current_node):
        for e in edges:
            neighbour = another(e, current_node)
            if not path.has_node(neighbour):
                return e
        raise NoGreedySolution()

    @classmethod
    def ants_colony(cls, graph, start, n=1000):
        u"""
            n - number of iterations
        """
        for i_ in range(n):
            pass #simulation here

class NoGreedySolution(Exception):
    pass


class FinishGreedySearch(Exception):
    def __init__(self, last_edge):
        self.last_edge = last_edge