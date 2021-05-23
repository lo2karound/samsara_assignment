# Copyright (c) 2021 Apple Inc. All rights reserved
""" DictFleet.py
"""
from typing import List, Dict

from src.fleet.Fleet import Fleet
from src.location.Location import Location
from src.utils.DistanceUtils import DistanceUtils
from src.vehicle.Vehicle import Vehicle, VehicleId


class DictFleet(Fleet):
    """An implementation of `Fleet` backed by a dictionary"""
    def __init__(self, vehicles: List[Vehicle], home_base: Location):
        self._id_to_vehicle: Dict[VehicleId, Vehicle] = {v.vehicle_id: v for v in vehicles}
        self._home_base = home_base

    @property
    def home_base(self) -> Location:
        return self._home_base

    def vehicles(self) -> List[Vehicle]:
        return list(self._id_to_vehicle.values())

    def update_or_add(self, vehicle: Vehicle):
        # TODO: Unit test
        if vehicle.vehicle_id in self._id_to_vehicle:
            self._id_to_vehicle[vehicle.vehicle_id].latest_location = vehicle.latest_location
        else:
            self._id_to_vehicle[vehicle.vehicle_id] = vehicle

    def vehicles_within_distance_km(self, distance_km) -> List[Vehicle]:
        # TODO: (siddharth) There is potential to make this faster by introducing a flag that gauges whether it is
        #  physically feasible for a vehicle to enter/exit the 200km radius in an upcoming iteration
        return [
            v for v in self.vehicles() if DistanceUtils.haversine_distance_km(
                v.latest_location, self.home_base
            ) < distance_km
        ]
