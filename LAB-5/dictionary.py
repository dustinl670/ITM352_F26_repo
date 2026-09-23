# Introduction to nested dictionaries.

country_capitals = {
    "USA": {"capital": "Washington, D.C.", "population": 331002651},
    "Canada": {"capital": "Ottawa", "population": 40000000},
    "France": {"capital": "Paris", "population": 68000000},
    "Germany": {"capital": "Berlin", "population": 84000000}
}

print("Country capitals: ", country_capitals)
print(country_capitals["Canada"]["capital"])
print(country_capitals["Canada"]["population"])

country_capitals["England"] = {"capital": "London", "population": 56000000}
print(country_capitals["England"]["capital"])

print("Germany" in country_capitals)
print("Spain" not in country_capitals)