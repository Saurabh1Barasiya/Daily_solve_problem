# Formula to calculate compound interest annually is given by:
# Compound Interest = P(1 + R/100) t
# Where,
# P is principle amount
# R is the rate and
# T is the time span
principle_amount = int(input("Please enter principle amount :- ")) 
time = int(input("Please enter time span :- "))
rate = float(input("Please enter rate :- ")) 
compound_interest = principle_amount * (1 + (rate /100))**time 
print(f"compound_interest is {compound_interest}") 
# print(1200 * (1 + (5.4/100))**2)