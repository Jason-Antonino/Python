# Best of Seven NHL Playoff Series

from random import randrange

team1 = input("Enter first team name: ")
team2 = input("Enter second team name: ")

counta = 0
countb = 0

for n in range(0, 7):
    x = randrange(0, 11)
    y = randrange(0, 11)
    
    if x == y:
        r = randrange(1, 2)
        if r == 1:
            print(team1, x+1, team2, y, "(OT)")
            print("Team 1 wins in overtime!")
            counta += 1
        elif r == 2:
            print(team2, y+1, team1, x, "(OT)")
            print("Team 2 wins in overtime!")
            countb += 1
        
    if x > y:
        print(team1, x, team2, y)
        print("Team 1 wins!")
        counta += 1
        
    elif y > x:
        print(team2, y, team1, x)
        print("Team 2 wins!")
        countb += 1

    if counta == 4:
        print("\n", team1, "wins the series", counta, "games to", countb)
        break
    elif countb == 4:
        print("\n", team2, "wins the series", countb, "games to", counta)
        break
    
    print("")
