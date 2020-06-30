# Python Program to check Armstrong Number

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

number = int(input("Please enter numer to cheack Armstrong :- "))
str_num = str(number) 
count = 0 
for i in str_num:
	count += 1 
result = 0  
for i in str_num:
	cheack = int(i) ** count 
	result += cheack 
if result == number:
	print(f"Entered number {result} is Armstrong")
else:
	print(f"Entered number {number} is not Armstrong") 
