# Python Program for Program to find area of a circle
# Area of a circle can simply be evaluated using following formula.
# Area = pi * r2
# where r is radius of circle 
import math
radius = float(input("Please enter the radius of the circle :- "))  
a_o_c = math.pi * radius**2 
print("Area of circle is %.2f" % a_o_c)