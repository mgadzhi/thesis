# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.core.management import BaseCommand
from vrp.ant_colony import solve_vrp, traverse, init_with_pheromones, total_cost
from vrp.complete_graph import CompleteGraph
from vrp.models import load_orders_map_by_id, Vehicle, Station, Depot, MapNode
from vrp.vrp_instances import parser


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        inst_file = 'A-n32-k5.vrp'
        instance = parser.parse_vrp_instance(
            os.path.join(settings.VRP_INSTANCES_DIR, inst_file)
        )
        depot = Depot.objects.get(id=1)
        graph = CompleteGraph.create_clients_map(
            instance['nodes'],
            depot,
            dist=MapNode.distance,
        )
        graph = init_with_pheromones(graph)
        vehicles = Vehicle.get_all_vehicles_with_full_tanks()
        solution = solve_vrp(graph, depot, vehicles)
        for k, v in solution.graph['paths'].iteritems():
            print k.id, v
        print total_cost(solution)
        print 'Ok'