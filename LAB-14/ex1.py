# Scrape data from the city of chicago's data portal.
# Print any line with a title tag.
# Name: Dustin Lopera
# Date: November 18, 2026

import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

print("Scraping data from:", url)
response = urllib.request.urlopen(url)

for line in response:
    line = line.decode("utf-8")
    if "<title>" in line:
        print(line)


