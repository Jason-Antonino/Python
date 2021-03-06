print("Best of Seven NHL Playoff Series")

from time import sleep
from random import randrange


west_conf_teams = [] #empty list to store West Conf team names
east_conf_teams = [] #empty list to store East Conf team names
#round1winners = [] #empty set to store winners of Quarterfinal series
next_round_teams = [] #creates an empty list to store names of teams to compete in the Semifinals
#round2winners = [] #empty set to store winning teams in Semifinal series
#round3winners = [] #empty set to store winning teams for this round
#round4teams = [] # these teams will participate in the Stanley Cup Final


def select_West_Conf(): # Select 8 West Conference Teams--------------------
    west_conf_teams = [] #empty list to store team names
    print("\nEnter Names of 8 Western Conference Teams to participate in First Round")
    for x in range(8): #8 iterations adding team names to list
        team = input("Enter team name: ")
        west_conf_teams.append(team)
        
    return west_conf_teams

def select_East_Conf(): # Select 8 East Conference Teams--------------------
    east_conf_teams = [] #empty list to store team names
    print("Enter Names of 8 Eastern Conference teams to participate in the first round")
    for x in range(8): #8 iterations adding team names to list
        team = input("Enter team name: ")
        east_conf_teams.append(team)
        
    return east_conf_teams


print("")
print("")
sleep(2)


def oneround(team1, team2): #this is a single playoff series of two teams playing against each other
    
    counta = 0 #Team 1 starting with zero games won
    countb = 0 #Team 2 starting with zero games won
    this_series_winner = [] #initializing empty list to store series winner
        
    print("")
    for n in range(7): #defines a best-of-seven series starting from game zero and finishing with game six if necessary
        print("Game", n+1)
        x = randrange(10) #Team1 score as a random whole number between 0 and 9, inclusive
        y = randrange(10) #Team2 score as a random whole number between 0 and 9, inclusive
        
        if x > y: #Team 1 wins the game
            print(team1, x, ",", team2, y)
            print(team1 + " win!")
            counta += 1 #Team1 gains one win in the series
            sleep(1)
            print("")
        elif y > x: #Team 2 wins the game
            print(team2, y, ",", team1, x)
            print(team2 + " win!")
            countb += 1 #Team2 gains one win in the series
            sleep(1)
            print("")

        if x == y: #if there's a tie game
            otwinnr = randrange(2) #picks a zero or one to decide overtime winner
            otnum = randrange(1,5) #number of overtime periods ranging from 1 to 4
            if otwinnr == 0:
                print(team1, x+1, ",", team2, y, " ", "(", otnum,"OT )") #Team1 wins in overtime 
                print(team1, "win in overtime number", otnum)
                counta += 1
                sleep(1)
                print("")
            elif otwinnr == 1:
                print(team2, y+1, ",", team1, x, " ", "(", otnum,"OT )") #Team2 wins in overtime
                print(team2, "win in overtime number", otnum)
                countb += 1
                sleep(1)
                print("")

        if counta == 4: #Team1 is the first to win 4 games in the series
            print(team1, "win the series", counta, "games to", countb)
            this_series_winner.append(team1) #append team1 to list starting at index[0]
            sleep(2)
            return this_series_winner

        elif countb == 4: #Team2 wins 4 games first
            print(team2, "win the series", countb, "games to", counta)
            this_series_winner.append(team2) #append team2 to list starting at index[0]
            sleep(2)
            return this_series_winner


def auxillary_function (team1, team2, this_series_winner):
    a = this_series_winner.count(team1)
    b = this_series_winner.count(team2)
    next_round_teams = [] #empty set to store winning teams
    
    if a > b:
        team1 = team1 #designating team1 to be the new team 1 for the next round
        next_round_teams.append(team1)
    elif b > a:
        team1 = team2 #designating team2 to be the new team 1 for the next round
        next_round_teams.append(team2)
    


