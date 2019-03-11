print("Best of Seven NHL Playoff Series")

from time import sleep
from random import randrange


west_conf_teams = [] #empty list to store initial West Conf team names
east_conf_teams = [] #empty list to store initial East Conf team names
next_round_teams = [] #creates an empty list to store names of teams to compete in the next round


def select_West_Conf(): # Select 8 West Conference Teams--------------------
    west_conf_teams = [] #empty list to store team names
    print("\nEnter Names of 8 Western Conference Teams to participate in First Round")
    for x in range(8): #8 iterations adding team names to list
        team = input("Enter team name: ")
        west_conf_teams.append(team)
    print(west_conf_teams)    
    return west_conf_teams[:]

def select_East_Conf(): # Select 8 East Conference Teams--------------------
    east_conf_teams = [] #empty list to store team names
    print("\nEnter Names of 8 Eastern Conference teams to participate in the first round")
    for x in range(8): #8 iterations adding team names to list
        team = input("Enter team name: ")
        east_conf_teams.append(team)
    print(east_conf_teams)    
    return east_conf_teams[:]


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
    
    return (team1, team2, next_round_teams)


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

        elif countb == 4: #Team2 wins 4 games first
            print(team2, "win the series", countb, "games to", counta)
            this_series_winner.append(team2) #append team2 to list starting at index[0]
            sleep(2)
            
    auxillary_function(team1, team2, this_series_winner)


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

        elif num == 1:
            team1 = west_conf_teams[1]
            team2 = west_conf_teams[6]
            print("---------------------------------")
            print("Western Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)

        elif num == 2:
            team1 = west_conf_teams[2]
            team2 = west_conf_teams[5]
            print("---------------------------------")
            print("Western Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)

        elif num == 3:
            team1 = west_conf_teams[3]
            team2 = west_conf_teams[4]
            print("---------------------------------")
            print("Western Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
        
        # Eastern Conference Quarterfinals (4 matches)
        elif num == 4:
            team1 = east_conf_teams[0]
            team2 = east_conf_teams[7]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            
        elif num == 5:
            team1 = east_conf_teams[1]
            team2 = east_conf_teams[6]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            
        elif num == 6:
            team1 = east_conf_teams[2]
            team2 = east_conf_teams[5]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
                           
        elif num == 7:
            team1 = east_conf_teams[3]
            team2 = east_conf_teams[4]
            print("---------------------------------")
            print("Eastern Conference Quarterfinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            
        second_round(next_round_teams)


def second_round(next_round_teams): #Second Round
    for num in range(4): # Defines the second playoff round - East & West Semifinals (4 matches total)
        
        #Western Conference Semifinals (2 matches)
        if num == 0:
            team1 = next_round_teams[0]
            team2 = next_round_teams[3]
            print("---------------------------------")
            print("Western Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2) #execute the above function with these two teams
            auxillary_function(team1, team2)

        elif num == 1:
            team1 = next_round_teams[1]
            team2 = next_round_teams[2]
            print("---------------------------------")
            print("Western Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)

        #Eastern Conference Semifinals
        elif num == 2:
            team1 = next_round_teams[0]
            team2 = next_round_teams[3]
            print("---------------------------------")
            print("Eastern Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)

        elif num == 3:
            team1 = next_round_teams[1]
            team2 = next_round_teams[2]
            print("---------------------------------")
            print("Eastern Conference Semifinals")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2) 
            auxillary_function(team1, team2)
        
        third_round(next_round_teams)


def third_round(next_round_teams):
    for num in range(2): # Defines the third playoff round - East & West Conference Finals (2 matches total)

        # Western Conference Final
        if num == 0:
            team1 = next_round_teams[0]
            team2 = next_round_teams[1]
            print("---------------------------------")
            print("Western Conference Final")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)

        elif num == 1:
            team1 = next_round_teams[2]
            team2 = next_round_teams[3]
            print("---------------------------------")
            print("Eastern Conference Final")
            print("\n", team1, "vs.", team2)
            oneround(team1, team2)
            auxillary_function(team1, team2)
                
        final_round(next_round_teams)


# WELCOME TO THE STANLEY CUP FINAL
def final_round(next_round_teams):
    team1 = next_round_teams[0]
    team2 = next_round_teams[1]
    print("---------------------------------")
    print("STANLEY CUP FINAL")
    print("\n", team1, "vs.", team2)
    oneround(team1, team2)


def main():
    select_West_Conf()
    select_East_Conf()
    first_round(west_conf_teams, east_conf_teams)


main()
print("Thank you for playing.")
input("\n\nPress Enter to exit.")