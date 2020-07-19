n = int(input('Please enter N range value :- '))
square = [i**2 for i in range(1,n+1)]
sum = 0 
for num in square:
    sum += num
print(f"suare of sum is {sum}")
