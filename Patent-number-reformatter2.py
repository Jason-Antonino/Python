from time import sleep #imports the sleep function from the time module
from sys import exit #imports the exit function from the sys module

#gathering user inputs---------------------------
numrefs = int(input("Enter total number of references you wish to cite: ")) #the number or patents/publications in your set
references = [] #references starts out as an empty set

for x in range(numrefs): #this loop inputs a single reference number until it has reached the total number of references in your set that you specified
    reference = input("Type the patent or publication number (without spaces or kind codes): ")
    references.append(reference) #appends each successive reference number to the initially empty references set until it has reached the total number of references in your set that you specified

span = len(references)

sleep(1) #wait one second


#data validation-----------------------------
print ("\nYou entered:", numrefs, "references, as follows:", references) #this prints out references populated by your entries in list format ['reference', 'reference', 'reference', ...]
sleep(1)
corr = input("Is this correct? (Y or N): ")

if corr == "Y":
    pass
if corr == "N":
    print("Sayonara")
    exit() #this exits the program immediately
#else:
   # print("You fail!")
   # exit()

#gathering user preferences--------------- 
punc = input ("\nDo you want your references displayed with or without punctuation? Enter 1 for without characters and 2 for insert characters. ")
sleep(1)
orient = input ("\nDo you want to see a horizontal list, or would you rather have a vertical listing? Enter 1 for horizontal, 2 for vertical.  ")


if punc == "1": #without characters
    
    if orient == "1": # 1 will print out a horizontal list with "OR" in between each
        pref = input("\nHow do you want the references delimited? Enter 1 for 'OR'. Enter 2 for 'or'. Enter 3 for comma. Enter 4 for semicolon. ") #asks for user preference
        print("\nYour list: ")
        if pref == "1":
            for reference in references:
                print(reference, end = " OR ")
            
        elif pref == "2": # 2 will print out a horizontal list with "or" in between each
            for reference in references:
                print(reference, end = " or ")
            
        elif pref == "3": # 3 will print out a horizontal list with a comma in between each
            for reference in references:
                print(reference, end = ", ")
            
        elif pref == "4": # 4 will print out a horizontal list with a semicolon in between each
            for reference in references:
                print(reference, end = "; ")
            
        else:
            print("You need to enter a 1 thru 4, buddy.")
            sleep(0.5)
            print("Try again.")
            sleep(1)
                      
    elif orient == "2": # 2 prints out each item in a vertical list in the order entered
        print("\nYour list: ")
        sleep(1)
        for reference in references: 
            print(reference)
            
    else:
        print("You need to enter 1 or 2, buddy.")
        sleep(1)


