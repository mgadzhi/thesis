# -*- coding: utf-8 -*-
from vrp.utils import euclidean_metric


class GraphNodeMixin(object):

    def __init__(self, id_, x, y, demand=0):
        self._id = id_
        self._x = x,
        self._y = y,
        self._demand = demand

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