# -*- coding: utf-8 -*-
from vrp.utils import euclidean_metric


class NodeIdRegistry(object):

    def __init__(self):
        self._current_max_id = 0
        self._registry = []

    def add(self, new_id):
        if not new_id in self._registry:
            self._registry.append(new_id)
            self._registry.sort()
            self._current_max_id = self._registry[-1]

    def delete(self, id):
        try:
            self._registry.remove(id)
            self._current_max_id = self._registry[-1]
        except ValueError:
            pass
        except IndexError:
            self._current_max_id = 0

    def contains(self, id):
        return id in self._registry

    def get_next_id(self):
        return self._current_max_id + 1


class GraphNode(object):

    _REGISTRY = NodeIdRegistry()

    def __init__(self, x, y, id_=None, demand=0):
        if self._REGISTRY.contains(id_):
            raise ValueError('Object with id {} already exists'.format(id_))
        if id_ is None:
            id_ = self._REGISTRY.get_next_id()
        self._REGISTRY.add(id_)
        self._id = id_
        self._x = x
        self._y = y
        self._demand = demand

    def __del__(self):
        self._REGISTRY.delete(self.id)

    @property
    def id(self):
        return self._id

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, value):
        self._demand = value

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @classmethod
    def distance(cls, a, b):
        u"""Euclidean metric"""
        return euclidean_metric((a.x, b.x), (a.y, b.y))
