column_widths = [7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 4, 7, 5, 5, 5, 5, 4]
lines_seen_so_far = set()
notes = ('GLOBAL', 'sources', 'using', 'Notes', 'AnnMean', 'Divide', 'Multiply', 'Example', 'change')

# Open the fixed-width text file for reading
with open('data\GLB.Ts+dSST.txt', 'r') as f:
    lines = f.readlines()

# Open the CSV file for writing
with open('clean_data.csv', 'w') as csvfile:
    # Write the header row if needed
    # f.write('Column1,Column2,...\n')

    # Parse each line and write to CSV
    for line in lines:
        start = 0
        row = []
        if line.strip() == "" or line in lines_seen_so_far or line.strip().startswith(notes):
                continue  # Skip empty lines
        lines_seen_so_far.add(line)
        for width in column_widths:
            # Extract the value for the current column
            value = line[start:start+width].strip()
            if '*' in value:
                value = '-'  # Replace asterisks with placeholder for missing data
            row.append(value)
            start += width

        # Write the row to the CSV file
        csvfile.write(','.join(row) + '\n')