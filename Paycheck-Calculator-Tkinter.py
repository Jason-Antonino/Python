import tkinter
from time import sleep
import locale
locale.setlocale(locale.LC_ALL, '')

# this tuple covers the first 20 cases done in a single month; minimum gross income is 2455 per month, based on 5 cases finished
case_values = (491, 491, 491, 491, 491, 491, 491, 491, 491, 516, 516, 516, 516, 516, 563, 563, 563, 563, 563, 563)
regularpay1 = 1227.50
regularpay2 = 1227.50

window = tkinter.Tk()
window.title("GPS Paycheck Calculator")

label = tkinter.Label(window, text = "Welcome, User.").grid(row = 0)
label2 = tkinter.Label(window, text = "This program will calculate your mid-month and month-end paychecks for the current month.").grid(row = 1)
label3 = tkinter.Label(window, text = "Please answer the following 12 questions:").grid(row = 2)

# creating 2 frames TOP and BOTTOM
#top_frame = tkinter.Frame(window).grid()
#bottom_frame = tkinter.Frame(window).grid()


#Program Inputs----------------------------------->
question1 = tkinter.Label(window, text = "1. Enter average gross monthly income over the last 90 days:").grid(row = 3, column = 0)
entry1 = tkinter.Entry(window, text = " ").grid(row = 3, column = 1)
button1 = tkinter.Button(window, text = "Enter").grid(row = 3, column = 2)

question2 = tkinter.Label(window, text = "2. Enter total whole number of cases finished from the 1st through the 23rd of last month:").grid(row = 4, column = 0)
entry2 = tkinter.Entry(window, text = " ").grid(row = 4, column = 1)
button2 = tkinter.Button(window, text = "Enter").grid(row = 4, column = 2)

question3 = tkinter.Label(window, text = "3. Enter number of cases completed from the 24th through the last day of last month:").grid(row = 5, column = 0)
entry3 = tkinter.Entry(window, text = " ").grid(row = 5, column = 1)
button3 = tkinter.Button(window, text = "Enter").grid(row = 5, column = 2)

question4 = tkinter.Label(window, text = "4. Enter number of PTO days taken between the 24th and last day of last month:").grid(row = 6, column = 0)
entry4 = tkinter.Entry(window, text = " ").grid(row = 6, column = 1)
button4 = tkinter.Button(window, text = "Enter").grid(row = 6, column = 2)

question5 = tkinter.Label(window, text = "5. Enter subclin decimal count for last month, if any:").grid(row = 7, column = 0)
entry5 = tkinter.Entry(window, text = " ").grid(row = 7, column = 1)
button5 = tkinter.Button(window, text = "Enter").grid(row = 7, column = 2)

question6 = tkinter.Label(window, text = "6. Enter number of cases completed from the 1st thru 8th day of this month:").grid(row = 8, column = 0)
entry6 = tkinter.Entry(window, text = " ").grid(row = 8, column = 1)
button6 = tkinter.Button(window, text = "Enter").grid(row = 8, column = 2)

question7 = tkinter.Label(window, text = "7. Enter number of PTO days taken between the 1st and 8th of this month:").grid(row = 9, column = 0)
entry7 = tkinter.Entry(window, text = " ").grid(row = 9, column = 1)
button7 = tkinter.Button(window, text = "Enter").grid(row = 9, column = 2)

question8 = tkinter.Label(window, text = "8. Enter number of cases completed from the 9th thru 15th of this month:").grid(row = 10, column = 0)
entry8 = tkinter.Entry(window, text = " ").grid(row = 10, column = 1)
button8 = tkinter.Button(window, text = "Enter").grid(row = 10, column = 2)

question9 = tkinter.Label(window, text = "9. Enter number of cases completed or will be completed from the 16th thru 23rd of this month:").grid(row = 11, column = 0)
entry9 = tkinter.Entry(window, text = " ").grid(row = 11, column = 1)
button9 = tkinter.Button(window, text = "Enter").grid(row = 11, column = 2)

question10 = tkinter.Label(window, text = "10. Enter number of cases you'll complete between the 24th and last day of this month:").grid(row = 12, column = 0)
entry10 = tkinter.Entry(window, text = " ").grid(row = 12, column = 1)
button10 = tkinter.Button(window, text = "Enter").grid(row = 12, column = 2)

