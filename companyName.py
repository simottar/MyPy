#! python3
# companyName.py - Prints the name for an icelandic registered company from the command line.

import json, requests, sys

# Compute SSN from command line arguments.
if len(sys.argv) < 2:
    print('Usage: companyName.py SSN')
    sys.exit()

# Call the join() method to join all the strings except for the first in sys.argv
ssn = ' '.join(sys.argv[1:])

# Download the JSON data from apis.is API.
url ='http://apis.is/company?socialnumber=%s' % (ssn)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
companyData = json.loads(response.text)
# Print weather descriptions.
result = companyData['results']
name = result[0]['name']
print(name)