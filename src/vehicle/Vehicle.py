"""Vehicle.py
"""
from __future__ import annotations

import abc
from typing import List

from src.location.Location import Location

VehicleId = str


class Vehicle(metaclass=abc.ABCMeta):
    """Provides information to identify a vehicle along with recent location information"""

    @property
    def latest_location(self) -> Location:
        """The most recent known `Location` of the vehicle"""
        raise NotImplementedError

    @latest_location.setter
    def latest_location(self, location: Location) -> None:
        """Setter to update the most recent location"""
        raise NotImplementedError

    @property
    def address(self) -> str:
        """The reverse geocoded address of the `latest_location` of the vehicle"""
        raise NotImplementedError

    @property
    def vehicle_id(self) -> VehicleId:
        """A unique identifier for the vehicle"""
        raise NotImplementedError

    @property
    def locations(self) -> List[Location]:
        """Recent location history of the vehicle"""
        raise NotImplementedError
