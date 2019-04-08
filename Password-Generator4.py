from random import randrange
from time import sleep
password = [] #empty list to store created password
random_character = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "/", ",", ".", "<", ">", "?", ";", ":", "\\") #tuple of password character choices

def get_info(password):
    length = input("\nHow many characters for your password?: ")
    length = int(length)
    run_loop(length, password) #calls the run_loop function and passes the length and empty password to it

def run_loop(length, password):
    num = 1
    while num <= length: #a loop that executes while num is less than or equal to the length of the password
        x = randrange(65) #picks a random number between zero and 64, inclusive
        password.append(random_character[x]) #locates the character in the tuple at the corresponding key number and appends the character to the list
        num += 1 #increments counter by 1
    
    output(length, password) #calls the output function and passes the length and new password to it

def output(length, password):
    password = ''.join(map(str, password)) #removes list formatting by converting the list to a string and then replacing the brackets and commas with null values
    sleep(1)
    print("\nYour new password is: ", password)
    sleep(0.5)
    sat = input("Are you satisfied (Y/N)?: ")

    if sat == "N" or sat == "n":
        password = [] #resets password to empty
        get_info(password) #calls the get_info function and passes the empty password to it

    else:
        input("\n\n Press enter key to exit.")

get_info(password) #calls the get_info function and passes the empty password to it