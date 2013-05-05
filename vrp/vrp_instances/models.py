# -*- coding: utf-8 -*-
from vrp.utils import euclidean_metric


class GraphNode(object):

    def __init__(self, id, x, y, demand=0):
        self._id = id
        self._x = x
        self._y = y
        self._demand = demand

    @property
    def id(self):
        return self._id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, value):
        self._demand = value

    @classmethod
    def distance(cls, a, b):
        u"""Euclidean metric"""
        return euclidean_metric((a.x, b.x), (a.y, b.y))


class Station(GraphNode):
    def __unicode__(self):
        return u'S<{},{}>'.format(self.id, self.demand)

    def __repr__(self):
        return unicode(self)


class Depot(GraphNode):

    def __init__(self, id, x, y, demand=0):
        if demand != 0:
            raise ValueError("Depot's demand must equal 0")
        super(Depot, self).__init__(id, x, y, demand)

    def __unicode__(self):
        return u'Depot<{}>'.format(self.id)

    def __repr__(self):
        return unicode(self)


class Ant(object):

    def __init__(self, id, max_capacity):
        self._id = id
        self._max_capacity = max_capacity
        self._capacity = 0

    @property
    def id(self):
        return self._id

    @property
    def capacity(self):
        return self._capacity

    @property
    def max_capacity(self):
        return self._max_capacity

    def fill(self):
        self._capacity = self._max_capacity

    def is_empty(self):
        return self.capacity == 0

    def pour_off(self, d):
        if d > self._capacity:
            raise ValueError('Not enough capacity')
        else:
            self._capacity -= d

    def pour_off_or_empty(self, d):
        try:
            self.pour_off(d)
        except ValueError:
            self.pour_off(self.capacity)

    def __unicode__(self):
        return u'Ant<{}>'.format(self.id)

    def __repr__(self):
        return unicode(self)