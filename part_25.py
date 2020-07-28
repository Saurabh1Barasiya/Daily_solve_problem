 # Program to find out least common multiple (LCM).
# suppose 3 and 4 is numbers so 
# multiple of 3 ----> 3,6,9,12,15,18,21,24,27,30
# multiple of 4 ----> 4,8,12,16,20,24,28,32,36,40 

# _______________________________________________________________________________________________________

# a,b = eval(input("Enter two numbers : "))
# for i in range(1,(a*b)+1):
#    if i%a == 0 and i%b == 0:
#        print("LCM is",i)
#        break


# a,b = eval(input("Enter two numbers : "))
# print([i for i in range(1,(a*b)+1) if i%a == 0 and i%b == 0][0])

# _______________________________________________________________________________________________________________________

a,b = eval(input("Enter Two numbers separated by (,) comm :-  "))
print("LCM is ",[i for i in range(1,(a*b)+1) if i%a == 0 and i%b == 0][0])
