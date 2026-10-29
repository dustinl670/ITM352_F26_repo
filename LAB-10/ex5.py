import pandas as pd
# Read the homes data from the provided Google Drive link and display the first few rows.
homes_data_file = ('homes_data.csv')
homes_df = pd.read_csv(homes_data_file)
print(homes_df.head())

# Print the dimensions of the dataframe.
shape = homes_df.shape
print("The dimensions of the dataframe are: ", shape)

# Only keep units with more than 500 units and drop the easement column.
df_big = homes_df[homes_df['units'] >= 500]
df_big = df_big.drop(columns=['easement'])
print(df_big.head(10))

print(df_big.info())

# coerce land_sqft, gross_sqft, and sales_price to numeric values
df_big['land_sqft'] = pd.to_numeric(df_big['land_sqft'], errors='coerce')
df_big['gross_sqft'] = pd.to_numeric(df_big['gross_sqft'], errors='coerce')
df_big['sale_price'] = pd.to_numeric(df_big['sale_price'], errors='coerce')

print("After cleaning...")
print(df_big.info())
print(df_big.head(10))

# Drop the null values.
df_big = df_big.dropna()

# Now drop duplicate records.
df_big = df_big.drop_duplicates()
print("After dropping duplicates...")
print(df_big.info())
print(df_big.head(10))

# Filter out 0 sales.
df_big = df_big[df_big['sale_price'] > 0]
print("After filtering out 0 sales...")
print(df_big.info())
print(df_big.head(10))