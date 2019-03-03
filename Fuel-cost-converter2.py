from time import sleep
from forex_python.converter import CurrencyRates

#User inputs ----------------------------------->
print("US-to-Mexico Fuel Conversion")
sleep(1)
print("Hey Gringo!")
sleep(1)
print("You wanna convert our pesos-per-liter fuel cost to your 'merican dollars-per-gallon?")
sleep(2)

#Formulas -------------------------------------->
c = CurrencyRates()
exchrate = c.get_rate('USD', 'MXN')
gas_price = input("Okay! Gringo, enter the price per liter of Magna gas in pesos: ")
gas_price = float(gas_price)
exchrate = float(exchrate)
gallons = 3.785
usdollars = gas_price / exchrate
    
sleep(2)

#Output ---------------------------------------->
print("\nOkay Gringo, your price is $", round(usdollars * gallons, 2), "per gallon.")
print("There are", exchrate, "pesos per US dollar.")
print("Adios, amigos!")
input("\n\nPress any key to exit.")