'''
        *
      *   *       
    *   *   *     
  *   *   *   *   
*   *   *   *   *

'''



check = True
for i in range(1,6):
    for j in range(1,10):
        if (j >= (6-i)) and (j <= 4+i) and check: 
            print("*",end=' ')  
        else:     
            print(" ",end=' ') 
        if check == True: 
            check = False 
        elif check == False: 
            check = True  
    print("")
