# Read a taxi file of trip data and display it using pandas.
# Print summary statistics about the dataframe, as well as the median.

import pandas as pd

df = pd.read_json("taxitrips.JSON", lines=True)

print(df.head(6))

print(df.describe())

median = df['fare'].median()
print("The value of the median is: ", median)