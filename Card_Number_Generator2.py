from time import sleep
from random import randrange

cardnum = [] #credit card number starts out as an empty list

#First Set of Numbers----------------------
x = randrange(1,10000) #picks random number from 1 to 9999, inclusive
x = int(x) 
x = "{:0>4d}".format(x) #formats this number with zeroes padded to the left
cardnum.append(x) #appends this number to the cardnum list
    
cardnum.append(" ") #blank space separator between sets

#Second Set----------------
y = randrange(1,10000)
y = int(y)
y = "{:0>4d}".format(y)
cardnum.append(y)

cardnum.append(" ")

#Third Set-----------------
z = randrange(1,10000)
z = int(z)
z = "{:0>4d}".format(z)
cardnum.append(z)

cardnum.append(" ")

#Fourth Set----------------
n = randrange(1,10000)
n = int(n)
n = "{:0>4d}".format(n)
cardnum.append(n)

#OUTPUTS------------------------------
print("Congratulations! Your card account data is below.")
cardnum = ''.join(map(str, cardnum)) #removes list formatting by converting the list to a string and then deleting the brackets and commas
sleep(1.5)
print("\nYour credit card number is:", cardnum)
sleep(1.5)
print("\nWith an expiration date of:", "{:0>2d}".format(randrange(1,13)), "/", randrange(19,24)) #two-digit month / two-digit year from 2019-2023
sleep(1.5)
print("\nand a CVN/CVV of:", "{:0>3d}".format(randrange(1,1000))) #three-digit CVV number 1 to 999 with padded zeroes to the left
sleep(1)
input("\n\nPress enter key to exit.")