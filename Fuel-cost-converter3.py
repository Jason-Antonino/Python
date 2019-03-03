from time import sleep
from forex_python.converter import CurrencyRates

print("International Fuel Conversion Cost Calculator")
sleep(1)

#Formulas -------------------------------------->
c = CurrencyRates()
dict = c.get_rates('USD') #dictionary of countries and conversion factors
key = input("Enter 3-character code for the country you want (e.g. MXN): ")
key = key.upper() #forces uppercase lettering

exchrate = dict[key] #cross-reference country code with conversion factor in dictionary
exchrate = float(exchrate)

gas_price = input("Enter the price per liter of gas in foreign currency: ")
gas_price = float(gas_price)

liters = 1.00
gallons = 3.785 * liters

usdollars = gas_price / exchrate

convprice = usdollars * gallons
convprice = round(convprice, 3)  

sleep(2)

#Output ---------------------------------------->
print("\nYour price is", '${:,.3f}'.format(convprice), "per US gallon.")
sleep(1)
print("There are", exchrate, key, "per US dollar.")
input("\n\nPress any key to exit.")