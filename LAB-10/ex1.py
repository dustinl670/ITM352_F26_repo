# Analyze household-income data using a NumPy array.
import numpy as np  # Import NumPy and give it the shorter name "np".

# Store each record as a tuple: (income percentile, household income).
hh_income = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292),
]

hh_income_array = np.array(hh_income)  # Convert the list of tuples into a NumPy array.

# ndim reports the number of axes; size reports the total number of values.
print(f"Dimensions of the array: {hh_income_array.ndim}")
print(f"Number of elements in the array: {hh_income_array.size}")

# shape[0] is the number of rows. Visit each row and unpack its two values.
for i in range(hh_income_array.shape[0]):
    percentile, income = hh_income_array[i]
    print(f"Percentile: {percentile}, Income: {income}")

# Visit each row again, printing column 0 (percentile) and column 1 (income).
for i in range(hh_income_array.shape[0]):
    print(hh_income_array[i, 0], hh_income_array[i, 1])
    
        