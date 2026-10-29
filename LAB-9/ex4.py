# Read taxi_1000.csv and calulate the total of all fares, average fare, 
# and max trip distance for records that have fares greater than 10 dollars.
import csv

filename = "taxi_1000.csv"

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)

    total_fare = 0.0
    max_distance = 0.0
    average_fare = 0.0
    num_rows = 0
    qualifying_trips = 0

    for row in csv_reader:
        if num_rows == 0:
            # Skip the header row
            fare_index = row.index('Fare')  # Get the index of the fare column
            distance_index = row.index('Trip Miles')  # Get the index of the distance column
            num_rows += 1
            continue

        if (num_rows > 0):
            fare = float(row[fare_index])
            distance = float(row[distance_index])

            if fare > 10:
                total_fare += fare
                qualifying_trips += 1
                if distance > max_distance:
                    max_distance = distance

        num_rows += 1

if qualifying_trips > 0:  # Ensure there are qualifying trips to avoid division by zero
    average_fare = total_fare / qualifying_trips  # Only consider fares greater than 10

print(f"Total Fare: ${total_fare:.2f}")
print(f"Average Fare: ${average_fare:.2f}")
print(f"Max Trip Distance: {max_distance:.2f} miles")