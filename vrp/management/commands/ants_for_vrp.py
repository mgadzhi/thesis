from django.core.management import BaseCommand
from vrp.ant_colony import solve_vrp
from vrp.models import load_orders_map_by_id, Vehicle, Station


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        g = load_orders_map_by_id(1)
        vs = Vehicle.get_all_vehicles_with_full_tanks()
        start = Station.objects.get(id=1)

        print solve_vrp(g, start, vs, iter_num=1)
