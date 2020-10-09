# int_val = 4
# str_val = 'GeeksforGeeks'
# flt_val = 24.56
  
# Printing the hash values. 
# Notice Integer value doesn't change 
# You'l have answer later in article. 
# print ("The integer hash value is : " + str(hash(int_val))) 
# print ("The string hash value is : " + str(hash(str_val))) 
# print ("The float hash value is : " + str(hash(flt_val))) 



'''  
  Task
  Given an integer,n ,and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t).
  Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

  Input Format

  The first line contains an integer,n, denoting the number of elements in the tuple.
  The second line contains n space-separated integers describing the elements in tuple t.

  Output Format

  Print the result of hash(t).

  Sample Input 0

  2
  1 2

  Sample Output 0

  3713081631934410656
'''


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)  
    print(hash(t))
