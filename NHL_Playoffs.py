# Best of Seven NHL Playoff Series

from time import sleep
from random import randrange

team1 = input("Enter first team name: ")
team2 = input("Enter second team name: ")

counta = 0
countb = 0

print("")
for n in range(0, 7):
    x = randrange(0, 11)
    y = randrange(0, 11)
    
    if x == y:
        r = randrange(0, 2)
        if r == 1:
            print(team1, x+1, ",", team2, y, "(OT)")
            print(team1, "win in overtime!")
            counta += 1
        elif r == 2:
            print(team2, y+1, ",", team1, x, "(OT)")
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

    if counta == 4:
        print("")
        print(team1, "win the series", counta, "games to", countb)
        break
    elif countb == 4:
        print("")
        print(team2, "win the series", countb, "games to", counta)
        break
    
    print("")
    sleep(1)
