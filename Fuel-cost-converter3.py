from time import sleep
from forex_python.converter import CurrencyRates
import datetime

print("International Fuel Cost Conversion Calculator")
sleep(1)

#Formulas -------------------------------------->
c = CurrencyRates()
dict = c.get_rates('USD') #builds a dictionary of countries and conversion factors
key = input("Enter 3-character code for the country you want (e.g. MXN, CAD): ")
key = key.upper() #forces uppercase lettering

exchrate = dict[key] #cross-reference the country code with its conversion factor in the dictionary
exchrate = float(exchrate)

gas_price = input("Enter the price PER LITER of gas in the foreign currency: ")
gas_price = float(gas_price)

liters = 1.00
gallons = 3.785 * liters #converts price per liter to price per US gallon

usdollars = gas_price / exchrate #converts gas price to USD
convprice = usdollars * gallons #converts USD-per-liter to USD-per-gallon

today = datetime.datetime.now()
today = (today.strftime("%B") + " " + today.strftime("%d") + ',' + " " + today.strftime("%Y"))

sleep(2)

#Output ---------------------------------------->
print('')
for x in range(10):
    print(".", end='')
    sleep(0.4)

print('')    
print("\nYour price is", '${:,.3f}'.format(convprice), "per US gallon.")
sleep(1.5)
print("\nThere are", exchrate, key, "per US dollar, as of", today + ".")
sleep(1.75)
input("\n\nPress Enter key to exit.")