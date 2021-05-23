""" VehicleImpl.py
"""
from typing import List

from queue import Queue

from src.vehicle.Vehicle import Vehicle, Location, VehicleId


class VehicleImpl(Vehicle):
    def __init__(self, location: Location, vehicle_id: str, max_num_locations: int = 100):
        """
        In implementation of `Vehicle` that uses a `Queue` of fixed length `max_num_location` to store the recent
        locations of the vehicle
        :param location: Initial `Location` of the vehicle
        :param vehicle_id: See `Vehicle.vehicle_id`
        :param max_num_locations: The number of recent location of the vehicle to be stored
        """
        self._vehicle_id = vehicle_id
        self._locations = Queue(maxsize=max_num_locations)
        self._locations.put(location)
        self._max_num_locations = max_num_locations

    @property
    def latest_location(self) -> Location:
        return self._locations.queue[-1]

    @latest_location.setter
    def latest_location(self, location: Location) -> None:
        self._locations.put(location)

    @property
    def address(self) -> str:
        return self.latest_location.address

    @property
    def vehicle_id(self) -> VehicleId:
        return self._vehicle_id

    @property
    def locations(self) -> List[Location]:
        return list(self._locations.queue)
