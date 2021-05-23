# Copyright (c) 2021 Apple Inc. All rights reserved
""" TestVehicleImpl.py
"""
import unittest

from src.location.Location import Location
from src.vehicle.impl.VehicleImpl import VehicleImpl


class TestVehicleImpl(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = VehicleImpl(Location(1.23, 4.56, address="Address"), "ID_1", max_num_locations=2)

    def test_initialization(self):
        self.assertEqual(self.vehicle.vehicle_id, "ID_1")
        self.assertEqual(self.vehicle.address, "Address")
        self.assertEqual(self.vehicle.latest_location, Location(1.23, 4.56, address="Address"))
        self.assertListEqual(self.vehicle.locations, [Location(1.23, 4.56, address="Address")])

    def test_update_latest_location(self):
        self.vehicle.latest_location = Location(4.56, 7.89, address="Address_2")
        self.assertEqual(self.vehicle.latest_location, Location(4.56, 7.89, address="Address_2"))
        self.assertEqual(self.vehicle.locations, [
            Location(1.23, 4.56, address="Address"),
            Location(4.56, 7.89, address="Address_2")
        ])
        self.vehicle.latest_location = Location(7.89, 1.23, address="Address_3")
        # Drop old locations
        self.assertListEqual(
            self.vehicle.locations,
            [
                Location(4.56, 7.89, address="Address_2"),
                Location(7.89, 1.23, address="Address_3")
            ]
        )


if __name__ == '__main__':
    unittest.main()
