# Python Program for How to check if a given number is Fibonacci number?   
'''
n = int(input("Please enter number to cheack The number  is Fibonacci or not"))
res = (n-2)+(n-1) 
print(f"Number is Fibonacci{n}") if res == n else print(f"Number is not Fibonacci{n}")
'''
# -----------------------------------------------------------------------------------------
n = int(input("Please enter number to cheack The number  is Fibonacci or not :- "))
r_ange = n*2
a,b = -1,1
for i in range(r_ange):
    res = a+b 
    if res == n:
        print("yes")
        break
    a,b = b,res 
else:
    print('No')
