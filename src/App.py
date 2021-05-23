""" App.py
"""
import time

from src.fleet.FleetFactory import FleetFactory
from src.location.Location import Location
from src.services.SamsaraApi import SamsaraApi


class App(object):
    """
    This Application is the entry point for the assignment
    The application hits the vehicle location endpoint of the Samsara API and tracks recent location history of the
    vehicles in the fleet.
    The API is hit every 10 seconds and the most recent location of all the vehicles is plot with each iteration.
    The App also prints out the list of all vehicles within a 200km radius of the home base in each iteration
    """

    @staticmethod
    def run():
        home_base = Location(37.998784683469, -121.28664482335675, address="1633 E Bianchi Rd, Stockton, CA 95210")
        fleet = FleetFactory.get_dict_fleet([], home_base)
        while True:
            active_vehicles = SamsaraApi.get_vehicles()
            for vehicle in active_vehicles:
                fleet.update_or_add(vehicle)
            print("Vehicles to recall: ", [v.vehicle_id for v in fleet.vehicles_within_distance_km(200)])
            fleet.plot_locations()
            time.sleep(10)  # seconds TODO: (siddharth) account for processing time of an iteration of the loop


if __name__ == "__main__":
    App.run()
