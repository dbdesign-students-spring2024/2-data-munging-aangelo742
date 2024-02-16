import csv

# Open the CSV file for reading
with open('clean_data.csv', 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Skip the first row
    next(csvreader)

    # Initialize variables
    current_year = 1880
    running_total = 0
    row_count = 0

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Convert dashes to None and convert row elements to floats, excluding the first and last elements
        row_values = [float(value) if value != '-' else None for value in row[1:-1]]

        # Remove None values from the row_values list
        row_values = [value for value in row_values if value is not None]

        # Calculate the average of the row values
        if row_values:  # Check if there are non-dash values
            row_average = sum(row_values) / len(row_values)
            running_total += row_average
            row_count += 1

        # If we have processed ten rows, print the average and reset the counters
        if row_count == 10:
            average_of_ten_rows = running_total / 10
            print(f"Average of {current_year}-{current_year+9}:", average_of_ten_rows)
            current_year += 10
            row_count = 0
            running_total = 0

    # If there are remaining rows, print the average of the remaining years
    if row_count > 0:
        average_of_remaining_rows = running_total / row_count
        print(f"Average of remaining years ({current_year}-2023):", average_of_remaining_rows)