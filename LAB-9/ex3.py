# Read the 1000 lines of data from tax_1000.csv
# Calculate the the total of all fares, the average of those fares, and the maximum trip distance (based on the Trip Miles field) for records that have fares greater than 10 dollars.
import csv

filename = "..\\tax_1000.csv" 

with open(filename, "r") as file:
    csv_reader = csv.reader(file)

    total_fares = 0
    max_distance = 0
    average_fare = 0
    num_rows = 0

    for row in csv_reader:
        if num_rows == 0:
            # Skip the header row.
            fare_index = row.index("Fare")
            distance_index = row.index("Trip Miles")
            num_rows += 1
            continue

        if (num_rows > 0):
            fare = float(row[fare_index])
            distance = float(row[distance_index])

            total_fares += fare
            if distance > max_distance:
                max_distance = distance

        num_rows += 1

if num_rows > 1:
    average_fare = total_fares / (num_rows - 1)

print("Total fares:", total_fares)
print("Average fare:", average_fare)
print("Maximum trip distance:", max_distance)
