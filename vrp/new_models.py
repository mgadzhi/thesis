# -*- coding: utf-8 -*-
from vrp.solver_models_mixins import GraphNode
from vrp.utils import euclidean_metric


class Ant(object):

    def __init__(self, id_, max_capacity):
        self._id = id_
        self.max_capacity = max_capacity
        self._capacity = max_capacity

    @property
    def id(self):
        return self._id

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

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

    def fill(self):
        self.capacity = self.max_capacity

    def __unicode__(self):
        return u'Ant<{}>'.format(self.id)

    def __repr__(self):
        return unicode(self)


class Depot(GraphNode):

    def __init__(self, x, y, id_=None, demand=0):
        assert demand == 0, "Depot's demand must be 0"
        super(Depot, self).__init__(x, y, id_=id_)

    def __unicode__(self):
        return u'Depot<{}>'.format(self.id)

    def __str__(self):
        return 'Depot<{}>'.format(self.id)

    def __repr__(self):
        return unicode(self)


class Station(GraphNode):

    def __unicode__(self):
        return u'S<{},{}>'.format(self.id, self.demand)

    def __str__(self):
        return 'S<{}>'.format(self.id)

    def __repr__(self):
        return unicode(self)