"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from vrp.ant_colony import AntColony
from vrp.models import Network


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class AntColonyTest(TestCase):
    def test_traverse(self):
        g = Network.objects.get(id=1).get_graph()
        g = AntColony.init_with_pheromones(g)
        path = AntColony.traverse(g)
        print path
        self.assertTrue(path.number_of_nodes() == g.number_of_nodes())
        self.assertTrue(path.number_of_edges() == g.number_of_nodes() - 1)
