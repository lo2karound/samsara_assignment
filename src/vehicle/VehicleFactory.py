""" VehicleFactory.py
"""
from datetime import datetime
from typing import Dict

from src.Constants import Constants
from src.location.Location import Location
from src.vehicle.Vehicle import Vehicle
from src.vehicle.impl.VehicleImpl import VehicleImpl


class VehicleFactory:
    @staticmethod
    def from_attributes(location: Location, vehicle_id: str) -> Vehicle:
        return VehicleImpl(location, vehicle_id)

    @staticmethod
    def from_vehicle_location_json(vehicle_json: Dict) -> Vehicle:
        return VehicleFactory.from_attributes(
            Location(
                vehicle_json["location"]["latitude"],
                vehicle_json["location"]["longitude"],
                Constants.UTC.localize(datetime.strptime(vehicle_json["location"]["time"], "%Y-%m-%dT%H:%M:%SZ")),
                vehicle_json["location"]["reverseGeo"]
            ),
            vehicle_json["id"]
        )
