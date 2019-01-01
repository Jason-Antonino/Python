from time import sleep

import locale
locale.setlocale(locale.LC_ALL, '')


# this tuple covers the first 20 cases done in a single month
case_values = (491, 491, 491, 491, 491, 491, 491, 491, 491, 516, 516, 516, 516, 516, 563, 563, 563, 563, 563, 563)
regularpay1 = 1227.50
regularpay2 = 1227.50


# these variables influence the mid-month paycheck
last23days = int(input("Enter total whole number of cases finished from the 1st through the 23rd of last month: "))
comp1 = int(input("Enter number of cases completed from the 24th through the last day of last month: "))
subclins1 = float(input("Enter subclin decimal count for last month, if any: "))
comp2 = int(input("Enter number of cases completed from the 1st thru 8th day of this month: "))
last_month_total = float(last23days + comp1 + subclins1)


# these variables influence the month-end paycheck
comp3 = int(input("Enter number of cases completed from the 9th thru 15th of this month: "))
comp4 = int(input("Enter number of cases completed or will be completed from the 16th thru 23rd of this month: "))
comp5 = int(input("Enter predicted number of cases you'll complete between the 24th and last day of this month: "))
subclins2 = float(input("Enter subclin decimal count this month, if any: "))
these23days = float(comp2 + comp3 + comp4 + subclins2)
this_month_total = float(comp2 + comp3 + comp4 + comp5 + subclins2)


# converting floating numbers to integers
ilast_month_total = int(last_month_total)
ithese23days = int(these23days)
isubclins1 = int(subclins1)
isubclins2 = int(subclins2)
ithis_month_total = int(this_month_total)


sleep(2)
print("")
print("You completed:", last_month_total, "cases last month, which includes", comp1, "bonus cases and", subclins1, "subclins.")
print("\nYou should have", this_month_total, "cases finished by the end of this month, which includes", (these23days-5), "bonus cases and", subclins2, "subclins.")


# calculate bonus pay 1 (15th day of the current month) using an index agaist the tuple and accounting for any subclins
bonuspay1 = sum(case_values[(last23days):(ilast_month_total)]) + (subclins1 - isubclins1) * case_values[(ilast_month_total)-1]

if comp2 > 5.0: #any cases over 5 in new month is a bonus case
    bonuspay1 += sum(case_values[5:(comp2)])
else:
    pass


# calculate bonus pay 2 (last day of the current month) using an index agaist the tuple and accounting for any subclins
bonuspay2 = sum(case_values[5:(ithese23days)]) + (subclins2 - isubclins2) * case_values[(ithese23days)-1]


# calculating gross income
grosspaycheck1 = regularpay1 + bonuspay1
grosspaycheck2 = regularpay2 + bonuspay2
gross_income = grosspaycheck1 + grosspaycheck2


# program outputs
sleep(2)
print("Your mid-month gross paycheck is: ", locale.currency(grosspaycheck1))
sleep(1)
print("Your month-end gross paycheck is: ", locale.currency(grosspaycheck2))
sleep(1)
print("For a grand total earned of: ", locale.currency(gross_income), "this month, which equates to", locale.currency(gross_income*12), "per year.")
sleep(1)
print("\nDone.")
input("\n\nPress Enter key to exit.")