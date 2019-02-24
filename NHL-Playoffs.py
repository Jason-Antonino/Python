print("Best of Seven NHL Playoff Series")

from time import sleep
from random import randrange
#from random import choice

team1 = input("Enter first team name: ")
team2 = input("Enter second team name: ")

counta = 0 #Team 1 starting with zero games won
countb = 0 #Team 2 starting with zero games won

print("")
for n in range(7): #defines a best-of-seven series starting from game zero and finishing with game six if necessary
    x = randrange(10) #Team1 score as a random whole number between 0 and 9, inclusive
    y = randrange(10) #Team2 score as a random whole number between 0 and 9, inclusive
        
    if x > y:
        print(team1, x, ",", team2, y)
        print(team1 + " win!")
        counta += 1 #Team1 gains one win in the series
        sleep(2)
        print("")
    elif y > x:
        print(team2, y, ",", team1, x)
        print(team2 + " win!")
        countb += 1 #Team2 gains one win in the series
        sleep(2)
        print("")

    if x == y: #if there's a tie game
        otwinnr = randrange(2) #picks a zero or one to decide overtime winner
        otnum = randrange(1,5) #number of overtime periods ranging from 1 to 4
        if otwinnr == 0:
            print(team1, x+1, ",", team2, y, " ", otnum,"OT") #Team1 wins in overtime 
            print(team1, "win in overtime number", otnum)
            counta += 1
            sleep(2)
            print("")
        elif otwinnr == 1:
            print(team2, y+1, ",", team1, x, " ", otnum,"OT") #Team2 wins in overtime
            print(team2, "win in overtime number", otnum)
            countb += 1
            sleep(2)
            print("")

    if counta == 4: #Team1 is the first to win 4 games in the series
        sleep(2)
        print(team1, "win the series", counta, "games to", countb)
        sleep(1)
        break

    elif countb == 4: #Team2 wins 4 games first
        sleep(2)
        print(team2, "win the series", countb, "games to", counta)
        sleep(1)
        break

input("\n\nPress Enter to exit.")