#importing libraries
#import urllib.request
import time
#from BeautifulSoup4 import BeautifulSoup

"""
#URL declaration
pageaddr = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=MXN&To=USD"

#opens the URL
page = urllib.request.urlopen(pageaddr)

#parsing the web page using BeautifulSoup
soup = BeautifulSoup(page,'html.parser')

#locate the exact piece of data and get its value from this segment: <span class="converterresult-toAmount">
name = soup.find('span', attrs={'class': 'converterresult-toAmount'})
name = name.text.strip() #removes extra whitespace characters
"""

#collects input from user
print("US-to-Mexico Fuel Conversion")
time.sleep(1)
print("Hey Gringo!")
time.sleep(1)
print("You wanna convert our pesos-per-liter fuel cost to your 'merican dollars-per-gallon?")
time.sleep(2)
gas_price = input("Gringo, enter the price per liter of Magna gas in pesos: ")
time.sleep(1)
rate = input("What's the exchange rate, mane? (pesos per dollar): ")

#Formulas
gas_price = float(gas_price)
rate = float(rate)
liter = float(1)
gallon = liter*3.785
dollars = gas_price / rate
time.sleep(2)

#Output
print("\nOkay Gringo, your price in dollars-per-gallon is $", round(dollars*gallon, 2))
print("Adios, amigos!")
input("\n\nPress any key to exit.")