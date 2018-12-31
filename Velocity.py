import time

print("kph", "knots", "mph", "feet/sec")
time.sleep(2)
for kph in range(0, 1000, 10):
    mph = int(kph*0.62)
    kts = int(kph*0.62*1/1.15)
    fps = int(kph*0.62*88/60)
    print(kph, "kph", kts, "knots", mph, "mph", fps, "feet/sec")
    time.sleep(0.15)
    

print("\n...................................................")


time.sleep(4)

cel = int(-273)

for cel in range (-273,501,25):
    fah = int((cel * 1.8) + 32)
    kel = int(cel + 273)
    print(cel, "Celcius", fah, "Fahrenheit", kel, "Kelvin")
    time.sleep(0.25)

print("\n...................................................")
time.sleep(4)

mortgage = int(122500)
sale_price = int(input("Sale price? "))

commission = int(0.055 * sale_price)
sale_costs = int(0.01*sale_price)
print("\n...................................................")

time.sleep(3)
print("Sale price of $", sale_price)
time.sleep(1)
print("\nwith a total cost of sale of $",  commission + sale_costs)
time.sleep(1)
print("\nand a mortgage payoff of $", mortgage)
time.sleep(2)
print("\nresults in a net payout of: $", sale_price - commission - sale_costs - mortgage)

print("\n...................................................")
time.sleep(3)

input("\n\nPress any key to exit.")