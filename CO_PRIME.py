# given two number is co-prime or not.
a = int(input("Please enter frist number :- "))
b = int(input("Please enter secound number :- ")) 
hcf = 1 
# so frist we make factors of given number    
a1 = [i for i in range(2,a+1) if a%i ==0]
b1 = [i for i in range(2,b+1) if b%i ==0]   
if len(a1)==1 and len(b1) ==1: 
	i = a1[0]
	j = b1[0]     
	min = i if i < j else j     
	max = i if i > j else j     
	if max%min == 0:
		print(f"Given number {a} and {b} is not Co-prime :- ")
	else:
		print(f"Given number {a} and {b} is Co-prime :- ")
else:   
	min_val = a1 if len(a1) < len(b1) else b1  
	max_val = a1 if len(a1) > len(b1) else b1    
	for i in min_val:
		if i in max_val:
			hcf = i 
	if hcf == 1:
		print(f"Given number {a} and {b} is Co-prime :- ")
	else:
		print(f"Given number {a} and {b} is not Co-prime :- ")