question11 = tkinter.Label(window, text = "11. Enter subclin decimal count through the 23rd of this month, if any:").grid(row = 13, column = 0)
entry11 = tkinter.Entry(window, text = " ").grid(row = 13, column = 1)
button11 = tkinter.Button(window, text = "Enter").grid(row = 13, column = 2)

question12 = tkinter.Label(window, text = "12. Enter number of PTO days taken between the 9th and 23rd of this month:").grid(row = 14, column = 0)
entry12 = tkinter.Entry(window, text = " ").grid(row = 14, column = 1)
button12 = tkinter.Button(window, text = "Enter").grid(row = 14, column = 2)

"""
def function1():
    need code that will, upon clicking, enable the button1 to input the contents of entry1 into the last90 variable below and convert the number to float
    last90 = float(input("1. Enter average gross monthly income over the last 90 days: "))
    PTOvalue = last90 / 21 #estimated value of a single PTO day taken, based on 21 working days in a month

# these variables influence the mid-month paycheck
last23days = int(input("2. Enter total whole number of cases finished from the 1st through the 23rd of last month: "))
comp1 = int(input("3. Enter number of cases completed from the 24th through the last day of last month: "))
PTO1 = int(input("4. Enter number of PTO days taken between the 23rd and last day of last month: "))
subclins1 = float(input("5. Enter subclin decimal count for last month, if any: "))
comp2 = int(input("6. Enter number of cases completed from the 1st thru 8th day of this month: "))
PTO2 = int(input("7. Enter number of PTO days taken between the 1st and 8th of this month: "))
last_month_total = float(last23days + comp1 + subclins1)


# these variables influence the month-end paycheck
comp3 = int(input("8. Enter number of cases completed from the 9th thru 15th of this month: "))
comp4 = int(input("9. Enter number of cases completed or will be completed from the 16th thru 23rd of this month: "))
comp5 = int(input("10. Enter number of cases you'll complete between the 24th and last day of this month: "))
subclins2 = float(input("11. Enter subclin decimal count thru the 23rd of this month, if any: "))
PTO3 = int(input("12. Enter number of PTO days taken between the 9th and 23rd of this month: "))
these23days = float(comp2 + comp3 + comp4 + subclins2)
this_month_total = float(comp2 + comp3 + comp4 + subclins2 + comp5)


# converting floating numbers to integers
ilast_month_total = int(last_month_total)
ithese23days = int(these23days)
isubclins1 = int(subclins1)
isubclins2 = int(subclins2)
ithis_month_total = int(this_month_total)


#Program Summary Report----------------------->
sleep(2)
print("\nSummary Report")
sleep(1)
print("\nYou completed:", last_month_total, "cases last month, which includes", comp1, "bonus cases, and", subclins1, "subclins.")
print("\nYou should have", this_month_total, "cases finished by the end of this month, which includes", (these23days-5), "bonus cases and", subclins2, "subclins.")
print("\nYou took a total of", PTO1+PTO2+PTO3, "PTO days over the last two pay periods.")

# calculate bonus pay 1 (15th day of the current month) using an index against the tuple and accounting for any subclins and/or PTO days taken
bonuspay1 = sum(case_values[(last23days):(ilast_month_total)]) + ((subclins1 - isubclins1) * case_values[(ilast_month_total)-1]) + (PTO1 + PTO2) * PTOvalue

if comp2 > 5.0: #any cases over 5 in the first 8 days of the new month is a bonus case
    bonuspay1 += sum(case_values[5:(comp2)])
else:
    pass


# calculate bonus pay 2 (last day of the current month) using an index agaist the tuple and accounting for any subclins and/or PTO days taken
bonuspay2 = sum(case_values[5:(ithese23days)]) + ((subclins2 - isubclins2) * case_values[(ithese23days)-1]) + PTO3* PTOvalue


# calculating gross income
grosspaycheck1 = regularpay1 + bonuspay1 #15th day of the month
grosspaycheck2 = regularpay2 + bonuspay2 #last day of the month
gross_income = grosspaycheck1 + grosspaycheck2


# program outputs----------------------------->
sleep(1.5)
print("\nYour mid-month gross paycheck is:", locale.currency(grosspaycheck1))
sleep(1)
print("Your month-end gross paycheck is:", locale.currency(grosspaycheck2))
sleep(1.5)
print("\nFor a grand total earned of:", locale.currency(gross_income), "this month, equal to", locale.currency(gross_income*12), "per year.")
sleep(1)
print("\nDone.")
"""
window.mainloop()