# take number and give co-prime numbers of that number.     

def cheack_co_prime(a,b):
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
			# print(f"Given number {a} and {b} is not Co-prime :- ")
			pass
		else:
			print(f"Given number {a} and {b} is Co-prime :- ")
			return 1 
	else:   
		min_val = a1 if len(a1) < len(b1) else b1  
		max_val = a1 if len(a1) > len(b1) else b1    
		for i in min_val:
			if i in max_val:
				hcf = i 
		if hcf == 1:
			print(f"Given number {a} and {b} is Co-prime :- ")
			return 1 
		else:
			# print(f"Given number {a} and {b} is not Co-prime :- ")
			pass

cheack = 1 
number = int(input("please enter number"))
l1 = [i for i in range(2,number+1) if number%i == 0]
for i in l1:
	for j in l1:
		if i*j == number:
			c = cheack_co_prime(i,j)
			if c == cheack:
				s = input("Enter any key to exit")
				exit()



