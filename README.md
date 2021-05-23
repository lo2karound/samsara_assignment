## App to process Samsara Telemetry

This module is intended to visualize and derive insights from telemetry obtained from the Smasara fleets.

The entry point for this module is `src/App.py`. The application currently works for a single fleet but support for 
multiple fleets has been built in.

To run the application in PyCharm, hit the green 'play' button next to the line `if __name__ == "__main__":`.

This will start producing plots every 10 seconds with the latest location for all vehicles in the fleet.
Currently, the past 100 locations of each vehicle are stored. With a vehicle that is continuously observed, this
corresponds to a duration of `100 * 10 = 1000 seconds ~ 17minutes`. This parameter is also configurable.

### Design choices
 - I chose not to create a database as the volume of data that is being dealt with is low.
 - As the data volume increases, if only the latest location of each vehicle is to be stored, any relational database 
   could be used instead    
 - If entire trajectories for vehicles are to be stored, the time and distance could be delta-encoded and perhaps stored
   in a document format
 - I wrote this in Python as I am not too familiar with the support for plotting in React
 - I realize that not hosting this on Heroku/a PaaS is not ideal. I am a bit rusty on working with these but I have 
   worked with them in the past and should be up to speed in a few days
   
### Note
The Samsara API token has not been checked in. To get the App to run, add the token to `SamsaraApi.py` in the line 
`headers = {"Authorization": "Bearer {token here}"}`