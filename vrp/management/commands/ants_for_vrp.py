# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.core.management import BaseCommand
from vrp.ant_colony import solve_vrp, traverse, init_with_pheromones
from vrp.models import load_orders_map_by_id, Vehicle, Station, Depot
from vrp.vrp_instances import parser


class Command(BaseCommand):
    #TODO: Как-то переделать работу с картами (графами)

    def handle(self, *args, **kwargs):
        inst = 'A-n32-k5.vrp'
        g = parser.clients_map_from_instance(
            os.path.join(settings.VRP_INSTANCES_DIR, inst)
        )
        vs = Vehicle.get_all_vehicles_with_full_tanks()
        start = Depot.objects.get(id=1)
        g.add_node(start)
        for n in g.nodes():
            if n != start:
                g.add_edge(n, start, weight=Station.distance(n, start))
        g = init_with_pheromones(g)

        # print solve_vrp(g, start, vs, iter_num=1)
        print traverse(g, vs[0], start).nodes()
