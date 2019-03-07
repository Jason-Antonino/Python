import time #this imports the time module
import datetime #this imports the datetime module

curr = datetime.datetime.now()
print("Today is " + curr.strftime("%B") + " " + curr.strftime("%d") + ',' + " " + curr.strftime("%Y"))


#Data Entry--------------------------------------------->
sentence = input("Enter a word or sentence: ")
time.sleep(1) #wait one second
print("\nYou entered: " + sentence + ".")


#Analysis------------------------------------------------>
span = len(sentence)
numwords = sentence.count(' ') + 1
#this counts the number of spaces in the sentence, starting from the first character of the first word (0) and stopping at the last character of the last word (span), plus one, because there is no space after the end of the sentence


#First Outputs------------------------------------------->
time.sleep(2)
print("\nYour entry has", numwords, "words and is", span, "characters in length.")
time.sleep(2)

print("\nNow we're going to translate your verbiage into Pig Latin.")
time.sleep(2)

for x in range(2):
    print(" ")  #prints single blank space on single line two times


#DataCleaning-------------------------------------------->
sentence = sentence.replace(',', '') #removes commas by replacing them with an empty character
sentence = sentence.replace('.', '') #removes periods by replacing them with an empty character
sentence = sentence.replace('-', '') #removes dashes
sentence = sentence.replace(';', '') #removes semicolons
sentence = sentence.replace(':', '') #removes colons
sentence = sentence.replace('?', '') #removes question marks
sentence = sentence.replace('!', '') #removes exclamation points
sentence = sentence.split(' ') # break down sentence into individual words using a space as the delimiter


#Reporting----------------------------------------------->
for word in sentence: # this loop prints each word starting with the second character and appends the first character and "ay" to the end of the word until the last word has been changed
    if word == sentence[-1]: #last word in sentence
        if len(word) >=2: #if a word is two or more characters in length
            word = word[1: ] + word[0] + "ay" #modify the word to append the first character (word[0]) and "ay" to the end, and making the word begin with the second character (word[1]) and end with the last character
            print(word.lower() + '.') #print the new Pig Latin word in lowercase plus a period at the end
            time.sleep(0.75)
        elif len(word) == 1:
            print(word + '.')
            time.sleep(0.75)
        break
    
    if len(word) >=2: #if a word is two or more characters in length
        word = word[1: ] + word[0] + "ay" #modify the word to append the first character (word[0]) and "ay" to the end, and making the word begin with the second character (word[1]) and end with the last character
        print(word.lower(), end = ' ') #print the new Pig Latin word in lowercase plus a space at the end, and append the next word to this word until the loop is finished
        time.sleep(0.75)
        
    elif len(word) == 1:
        print(word, end = ' ') #if a word is a single character then just print it out with a space at the end and keep going until the loop is finished
        time.sleep(0.75)

input("\n\nPress Enter to exit.")