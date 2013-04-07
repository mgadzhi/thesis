# -*- coding: utf-8 -*-
import itertools

import networkx as nx
from vrp.models import Station


class CompleteGraph(nx.Graph):

    @classmethod
    def create_complete_graph(cls, nodes):
        graph = cls()
        graph.add_edges_from(itertools.permutations(nodes, 2))
        return graph

    def add_node_and_save_completeness(self, new_node):
        for node in self.nodes():
            self.add_edge(node, new_node)

    @classmethod
    def create_clients_map(cls, clients, depot, dist=None):
        if dist is None:
            dist = lambda x, y: 0
        graph = cls()
        for c in clients:
            graph.add_node(c, demand=c.get_demand())
        graph.add_node(depot, demand=0)
        for x, y in itertools.permutations(graph.nodes(), 2):
            graph.add_edge(
                x,
                y,
                weight=dist(x, y)
            )
        return graph
