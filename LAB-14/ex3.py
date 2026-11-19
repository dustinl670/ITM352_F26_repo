# Scrape names of the faculty and grad students.

import urllib.request
from bs4 import BeautifulSoup

url = "https://shidler.hawaii.edu/itm/people"
print("Scraping data from:", url)

itm_page = urllib.request.urlopen(url)
itm_names = []

soup = BeautifulSoup(itm_page, "html.parser")

# Find all the faculty, which are in h2 tags with class = title.
faculty = soup.find_all("h2", class_="title")

for person in faculty:
    itm_names.append(person.get_text())
    print("Faculty:", person.get_text())

print("Total Faculty:", len(itm_names))
