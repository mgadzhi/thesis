# -*- coding: utf-8 -*-
from django.db import models
from vrp.utils import euclidean_metric
from vrp.errors import VehiclePouringError
import networkx as nx

# Create your models here.


class MapNode(models.Model):

    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        abstract = True

    @classmethod
    def distance(cls, a, b):
        u"""Euclidean metric"""
        return euclidean_metric((a.x, b.x), (a.y, b.y))

    @classmethod
    def get_or_create(cls, x, y):
        try:
            station = cls.objects.get(x=x, y=y)
        except Station.DoesNotExist:
            station = cls()
            station.x = x
            station.y = y
            station.save()
        return station
    

class Depot(MapNode):
    pass


class Station(MapNode):

    def __str__(self):
        return '%s: (%s, %s)' % (self.id, self.x, self.y)


class Edge(models.Model):
    
    # stations = models.ManyToManyField(Station, through='Edges_Stations')
    station1 = models.ForeignKey(Station, related_name="station1")
    station2 = models.ForeignKey(Station, related_name="station2")

    @classmethod
    def get_or_create_edge(cls, station1, station2):
        try:
            if isinstance(station1, int):
                station1 = Station.objects.get(id=station1)
            if isinstance(station2, int):
                station2 = Station.objects.get(id=station2)
        except DoesNotExist:
            return None
        try:
            edge = cls.objects.get(station1=station1, station2=station2)
        except DoesNotExist:
            edge = cls()
            edge.station1 = station1
            edge.station2 = station2
            edge.save()
        return edge

    def nodes(self):
        return self.station1, self.station2

    def __str__(self):
        return '(%s, %s)' % (self.station1_id, self.station2_id)


class Network(models.Model):

    edges = models.ManyToManyField(Edge)
    start = models.ForeignKey(Station)

    _graph = None

    def _generate_graph(self):
        graph = nx.Graph()
        for edge in self.edges.all():
            node1, node2 = edge.nodes()
            graph.add_edge(
                node1,
                node2,
                weight=Station.distance(node1, node2)
            )
        graph.node[self.start]['start'] = True
        return graph

    def get_graph(self):
        if self._graph is None:
            self._graph = self._generate_graph()
        return self._graph

    def __str__(self):
        return 'id = %s' % self.id


class Vehicle(models.Model):

    name = models.CharField(max_length=64)
    max_capacity = models.IntegerField()

    capacity = 0

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, value):
        self.capacity = value

    def is_full(self):
        return self.capacity == self.max_capacity

    def is_empty(self):
        return self.capacity == 0

    @classmethod
    def get_vehicle_with_full_tank(cls, id_):
        v = cls.objects.get(id=id_)
        if v:
            v.set_capacity(v.max_capacity)
        return v

    @classmethod
    def get_all_vehicles_with_full_tanks(cls):
        vs = cls.objects.all()
        for v in vs:
            v.set_capacity(v.max_capacity)
        return vs

    def _pour_off(self, d):
        if d > self.get_capacity():
            raise VehiclePouringError()
        else:
            self.capacity -= d

    def empty(self):
        c = self.get_capacity()
        self.set_capacity(0)
        return c

    def pour_off_or_empty(self, desirable):
        try:
            self._pour_off(desirable)
            return desirable
        except VehiclePouringError:
            return self.empty()

    def _pour_in(self, d):
        if d > self.max_capacity - self.get_capacity():
            raise VehiclePouringError()
        else:
            self.capacity += d

    def fill(self):
        d = self.max_capacity - self.get_capacity()
        self.set_capacity(self.max_capacity)
        return d


class Order(models.Model):

    station = models.ForeignKey(Station)
    status = models.CharField(max_length=20)
    creation_date = models.DateTimeField()
    capacity = models.IntegerField()

    STATUS_CREATED = 'created'
    STATUS_EXECUTING = 'executing'
    STATUS_FINISHED = 'finished'

    CAPACITY = 'capacity'

    @classmethod
    def get_by_status(cls, status):
        return cls.objects.filter(status=status)

    @classmethod
    def get_created(cls):
        return cls.get_by_status(cls.STATUS_CREATED)

    @classmethod
    def get_executing(cls):
        return cls.get_by_status(cls.STATUS_EXECUTING)

    @classmethod
    def get_finished(cls):
        return cls.get_by_status(cls.STATUS_FINISHED)


def load_orders_map_by_id(id_):
    map = Network.objects.get(id=id_).get_graph()
    orders = Order.get_created()
    for order in orders:
        if map.has_node(order.station):
            map.node[order.station][Order.CAPACITY] = order.capacity
    return map