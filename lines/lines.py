import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

line_count = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip().startswith('#') == True or line.strip() == '':
                pass
            else:
                line_count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(line_count)