# -------------------------Let the games begin!-------------------------------------------------->
def first_round(west_conf_teams, east_conf_teams): #First Playoff Round     
    
    for num in range(8): # Defines the first playoff round - East & West Quarterfinals (8 matches total)
    # Western Conference Quarterfinals (4 matches)
    
        if num == 0:
            team1 = west_conf_teams[0] #top ranked team
            team2 = west_conf_teams[7] #bottom ranked team
            print("---------------------------------")
            print("Western Conference Quarterfinals")
            print("\n", team1, "vs.", team2)

            oneround(team1, team2) #execute the above function with these two teams (i.e. make them play)
            auxillary_function(team1, team2) #execute the above function with these two teams

            '''a = oneround(this_series_winner.count(team1)) #after the function is finished, count the number of times team 1 appears in the round1winners series
            #b = oneround(this_series_winner.count(team2)) #same but for team 2
        
            #if a > b:
                #team1 = team1 #designating team1 to be the new team 1 for the Semifinals
                #next_round_teams.append(team1)
            #elif b > a:
                #team1 = team2 #designating team2 to be the new team 1 for the Semifinals
                #next_round_teams.append(team2)'''

        elif num == 1:
            team1 = west_conf_teams[1]
            team2 = west_conf_teams[6]
            print("---------------------------------")
            print("Western Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
            
            '''
            a = round1winners.count(team1) #after the function is finished, count the number of times team 1 appears in the round1winners series
            b = round1winners.count(team2)
            
            if a > b:
                team1 = team1
                next_round_teams.append(team1)
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)'''

        elif num == 2:
            team1 = west_conf_teams[2]
            team2 = west_conf_teams[5]
            print("---------------------------------")
            print("Western Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
            
            '''a = round1winners.count(team1) #after the function is finished, count the number of times team 1 appears in the round1winners series
            b = round1winners.count(team2)
            
            if a > b:
                team1 = team1
                next_round_teams.append(team1)
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)'''

        elif num == 3:
            team1 = west_conf_teams[3]
            team2 = west_conf_teams[4]
            print("---------------------------------")
            print("Western Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
            
            '''a = round1winners.count(team1) #after the function is finished, count the number of times team 1 appears in the round1winners series
            b = round1winners.count(team2)
            
            if a > b:
                team1 = team1
                next_round_teams.append(team1)
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)'''
        
        # Eastern Conference Quarterfinals (4 matches)
        elif num == 4:
            team1 = east_conf_teams[0]
            team2 = east_conf_teams[7]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
            
            '''a = round1winners.count(team1)
            b = round1winners.count(team2)
            
            if a > b:
                team1 = team1
                next_round_teams.append(team1)
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)'''

        elif num == 5:
            team1 = east_conf_teams[1]
            team2 = east_conf_teams[6]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
            
            '''a = round1winners.count(team1)
            b = round1winners.count(team2)
            
            if a > b:
                team1 = team1
                next_round_teams.append(team1)
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)'''

        elif num == 6:
            team1 = east_conf_teams[2]
            team2 = east_conf_teams[5]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
            
            '''a = round1winners.count(team1)
            b = round1winners.count(team2)
            
            if a > b:
                team1 = team1
                next_round_teams.append(team1)
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)'''
               
        elif num == 7:
            team1 = east_conf_teams[3]
            team2 = east_conf_teams[4]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
            
            '''a = round1winners.count(team1)
            b = round1winners.count(team2)
            
            if a > b:
                team1 = team1
                next_round_teams.append(team1)
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)'''
        break


def second_round(): #Second Round
    for num in range(4): # Defines the second playoff round - East & West Semifinals (4 matches total)
        
        #Western Conference Semifinals (2 matches)
        if num == 0:
            team1 = next_round_teams[0]
            team2 = next_round_teams[3]
            print("---------------------------------")
            print("Western Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2) #execute the above function with these two teams
            a = round2winners.count(team1)
            b = round2winners.count(team2)

            if a > b:
                team1 = team1
                next_round_teams.append(team1) #append team1 to the list of Conference Final participants as index[0]
            elif b > a:
                team1 = team2
                next_round_teams.append(team2) #append team2 to the list of Conference Final participants as index[0]

        if num == 1:
            team1 = next_round_teams[1]
            team2 = next_round_teams[2]
            print("---------------------------------")
            print("Western Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            a = round2winners.count(team1)
            b = round2winners.count(team2)

            if a > b:
                team1 = team1
                next_round_teams.append(team1) #append team1 to the list of Conference Final participants as index[1]
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)

        #Eastern Conference Semifinals
        if num == 2:
            team1 = next_round_teams[0]
            team2 = next_round_teams[3]
            print("---------------------------------")
            print("Eastern Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            a = round2winners.count(team1)
            b = round2winners.count(team2)

            if a > b:
                team1 = team1
                next_round_teams.append(team1) #append team1 to the list of Conference Final participants as index[2]
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)

        if num == 3:
            team1 = next_round_teams[1]
            team2 = next_round_teams[2]
            print("---------------------------------")
            print("Eastern Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2) 
            a = round2winners.count(team1)
            b = round2winners.count(team2)

            if a > b:
                team1 = team1
                next_round_teams.append(team1) #append team1 to the list of Conference Final participants as index[3]
            elif b > a:
                team1 = team2
                next_round_teams.append(team2)
        break


def third_round():
    for num in range(2): # Defines the third playoff round - East & West Conference Finals (2 matches total)

        # Western Conference Final
        if num == 0:
            team1 = next_round_teams[0]
            team2 = next_round_teams[1]
            print("---------------------------------")
            print("Western Conference Final")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            a = round3winners.count(team1)
            b = round3winners.count(team2)

            if a > b:
                team1 = team1
                round4teams.append(team1) #append team1 to the list of Stanley Cup Final teams as index[0]
            elif b > a:
                team1 = team2
                round4teams.append(team2) #append team2 to the list of Stanley Cup Final teams as index[0]

        if num == 1:
            team1 = next_round_teams[2]
            team2 = next_round_teams[3]
            print("---------------------------------")
            print("Eastern Conference Final")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            a = round3winners.count(team1)
            b = round3winners.count(team2)

            if a > b:
                team1 = team1
                round4teams.append(team1) #append team1 to the list of Stanley Cup Final teams as index[1]
            elif b > a:
                team1 = team2
                round4teams.append(team2)


# WELCOME TO THE STANLEY CUP FINAL
def final_round():
    team1 = next_round_teams[0]
    team2 = next_round_teams[1]
    print("---------------------------------")
    print("STANLEY CUP FINAL")
    print("\n", team1, "vs.", team2)
    oneround(team1, team2)


select_West_Conf()
select_East_Conf()
first_round(west_conf_teams, east_conf_teams)
second_round()
third_round()
final_round()

print("Thank you for playing.")
input("\n\nPress Enter to exit.")