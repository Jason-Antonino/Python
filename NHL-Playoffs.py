# Best of Seven NHL Playoff Series

from time import sleep
from random import randrange

team1 = input("Enter first team name: ")
team2 = input("Enter second team name: ")

counta = 0 #Team 1 starting with zero games won
countb = 0 #Team 2 starting with zero games won

print("")
for n in range(0, 7): #defines a best-of-seven series
    x = randrange(0, 11) #Team1 score as a random number between 0 and 10
    y = randrange(0, 11) #Team2 score as a random number between 0 and 10
    
    if x == y: #if there's a tie game
        r = randrange(0, 2) #picks a zero or one
        if r == 0:
            print(team1, x+1, ",", team2, y, "(OT)") #Team1 wins in overtime
            print(team1, "win in overtime!")
            counta += 1
        elif r == 1:
            print(team2, y+1, ",", team1, x, "(OT)") #Team2 wins in overtime
            print(team2, "win in overtime!")
            countb += 1
        
    if x > y:
        print(team1, x, ",", team2, y)
        print(team1 + " win!")
        counta += 1
        
    elif y > x:
        print(team2, y, ",", team1, x)
        print(team2 + " win!")
        countb += 1

    if counta == 4: #Team1 wins 4 games
        print("")
        print(team1, "win the series", counta, "games to", countb)
        break
    elif countb == 4: #Team2 wins 4 games
        print("")
        print(team2, "win the series", countb, "games to", counta)
        break
    
    print("")
    sleep(2)

input("\n\nPress Enter to exit")