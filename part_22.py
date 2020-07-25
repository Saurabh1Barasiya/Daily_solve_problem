numbers = eval(input("Enter list items : "))
unique_numbers = set(numbers)
d = {}

for i in unique_numbers:
    d[i] = numbers.count(i)

for key in list(d):
    if d[key] == 1:
        del d[key]

print(f"There is {len(d)} Mode")
for key,value in d.items():
    print(f"value {key} and its count {value}")
