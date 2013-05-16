# -*- coding: utf-8 -*-
import itertools

import os
from django.conf import settings
from django.core.management import BaseCommand
from vrp.ant_colony import solve_vrp, init_with_pheromones, total_cost
from vrp.complete_graph import CompleteGraph
from vrp.vrp_instances.models import GraphNode, Ant
from vrp.vrp_instances import parser


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        inst_file = 'A-n32-k5.vrp'
        instance, depot = parser.parse_vrp_instance(
            os.path.join(settings.VRP_INSTANCES_DIR, inst_file)
        )
        graph = CompleteGraph.create_clients_map(
            instance['nodes'],
            depot,
            dist=GraphNode.distance,
        )
        graph = init_with_pheromones(graph)
        ants = [
            Ant(1, 100),
            Ant(2, 100),
            Ant(3, 100),
            Ant(4, 100),
            Ant(5, 100),
        ]
        solution = solve_vrp(graph, depot, ants, iter_num=10000)
        for k, v in solution.graph['paths'].iteritems():
            print k.id, v
        print total_cost(solution)