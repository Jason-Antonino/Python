from random import randrange
from time import sleep
password = [] #empty list to store created password
random_character = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f", 16:"g", 17:"h", 18:"i", 19:"j", 20:"k", 21:"l", 22:"m", 23:"n", 24:"o", 25:"p", 26:"q", 27:"r", 28:"s", 29:"t", 30:"u", 31:"v", 32:"w", 33:"x", 34:"y", 35:"z", 36:"`", 37:"~", 38:"!", 39:"@", 40:"#", 41:"$", 42:"%", 43:"^", 44:"&", 45:"*", 46:"(", 47:")", 48:"-", 49:"_", 50:"=", 51:"+", 52:"[", 53:"]", 54:"{", 55:"}", 56:"|", 57:"/", 58:",", 59:".", 60:"<", 61:">", 62:"?", 63:";", 64:":", 65:"\\"} #dictionary of password character choices

def get_info(password):
    length = input("How many characters for your password?: ")
    length = int(length)
    run_loop(length, password) #calls the run_loop function

def run_loop(length, password):
    for num in range(length): #starts a loop that will repeat for each character, the number of loops equal to the length of the password
        x = randrange(66) #picks a random number between zero and 65, inclusive
        password.append(random_character[x]) #locates the character in the dictionary at the corresponding key number and appends the character to the list
    output(length, password)

def output(length, password):
    password = ''.join(map(str, password)) #removes list formatting by converting the list to a string and then replacing the brackets and commas with nothing
    sleep(1)
    print("Your new password is: ", password)
    sleep(0.5)
    sat = input("Are you satisfied (Y/N)?: ")

    if sat == "N" or sat == "n":
        password = [] #resets password to empty
        get_info(password)

    else:
        input("\n\n Press enter key to exit.")

get_info(password)