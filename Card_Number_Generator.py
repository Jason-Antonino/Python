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

print("Your credit card number is: \n")
print(''.join(map(str, cardnum)))

print("")
print("\nWith an expiration date of: ", randrange(1,13), "/", randrange(19,25))
print("\nand a CVN/CVV of: ", randrange(100,1000))

input("\n\nPress any key to exit")