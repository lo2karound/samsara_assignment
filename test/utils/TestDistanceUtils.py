# Copyright (c) 2021 Apple Inc. All rights reserved
""" TestDistanceUtils.py
"""
import math
import unittest

from src.location.Location import Location
from src.utils.DistanceUtils import DistanceUtils


class TestDistanceUtils(unittest.TestCase):
    def test_haversine_distance_km(self):
        self.assertEqual(DistanceUtils.haversine_distance_km(Location(1.23, 3.45), Location(1.23, 3.45)), 0)
        self.assertTrue(
            math.isclose(
                DistanceUtils.haversine_distance_km(Location(1.23, 3.45), Location(2.23, 3.45)),
                111.194926,
                abs_tol=1e-5
            )
        )


if __name__ == '__main__':
    unittest.main()
