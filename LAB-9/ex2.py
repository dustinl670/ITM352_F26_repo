

import csv
import os

# Check if the file exists and is readable.
if not os.path.isfile("window_cleaning_employees.csv"):
    print(f"Error: File not found.")
    exit(1)

if not os.access("window_cleaning_employees.csv", os.R_OK):
    print(f"Error: File not readable.")
    exit(1)

else:
    file_



csv_filename = "window_cleaning_employees.csv"
salaries = []

# Read the CSV file and extract the salaries into the list.
with open(csv_filename, "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)
    print("Headers:", headers)
    salary_index = headers.index("Annual_Salary")
    for row in reader:
        salary = float(row[salary_index])
        salaries.append(salary)

# Compute salary stats.
avg_salary = sum(salaries) / len(salaries)
min_salary = min(salaries)
max_salary = max(salaries)

# Print the stats.
print(f"Average Salary: ${avg_salary:.2f}")
print(f"Minimum Salary: ${min_salary:.2f}")
print(f"Maximum Salary: ${max_salary:.2f}")