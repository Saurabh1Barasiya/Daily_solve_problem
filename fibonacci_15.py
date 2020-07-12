# Python Program for Fibonacci numbers
n = int(input("Please  enter number that you want to genrate fibonacci series :- "))
a = -1
b =  1 
for i in range(n):
    res = a+b 
    print(res,end=' ')
    a = b
    b = res
