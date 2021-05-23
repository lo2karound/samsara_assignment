""" FleetFactory.py
"""
from typing import List

from src.fleet.Fleet import Fleet
from src.fleet.impl.DictFleet import DictFleet
from src.location.Location import Location
from src.vehicle.Vehicle import Vehicle


class FleetFactory:
    @staticmethod
    def get_dict_fleet(vehicles: List[Vehicle], home_base: Location) -> Fleet:
        return DictFleet(vehicles, home_base)
