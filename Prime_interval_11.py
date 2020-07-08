# Python program to print all Prime numbers in an Interval
# Given two positive integer start and end. 
# The task is to write a Python program toprint all Prime numbers in an Interval.


lower = int(input("Enter the lower limit :- "))
upper = int(input("Enter the upper limit :- "))
if lower == 1:
	lower = 2      
for i in range(lower,upper+1):
	for j in range(2,i+1):
		if i%j==0:
			break
	if i == j:
		print(f"{i} is prime number")
