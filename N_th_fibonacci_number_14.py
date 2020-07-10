# Python Program for n-th Fibonacci number
n_th = int(input("Please enter number :- "))
l = [0,1]
a = 0
b = 1
for i in range(n_th):
    c = a+b 
    l.append(c)
    a = b
    b = c 
print(f"{n_th} number of Fibonacci series is {l[n_th]}")
