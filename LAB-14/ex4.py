# Get public license data from the City of Chicago.
import ssl
import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)

# Specify the specific data file.
json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)
# Convert to pandas dataframe.
results_df = pd.DataFrame.from_records(results)
results_df.info()

vehicles = results_df[["public_vehicle_number", "vehicle_fuel_sources"]]
print("Public vehicles and fuel sources:")

vehicles.info()
vehicles_for_fuel = vehicles.groupby("vehicle_fuel_sources").count()
print(vehicles_for_fuel)