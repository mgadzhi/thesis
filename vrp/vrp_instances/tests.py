# -*- coding: utf-8 -*-
from django.conf import settings
from django.test import TestCase
import os
from vrp.models import Station
from vrp.vrp_instances.parser import parse_vrp_instance


class ParserTestCase(TestCase):

    def test_parse(self):
        inst_file = os.path.join(settings.VRP_INSTANCES_DIR, 'A-n32-k5.vrp')
        result = parse_vrp_instance(inst_file)

        self.assertIsNotNone(result)
        self.assertIsNotNone(result['nodes'])
        self.assertTrue(all(
            [isinstance(x, Station) for x in result['nodes']]
        ))