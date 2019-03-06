# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:40:08 2019

@author: jason
"""

list1 = []
list2 = []

string = "This is a string of alphanumeric characters that we can manipulate"

sentence = string.split(' ') #creates sentence by splitting string by spaces


for char in string: #iterates through each letter in the string and builds a list of characters
    list1.append(char) #appends the character to the list 1


for word in sentence: #same but builds a list of words
    list2.append(word) #appends the word to the list 2

print("")
print("String:", string[ : ]) #prints the string character by character from beginning to end
print("")
print("String backwards:", string[ : :-1]) #prints each character but from the end to the beginning
print("")
print("Sentence:", sentence) #prints out sentence created earlier
print("")
print("List 1:", list1) #prints the first list one character at a time from beginning to end
print("")
print("List 1 backwards:", list1[ : :-1]) #prints the first list from end to beginning
print("")
print("List 2:", list2) #prints the second list one word at a time from beginning to end
print("")
print("List 2 backwards:", list2[ : :-1]) #prints the second list one word at a time from end to beginning

tuple1 = list1
tuple2 = list2

newlist1 = ''.join(map(str, list1)) #removes list formatting by converting the list to a string and then replacing the brackets and commas with nothing
newlist2 = ' '.join(map(str, list2)) #removes list formatting by converting the list to a string and then replacing the brackets and commas with a single space
print("")
print("List 1 w/o formatting:", newlist1)
print("")
print("List 2 w/o formatting:", newlist2)
print("")
print("Tuple 1:", tuple1)
print("")
print("Tuple 2:", tuple2)
print("")
