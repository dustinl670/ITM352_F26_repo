# Create a dataframe from a CSV file, read a Pivot Table, and calculate total sales.
# Name: Dustin Lopera
# Date: October 30, 2026

import pandas as pd
import numpy as np
import ssl
import pyarrow

# Ignore SSL certificate verification warnings.
ssl._create_default_https_context = ssl._create_unverified_context

# Tell Pandas to print all the columns.
pd.set_option('display.max_columns', None)
csv_file = ('sales_data.csv')

try:
    df = pd.read_csv(csv_file, engine='pyarrow', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    print(df.head())

    # Calculate total sales per row.
    df['total_sales'] = df['quantity'] * df['unit_price']

    # Create a PIVOT Table aggregating sales by region and order type.
    pivot_table = pd.pivot_table(df,
                                 values = 'total_sales',
                                 index = 'sales_region',
                                 columns = 'order_type',
                                 aggfunc = np.sum,
                                 margins = True,
                                 margins_name = 'Total_Sales')
    print(pivot_table)

except Exception as e:
    print("Error reading CSV file:", e)
