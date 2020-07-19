# Python Program for cube sum of first n natural numbers
n = int(input('Please enter N range value :- '))
qube = [i**3 for i in range(1,n+1)]
sum = 0 
for num in qube:
    sum += num
print(f"qube of sum is {sum}")
