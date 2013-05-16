# -*- coding: utf-8 -*-
from celery.task import task


# The simplest task. For testing purposes
from vrp.ant_colony import solve_vrp, init_with_pheromones
from vrp.complete_graph import CompleteGraph
from vrp.models import Order, Depot, Station, Vehicle


@task()
def add(x, y):
    return x + y


def execute_orders_vrp():
    orders = Order.objects.filter(status=Order.STATUS_CREATED)
    depot = Depot.objects.get(pk=1)  # Пока можем считать, что депо только 1.
    stations = Station.objects.filter(id__in=[o.station_id for o in orders])
    vehicles = Vehicle.objects.all()
    graph = CompleteGraph.create_clients_map(
        stations,
        depot,
        dist=Station.distance
    )
    graph = init_with_pheromones(graph)
    return graph
    # return solve_vrp(graph, depot, vehicles, iter_num=1000)


@task()
def execute_orders_task():
    return execute_orders_vrp()