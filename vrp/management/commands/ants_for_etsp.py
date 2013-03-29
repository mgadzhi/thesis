from django.core.management.base import BaseCommand
from vrp.models import Network, Station
from vrp.tsp import Solver
from vrp.ant_colony import AntColony
import networkx as nx


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # network_id = 1
        # start = Station.objects.get(id=1)
        # network = Network.objects.get(id=1)
        # g = network.get_graph()
        # # greedy_solution = Solver.greedy(g, start)
        #
        # solution = AntColony.solve_tsp(g, start)
        # cost = sum([t[2]['weight'] for t in solution.edges(data='weight')])
        # print cost
        print 'Too old'
