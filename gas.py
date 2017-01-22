#! python3
# Author simottar@gmail.com
# companyNameExcel.py - Prints the name for an icelandic registered company from the command line.

import sys, json, requests, operator

# class to keep track of the gas stations
class GasStation:
    'Common base class for gas stations'

    def __init__(self, price, address, company):
        self.price = price
        self.address = address
        self.company = company   

    def displayPrices(self):        
        print('price: {}, company: {}, address: {}'.format(self.price, self.company, self.address))

# Get the search criteria from command line arguments.
if len(sys.argv) < 3:
    print('Usage: bensin95 or bensin95_discount or diesel or diesel_discount | max or min')
    sys.exit()

searchCrit = sys.argv[1]
op_input = sys.argv[2]

# check if the search criteria exists
if not any(searchCrit in criteria for criteria in ['bensin95','bensin95_discount', 'diesel', 'diesel_discount']):
    print('use correct input: bensin95 or bensin95_discount or diesel or diesel_discount')
    sys.exit()

# check if the comparision exists
if not any(op_input in op for op in ['min','max']):
    print('use correct input: min for lowest price or max for highest price')
    sys.exit()


# define the operators to use in comparison
ops = {"min": operator.gt, "max": operator.lt}
op_func = ops[op_input]

# return values 
price = 9999
if op_input == 'max':
    price = 0

company = "no result"
address = "no result"
station = GasStation(price,company,address)

# fetch the prices from apis.is
url = "http://apis.is/petrol"

# bypass proxy!!!
session = requests.Session()
session.trust_env = False

response = session.get(url)
response.raise_for_status()

#print(response.text)
# Load JSON data into a Python variable.
jsonToPython = json.loads(response.text)



# extract from results
result = jsonToPython['results']

stationList = []
# check for cheapest price
for i in range(0, len(result)):
    if result[i][searchCrit]:    
        thisPrice = float(result[i][searchCrit])
        if op_func(station.price, thisPrice):
            stationList = []
            station.price = thisPrice
            station.company = result[i]['company']
            station.address = result[i]['name']
            stationList = [station]            
        elif station.price == thisPrice:
            stationList.append(GasStation(thisPrice,result[i]['name'],result[i]['company']))                    

for s in stationList:
    s.displayPrices()



