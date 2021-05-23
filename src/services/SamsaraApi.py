import json
from typing import List

import requests

from src.vehicle.Vehicle import Vehicle
from src.vehicle.VehicleFactory import VehicleFactory

endpoint = "https://api.samsara.com/fleet/vehicles/locations"
headers = {"Authorization": "Bearer {token here}"}


class SamsaraApi(object):
    @staticmethod
    def get_vehicles() -> List[Vehicle]:
        """Invokes the vehicle location endpoint of the Samsara API and returns the list of vehicles that were observed
         TODO: Unit test with mocking
        """
        response = requests.get(endpoint, headers=headers)
        vehicle_locations_json = json.loads(response.content)["data"]
        return [VehicleFactory.from_vehicle_location_json(vehicle_json) for vehicle_json in vehicle_locations_json]
