""" TestDistanceUtils.py
"""
from math import radians, cos, sin, asin, sqrt

from src.Constants import Constants
from src.location.Location import Location


class DistanceUtils:

    @staticmethod
    def haversine_distance_km(location_1: Location, location_2: Location):
        """Calculate the great circle distance in kilometers between two `Location`s"""
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(
            radians, [location_1.longitude, location_1.latitude, location_2.longitude, location_2.latitude]
        )

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = Constants.RADIUS_OF_EARTH_KM
        return c * r
