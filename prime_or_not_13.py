# To cheack number is prime or not
n = int(input("Please enter number to cheack number is prime or not :- "))
if n > 0:
    if n == 1:
        print("Not prime")
    else:
        i = 2  
        while i < n:
            if n % i == 0:
                print("Not prime")
                break
            i+=1
        else:
            print("prime")
else:
    print("Enter positive number")
    
