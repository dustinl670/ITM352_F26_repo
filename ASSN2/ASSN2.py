import pandas as pd
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context 

saved_results = {} # Dictionary to store saved results.

# List of required columns for the CSV file.
required_columns = ["order_number", "employee_id", "employee_name", "job_title", "sales_region",
                    "order_date", "order_type", "customer_type", "customer_name", "customer_state",
                    "product_category", "produce_name", "quantity", "unit_price", "product_number"]
                    

def load_csv(filepath): # Loading CSV file to Pandas DataFrame.
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time() # To record start time.

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')  # Load CSV into DataFrame, skipping bad lines.
        end_time = time.time() # Record end time after loading CSV.
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Number of columns: {len(df.columns)}")
        missing_columns = [col for col in required_columns if col not in df.columns] # Checks for missing columns.
        if missing_columns:
            print(f"Warning: Missing required columns: {', '.join(missing_columns)}")
        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None


# Function to display initial rows of the DataFrame.
def display_initial_rows(data):
    while True:
        response = input(
            f"\nHow many initial rows would you like to see? "
            f"(1-{len(data)}, or 'all'): " # Prompt user for number of initial rows to display
        ).strip().lower()

        if response == "all":
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f"Invalid input '{response}'. Please enter a whole number or 'all'.")
            continue

        if num_rows < 1:
            print("Please enter a number greater than 0.")
            continue

        if num_rows > len(data):
            print(f"Only {len(data)} rows available; showing all of them.")
            continue

        print(data.head(num_rows))
        return

# Function to show the number of unique employees by sales region.
def show_employees_by_region(data):
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("\nNumber of employees by region:")
    print(counts.to_string())
    return counts

# Function to get user selection from a list of options.
def get_user_selection(options, prompt, required=False, single=False):
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))
        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected

# Function to create custom pivot tables.
def generate_custom_pivot_table(data):
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns available to aggregate.")
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table)
    return pivot_table

# Function to show avg sales by region.
def show_average_sales_by_region(data):
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    return pivot_table

# Function to show total sales by region and order type.
def show_total_sales_by_region_and_order_type(data):
    required = ["sales_region", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns="order_type",
        values="sales",
        aggfunc="sum",
    )
    print("\nTotal sales by region and order type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    return pivot_table

# Function to show sales by customer type and order type by state.
def show_sales_by_customer_type_and_order_type_by_state(data):
    required = ["customer_type", "order_type", "customer_state", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
       sales,
       index=["customer_state", "customer_type", "order_type"],
       values="sales",
       aggfunc="sum"
    )

    
    print("\nSales by customer type and order type by state:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    return pivot_table

# Function to show total sales quantity and price by region and product.
def show_total_sales_quantity_price_by_region_and_product(data):
    required = ["sales_region", "product_category", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(
        total_sales=data["quantity"] * data["unit_price"]
    )
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns="product_category",
        values=["quantity", "total_sales"],
        aggfunc="sum",
    )
    print("\nTotal sales quantity and price by region and product:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    return pivot_table

# Function to show total sales quantity and price by customer type.
def show_total_sales_quantity_price_by_customer_type(data):
    required = ["customer_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(
        total_sales=data["quantity"] * data["unit_price"]
    )
    pivot_table = pd.pivot_table(
        sales,
        index="customer_type",
        values=["quantity", "total_sales"],
        aggfunc="sum",
    )
    print("\nTotal sales quantity and price by customer type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    return pivot_table

# Function to show maximum and minimum sales price of sales by category.
def show_max_min_sales_price_by_category(data):
    required = ["product_category", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    pivot_table = pd.pivot_table(
        data,
        index="product_category",
        values=data["quantity"] * data["unit_price"],
        aggfunc=["max", "min"]
    )
    print("\nMaximum and minimum sales price by category:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    return pivot_table


def exit_program(data=None):
    print("Exiting the program. Byeeeee!")
    raise SystemExit(0)

# Requirement 2: Storing/showing saved results.
# *AI USAGE: Claude/Copilot was used to aid me with formatting and code placement.
# Function to show all saved results.
def show_saved_results(data=None):
    if not saved_results:
        print("No saved results available.")
        return
    for name, runs in saved_results.items():
        for number, result in enumerate(runs, start=1):
            print(f"\n{name}")
            print(result)

menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show total sales by region and order type", show_total_sales_by_region_and_order_type),
    ("Average sales by region, by state and sale type", show_average_sales_by_region),
    ("Show sales by customer type and order type by state", show_sales_by_customer_type_and_order_type_by_state),
    ("Show total sales quantity/price by region and product", show_total_sales_quantity_price_by_region_and_product),
    ("Show total sales quantity/price by customer type", show_total_sales_quantity_price_by_customer_type),
    ("Show maximum and minimum sales price of sales by category", show_max_min_sales_price_by_category),
    ("Show the number of unique employees by region", show_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Show all saved results", show_saved_results),
    ("Exit the program", exit_program),
)


def display_menu():
    while True:
        print("\n---Sales Data Dashboard---")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"\nSelect an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")

# Requirement 1: Selecting a row range from the data.
# *AI Usage: Copilot aided me in generating proper formatting of what I needed the function to do.
# Function to select a row range from the data.
def select_row_range(data):
    while True:
        try:
            start = int(input(f"What row do you want to start with? (1-{len(data)}): "))
            end = int(input(f"Enter the ending row. ({start}-{len(data)}): "))
        except ValueError:
            print("Please enter whole numbers.")
            continue

        if 1 <= start <= end <= len(data): # Checks if range is valid before returning.
            return data.iloc[start - 1:end]

        print(f"Enter a valid range between 1 and {len(data)}.")

def main():
    csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    try:
        while True:
            selection = display_menu()
            name, action = menu_options[selection]

            if action in (display_initial_rows, show_saved_results, exit_program): # Actions that do not require row selection.
                action(sales_data)
            elif sales_data.empty:
                print("There are no rows to analyze.")
            else:
                selected_data = select_row_range(sales_data)
                result = action(selected_data)

                if result is not None:
                    saved_results.setdefault(name, []).append(result)
    except (KeyboardInterrupt, EOFError): # For handling user interruptions (Ctrl+C or Ctrl+D).
        print("\nExiting.")


if __name__ == "__main__":
    main()