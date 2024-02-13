column_widths = [7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 4, 7, 5, 5, 5, 5, 4]
lines_seen_so_far = set()
notes = ('GLOBAL', 'sources', 'using', 'Notes', 'AnnMean', 'Divide', 'Multiply', 'Example', 'change', 'Year')

# Open the fixed-width text file for reading
with open('data\GLB.Ts+dSST.txt', 'r') as f:
    lines = f.readlines()

# Open the CSV file for writing
with open('clean_data.csv', 'w') as csvfile:
    # Write the header row if needed
    # f.write('Column1,Column2,...\n')
    heading_line = 'Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,J-D,D-N,DJF,MAM,JJA,SON,Year\n'
    csvfile.write(heading_line)

    # Parse each line and write to CSV
    for line in lines:
        start = 0
        row = []
        if line.strip() == "" or line in lines_seen_so_far or line.strip().startswith(notes):
                continue  # Skip empty lines, or lines that are repeated, or lines from the notes
        lines_seen_so_far.add(line)
        print(line)
        for i, width in enumerate(column_widths):
            # Extract the value for the current column
            value = line[start:start+width].strip()
            if '*' in value:
                value = '-'  # Replace asterisks with placeholder for missing data
            elif i != 0 and i != len(column_widths) - 1:  # Exclude first and last columns
                value = '{:.1f}'.format(float(value) / 100 * 1.8)  # Convert 0.01 Celsius to Fahrenheit
            row.append(value)
            start += width

        csvfile.write(','.join(row) + '\n')