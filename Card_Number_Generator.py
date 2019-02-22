from random import randrange

cardnum = [] #credit card number starts out as an empty list

#Four individual loops to generate four sets of 4 random numbers from 0 to 9, each set separated by a blank space

for num in range(4):
    x = randrange(10)
    cardnum.append(x)
    
cardnum.append(" ")

for num in range(4):
    x = randrange(10)
    cardnum.append(x)

cardnum.append(" ")

for num in range(4):
    x = randrange(10)
    cardnum.append(x)

cardnum.append(" ")

for num in range(4):
    x = randrange(10)
    cardnum.append(x)

print("Your credit card number is:\n") #outputs credit card number on a new line
print(''.join(map(str, cardnum))) #converts list format to numerical string format

print("")
print("\nWith an expiration date of:", "{:0>2d}".format(randrange(1,13)), "/", randrange(19,25)) #formats the month as two digits
print("\nand a CVN/CVV of:", "{:0>3d}".format(randrange(1,1000))) #formats the CVV as 3 digits

input("\n\nPress any key to exit")
