from time import sleep
import locale
import calendar 
locale.setlocale(locale.LC_ALL, '')

# This tuple covers the first 20 cases done in a single month; minimum gross income is 2455 per month, based on 5 cases finished
case_values = (491, 491, 491, 491, 491, 491, 491, 491, 491, 516, 516, 516, 516, 516, 563, 563, 563, 563, 563, 563)
regularpay1 = 1227.50
regularpay2 = 1227.50


# Print Calendar
print("Welcome to the GPS Paycheck Calculator")
sleep(2)

year = int(input("\nEnter year as 4-digit number: "))
month1 = int(input("Enter last month as 1 or 2-digit number: "))
month2 = int(input("Enter current month as 1 or 2-digit number: "))

#Correlating month numbers to month names (index numbers 0 through 11, inclusive)
list_of_months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")


def calendar_print(year, month1, month2):
    print ("")
    print (calendar.month(year, month1))
    print ("")
    print (calendar.month(year, month2))
    print ("")
    return(month1, month2)
    
calendar_print(year, month1, month2) #calls the above function using the 3 earlier inputs

month1name = (list_of_months[(month1)-1]) #converts the last month number to the month name
month2name = (list_of_months[(month2)-1]) #same but for the current month

sleep(1)


#PROGRAM INPUTS------------------------------------------------------->
print("Please answer the following 12 questions. If you do not know the answer, give your best guess. No blank fields are allowed.")
sleep(2)

last90 = float(input("1. Enter average gross monthly income over the last 90 days: "))
PTOvalue = (last90 / 21) #estimated value of a single PTO day taken, based on average of 21 working days in a month


# these variables influence the mid-month paycheck
last23days = int(input("2. Enter total whole number of cases finished from the 1st through the 23rd of last month: "))
comp1 = int(input("3. Enter number of cases completed from the 24th through the last day of last month: "))
PTO1 = int(input("4. Enter number of PTO days taken between the 24th and the last day of last month: "))
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


#PROGRAM SUMMARY REPORT---------------------------------------------->
sleep(2)
print("")
for x in range(20):
    print("-", end='')
print("\nSUMMARY REPORT")
for x in range(20):
    print("-", end='')
sleep(1)

print("\nYou completed:", last_month_total, "cases in", month1name, ", which includes", comp1, "bonus cases, and", subclins1, "subclins.")
sleep(2)
print("\nYou should have", this_month_total, "cases finished by the end of", month2name, ", which includes", (these23days-5), "bonus cases and", subclins2, "subclins.")
sleep(2)
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


#FINAL OUTPUTS----------------------------------------------------->
sleep(2)
print("\nYour mid-month gross paycheck is:", locale.currency(grosspaycheck1))
sleep(2)
print("Your month-end gross paycheck is:", locale.currency(grosspaycheck2))
sleep(2)
print("\nFor a grand total earned of:", locale.currency(gross_income), "this month, equal to", locale.currency(gross_income*12), "per year.")
sleep(1.5)
input("\n\nPress Enter key to exit.")


"""
NOTES: the first pay period is from the 24th of last month through the 8th day of this month. The second pay period is from the 9th through the 23rd day of this month.

how to figure out how to account for any PTO days taken
PTO is based on last 90 days of income
get average monthly income over last 90 days
then divide by about 21 to get value of one day of work
"""