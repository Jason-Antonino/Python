import time
print("Welcome. I am Ahhnold.")
time.sleep(2)
print("I'm going to ask you a bunch of questions, and I want them answered immediately!")
time.sleep(3)

# Arnold gets the dirt on you and your family
name = input("Who are you? ")
dad = input("Who is ya Daddy? ")
dadjob = input("and what does he do? ")
age = int(input("How old are you? "))
weight = int(input("How much do you weigh? "))
yourjob = input("Who do you work for? ")
time.sleep(2.5)

# Arnold gets nasty
print("I have a headache.")
time.sleep(1)
whyheadache = input("Why do I have a headache? ")

if whyheadache == "tumor":
    print("It's not a tumahhh!")
else:
    print("NO!")
time.sleep(2)

# countdown to zero with one second delay between each number
print("Ahhnold is thinking...")
time.sleep(2)
start = 20
while start>0:
    print(start)
    start = start-1
    time.sleep(1)


# final output with today's date
import datetime 
d = datetime.datetime.today()
print("Today is: ")
print(datetime.date.strftime(d, "%m/%d/%y"))
time.sleep(2)

print("Your name is "+ name +".")
time.sleep(2)
print("Your Daddy is " + dad +" and he works as a " + dadjob + ".")
time.sleep(3)
print("You are", age*12, "months old.")
time.sleep(2)
print("On The Moon, you would weigh", round(weight/6,0), "pounds, and on Mars you'd be", round(weight*0.38,0), "pounds.")
time.sleep(1.5)
print("You work for "+yourjob+".")
time.sleep(1)
print("This is why Ahhnold says get your ass to Mars.")
time.sleep(1)

counter = 6
while counter > 0:
    print("Get your ass to Mars.")
    counter = counter-1
    time.sleep(1)
