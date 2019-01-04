# 99 Bottles of Beer but with a random starting number

from random import randint

x = randint(1, 100)
for n in range(x):
    if x == 1:
        print (x, " bottle of beer on the wall,")
    else:
        print (x, " bottles of beer on the wall,")
        print (x, " bottles of beer.")
    print ("Take one down and pass it around, ")
    x = x-1
    if x == 1:
        print (x, " bottle of beer on the wall.")
    elif x == 0:
        print ("Now all the beer is gone. Let's get weed now.") 
    else:
        print (x, " bottles of beer on the wall.")
    print ("")
