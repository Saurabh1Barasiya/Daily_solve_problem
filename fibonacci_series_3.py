# Here we generate fibonacci series.
n = int(input("Please enter number that you would like to generate fibonacci series "))
a = 0
b = 1
l = [0,1]
while True:
	c = a + b
	l.append(c)
	a = b
	b = c 
	if len(l) == n:
		break
print(l)
