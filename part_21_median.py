# Try to find median
l = eval(input("Please enter element seprated by comma :-  "))
l.sort()
if len(l)%2==0:
    index =  int(len(l)/2)
    print(f"Median value is : {(l[index-1] + l[index])/2}")
else:
    index = int(len(l)/2)
    print("Median value is : ",l[index])
