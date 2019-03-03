import time #this imports the time module
import datetime #this imports the datetime module

curr = datetime.datetime.now()
print("Today is " + curr.strftime("%B") + " " + curr.strftime("%d") + ',' + " " + curr.strftime("%Y"))
print(" ")

#Data Entry---------------------------------------------
sentence = input("Enter a word or sentence: ")
time.sleep(1) #wait one second
print("You entered:", sentence)

#Analysis------------------------------------------------
span = len(sentence)
numwords = sentence.count(' ') + 1
#the above code counts the number of spaces in the sentence, starting from the first character of the first word (0) and stopping at the last character of the last word (span), plus one, because there is no space after the end of the sentence


time.sleep(2)

print("Your entry has", numwords, "words and is", span, "characters in length.")

time.sleep(2)

print("\nNow we're going to translate your verbiage into Pig Latin.")
time.sleep(2)

for x in range(2):
    print(" ")  #prints blank space two times

#DataCleaning------------------------------------
sentence = sentence.replace(',', '') #removes commas by replacing them with an empty character
sentence = sentence.replace('.', '') #removes periods by replacing them with an empty character
sentence = sentence.replace('-', '') #removes dashes
sentence = sentence.replace(';', '') #removes semicolons
sentence = sentence.replace(':', '') #removes colons
sentence = sentence.replace('?', '') #removes question marks
sentence = sentence.replace('!', '') #removes exclamation points
sentence = sentence.split(' ') # break down sentence into individual words using a space as the delimiter

newsentence = "" #empty string to store a new sentence

#Reporting------------------------------------------------------------------------------------------------------------------------
for word in sentence: # this loop prints each word starting with the second character and appends the first character and "ay" to the end of the word until the last word has been changed
    if len(word) >=2:
        word = word + word[0] + "ay" #modify the word to append the first character (word[0]) and "ay" to the end
        word = word[1: ] #then modifying the modified word to start with the second character (word[1]) and continue to the last character (word[])
        print(word.lower(), end = ' ') #print the new Pig Latin word in lowercase plus a space at the end, and append the next word to this word until the loop is finished
        #newsentence = newsentence + word.lower() #append new word to the new sentence
        time.sleep(0.75)
        
    elif len(word) == 1:
        print(word, end = ' ') #if a word is a single character then just print it out with a space at the end and keep going until the loop is finished

input("\n\nPress Enter to exit.")