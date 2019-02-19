from time import sleep
lafayette_troupes = ("Vinny", "Frankie", "Johnny", "Caul", "Milton", "Carmine")
print("We are the Lafayette Troupes.")
sleep(2)
print("There's ")
for guy in lafayette_troupes:
    print(guy, end=", ")
    
print("")
sleep(1)
name = input("What's your name? ")
if name in lafayette_troupes:
    print("You're with the Lafayette Troupes!")
else:
    print("Fuck off!")

input("\n\nPress Enter to exit")