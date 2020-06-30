# Python Program for factorial of a number
number = int(input("Please enter a number"))
fact = 1
for i in range(1,number+1):
	fact = fact * i

print(f"Factorial of given number is {fact}") 