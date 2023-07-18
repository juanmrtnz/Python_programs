import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".csv") == False:
    sys.exit("First command-line argument is not a csv file")

if sys.argv[2].endswith(".csv") == False:
    sys.exit("Second command-line argument is not a csv file")

table = []

try:
    with open(sys.argv[1]) as file1:
        reader = csv.DictReader(file1)
        for line in reader:
            table.append(line)

    with open(sys.argv[2], 'w') as file2:
        writer = csv.DictWriter(file2, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for line in table:
            last, first = line['name'].split(', ')
            writer.writerow({'first': first, 'last': last, 'house': line['house']})


except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])
