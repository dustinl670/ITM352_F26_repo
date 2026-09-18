# Define a list of survey response values (1, 2, 3, 4) and store them.
# In a variable, define a tuple of responses

response_values = [5, 7, 3, 8]
response_values.sort()
response_ids = (1012, 1035, 1021, 1053)
response_values.append(response_ids)

print("Combined response values and ids: ", response_values)

response_values_new = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
print("Combined response values and tuples: ", response_values_new)