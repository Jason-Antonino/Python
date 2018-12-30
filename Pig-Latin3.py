import time #this imports the time module
import datetime #this imports the datetime module

curr = datetime.datetime.now()
print("Today is ", curr.strftime("%B"), curr.strftime("%d"), ',', curr.strftime("%Y"))

#Data Entry---------------------------------------------
sentence = input("Enter a word or sentence: ")
time.sleep(1) #wait one second
print("You entered: " + sentence + ".")

#Analysis------------------------------------------------
span = len(sentence)
numwords = sentence.count(' ', 0, span)+1
"""
this counts the number of spaces in the sentence starting from the first character of the first word and stopping at the last character of the last word, plus one, because there is no space after the end of the sentence
"""

time.sleep(2)

print("Your entry has", numwords, "words and is", span,"characters in length.")

time.sleep(2)

print("\nNow we're going to translate your verbiage into Pig Latin.")
time.sleep(2)

for x in range(0, 2):
    print(" ")  #prints blank space two times

#DataCleaning------------------------------------
sentence = sentence.replace(',', '') #removes commas
sentence = sentence.replace('.', '') #removes periods
sentence = sentence.split(' ') # break down sentence into individual words using a space as the delimiter

#Reporting------------------------------------------------------------------------------------------------------------------------
for word in sentence: # this loop prints each word starting with the second character and appends the first character and "ay" to the end of the word until the last word has been changed
    if len(word) >=2:
        word = word + '%say' % (word[0]) #modify the word to append the first character (word[0]) and "ay" to the end
        word = word[1: ] #then modifying the modified word to start with the second character (word[1]) and continue to the last character (word[])
        print(word.lower(), end = ' ') #print the new Pig Latin word in lowercase plus a space at the end, and append the next word to this word until the loop is finished
        time.sleep(0.5)
        
    elif len(word) == 1:
        print(word, end = ' ') #if a word is a single character then just print it out with a space at the end and keep going until the loop is finished

    else:
        pass

input("\n\nPress Enter to exit.")