num = int(input("Please enter number "))
r = 10 * num    
l = [2]
# count = 0
for i in range(3,r):
	for j in range(2,i+1):    
		if i%j==0:
			break
	if i == j:
	 	l.append(i)
	if len(l) == num:
		break

print("Prime number is ",l)

