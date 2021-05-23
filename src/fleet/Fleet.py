""" Fleet.py
"""
import abc
from typing import List

from matplotlib import pyplot as plt

from src.location.Location import Location
from src.vehicle.Vehicle import Vehicle


class Fleet(metaclass=abc.ABCMeta):
    """A `Fleet` is a collection of `Vehicle`s with a common Home Base. New vehicles can be added to a fleet or the
    location of vehicles existing in the fleet can be updated. This API currently does not support removing vehicles
    from the fleet"""

    @property
    def home_base(self) -> Location:
        """:return The `Location` of the Home Base"""
        raise NotImplementedError

    def vehicles(self) -> List[Vehicle]:
        """:return List of all vehicles in the fleet"""
        raise NotImplementedError

    def update_or_add(self, vehicle: Vehicle):
        """If `vehicle` exists in the fleet, update its location. Else add the vehicle to the fleet"""
        raise NotImplementedError

    def vehicles_within_distance_km(self, distance_km) -> List[Vehicle]:
        """Returns the list of all vehicles that are within `distance_km` of the Home Base"""
        raise NotImplementedError

    def plot_locations(self):
        """Method to plot the most recent locations.
        TODO: (siddharth) Update background to a map layer"""
        vehicles = self.vehicles()
        latitudes = [vehicle.latest_location.latitude for vehicle in vehicles]
        longitudes = [vehicle.latest_location.longitude for vehicle in vehicles]
        plt.plot(longitudes, latitudes, 'rs')
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.show()
