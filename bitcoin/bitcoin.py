import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
    response = (requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')).json()
    response = float(response['bpi']['USD']['rate_float'])

except ValueError:
    sys.exit("Command-line argument is not a number")

output = response * float(sys.argv[1])
print(f"${output:,.4f}")

