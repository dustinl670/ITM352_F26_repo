# Read a taxi file of trip data and display it using pandas.
# Print summary statistics about the dataframe, as well as the median.
import pandas as pd

# Read the JSON file into a DataFrame
df = pd.read_json('taxitrips.JSON')

# Display the first few rows of the DataFrame
print(df.head(6))

# Display basic statistics about the DataFrame
print(df.describe())

median = df['fare'].median()
print("The median fare value is:", median)