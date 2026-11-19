# Grab one month interest rate data from the US treasury website.
# Name: Dustin Lopera
# Date: November 18, 2026

import ssl, lxml
from urllib import response
import pandas as pd
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603" 
print("Scraping data from:", url)

webpage = urllib.request.urlopen(url)
df = pd.read_html(webpage)
print("Columns:", df[0].columns)

int_rate_table = df[0]

# Print the table of one month interest rates.
print("One month interest rates:")

for index, row in int_rate_table.iterrows():
    print("Date:", row["Date"], "1 Month Interest Rate:", row["1 Mo"])