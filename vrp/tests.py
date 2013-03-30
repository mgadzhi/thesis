"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from vrp import ant_colony as ac
from vrp.models import Network, load_orders_map_by_id


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class AntColonyTest(TestCase):

    def test_solve_vrp(self):
        #TODO: Write some tests
        pass