elif punc == "2": #with characters

    if orient == "1": #horizontal format
            
        sel = input ("\nHow do you want the references delimited? Enter 1 for 'OR'. Enter 2 for 'or'. Enter 3 for comma. Enter 4 for semicolon. ") #asks for user preference
        print ("\nYour list: ")
            
        if sel == "1":
            for reference in references: #prints out each reference with punctuation
                if reference[0:2] == "US":
                    if len (reference) == 9:
                        print (reference[0:2] + " " + reference[2] + "," + reference[3:6] + "," + reference[6: ], end = " OR ") 
                
                    elif len (reference) == 10:
                        print (reference[0:2] + " " + reference[2:4] + "," + reference[4:7] + "," + reference[7: ], end = " OR ")
                       
                    elif len (reference) == 13:
                        print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = " OR ")

                elif reference[0:3] == "USD":
                    print (reference[0:2] + " " + reference[2: ], end = " OR ")

                elif reference[0:4] == "USRE":
                    print (reference[0:2] + " " + reference[2: ], end = " OR ")

                elif reference[0:2] == "WO":
                    print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = " OR ")

                else:
                        print(reference[0:2] + " " + reference[2: ], end = " OR ")
                
        elif sel == "2":
            for reference in references: #prints out each reference with punctuation
                if reference[0:2] == "US":
                    if len (reference) == 9:
                        print (reference[0:2] + " " + reference[2] + "," + reference[3:6] + "," + reference[6: ], end = " or ") 
                
                    elif len (reference) == 10:
                        print (reference[0:2] + " " + reference[2:4] + "," + reference[4:7] + "," + reference[7: ], end = " or ")
                       
                    elif len (reference) == 13:
                        print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = " or ")

                elif reference[0:3] == "USD":
                    print (reference[0:2] + " " + reference[2: ], end = " or ")

                elif reference[0:4] == "USRE":
                    print (reference[0:2] + " " + reference[2: ], end = " or ")

                elif reference[0:2] == "WO":
                    print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = " or ")
                            
                else:
                    print(reference[0:2] + " " + reference[2: ], end = " or ")

        elif sel == "3":
            for reference in references: #prints out each reference with punctuation
                if reference[0:2] == "US":
                    if len (reference) == 9:
                        print (reference[0:2] + " " + reference[2] + "," + reference[3:6] + "," + reference[6: ], end = ", ") 
                
                    elif len (reference) == 10:
                        print (reference[0:2] + " " + reference[2:4] + "," + reference[4:7] + "," + reference[7: ], end = ", ")
                       
                    elif len (reference) == 13:
                        print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = ", ")

                elif reference[0:3] == "USD":
                    print (reference[0:2] + " " + reference[2: ], end = ", ")

                elif reference[0:4] == "USRE":
                    print (reference[0:2] + " " + reference[2: ], end = ", ")

                elif reference[0:2] == "WO":
                    print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = ", ")
                            
                else:
                    print(reference[0:2]+ " " + reference[2: ], end = ", ")
            
        elif sel == "4":
            for reference in references: #prints out each reference with punctuation
                if reference[0:2] == "US":
                    if len (reference) == 9:
                        print (reference[0:2] + " " + reference[2] + "," + reference[3:6] + "," + reference[6: ], end = "; ") 
                
                    elif len (reference) == 10:
                        print (reference[0:2] + " " + reference[2:4] + "," + reference[4:7] + "," + reference[7: ], end = "; ")
                       
                    elif len (reference) == 13:
                        print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = "; ")

                elif reference[0:3] == "USD":
                    print (reference[0:2] + " " + reference[2: ], end = "; ")

                elif reference[0:4] == "USRE":
                    print (reference[0:2] + " " + reference[2: ], end = "; ")

                elif reference[0:2] == "WO":
                    print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ], end = "; ")

                else:
                    print(reference[0:2]+ " " + reference[2: ], end = "; ")

        else:
            print("You need to enter a 1 thru 4, buddy.")
            sleep(0.5)
            print("Try again.")
            sleep(1)
            
    elif orient == "2": #with characters in vertical format
        print("\nYour list: ")
        for reference in references: #prints out each reference with punctuation
            if reference[0:3] == "USD":
                if len (reference) == 9:
                    print (reference[0:2] + " " + reference[2:6] + "," + reference[6: ])

            elif reference[0:4] == "USRE":
                if len (reference) == 9:
                    print (reference[0:2] + " " + reference[2:6] + "," + reference[6: ])

            elif reference[0:2] == "US":
                if len (reference) == 9:
                    print (reference[0:2] + " " + reference[2] + "," + reference[3:6] + "," + reference[6: ]) 
                
                elif len (reference) == 10:
                    print (reference[0:2] + " " + reference[2:4] + "," + reference[4:7] + "," + reference[7: ])
                       
                elif len (reference) == 13:
                    print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ])

            elif reference[0:2] == "WO":
                print (reference[0:2] + " " + reference[2:6] + "/" + reference[6: ])
                            
            else:
                print(reference[0:2] + " " + reference[2: ])
                
    else:
        print("You need to enter 1 or 2, buddy.")
        sleep(1)
        
input("\n\nPress Enter to exit.")