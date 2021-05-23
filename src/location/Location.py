""" Location.py
"""
from datetime import datetime


class Location(object):
    """Stores the time and location information of an observation"""
    MIN_LATITUDE = -90
    MAX_LATITUDE = 90
    MIN_LONGITUDE = -180
    MAX_LONGITUDE = 180

    def __init__(
        self,
        latitude: float,
        longitude: float,
        timestamp: datetime = datetime(1970, 1, 1),
        address: str = ""
    ):
        assert Location.MIN_LATITUDE <= latitude <= Location.MAX_LATITUDE, "Latitude should be in range [-90, 90]"
        assert Location.MIN_LONGITUDE <= longitude <= Location.MAX_LONGITUDE, "Longitude should be in range [-180, 180]"
        self._latitude = latitude
        self._longitude = longitude
        self._timestamp = timestamp
        self._address = address

    def __eq__(self, other):
        return (isinstance(other, Location)
                and self.address == other.address
                and self.latitude == other.latitude
                and self.longitude == other.longitude
                and self.timestamp == other.timestamp
                )

    def __str__(self):
        return "Latitude: {}, Longitude: {}".format(self.latitude, self.longitude)

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def address(self) -> str:
        return self._address
