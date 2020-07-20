# Try to find the mean, maean is average.
l = eval(input("Please enter array elements seprated by comma:-  "))
sum = 0
for i in l:
    sum += i
print('Mean of the giviens number is',int(sum/len(l)))
