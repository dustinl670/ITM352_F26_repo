
import pandas as pd
import ssl
import time

csv_file = "https://drive.google.com/file/d/1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K/view?usp=drive_link"
ssl._create_default_https_context = ssl._create_unverified_context

try:
    df = pd.read_csv(csv_file, engine='python', on_bad_lines='skip')
    outfile = "sales_data.csv"
    df.head(10).to_csv(outfile, index=False)
    print("First ten rows of csv_file saved to outfile", outfile)
except Exception as e:
    print("Error reading CSV file:", e)