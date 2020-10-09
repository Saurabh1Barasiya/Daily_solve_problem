
'''
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.


############### input format #########################
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

############## output format #########################
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]




'''





N = int(input()) 
l1 = []
for _ in range(N):
    l2 = input().split(' ')  
    if l2[0] == 'insert':
       l1.insert(int(l2[1]),int(l2[2]))
    elif l2[0] == 'print':
        print(l1)
    elif l2[0] == 'remove':
        l1.remove(int(l2[1]))
    elif l2[0] == 'append':
        l1.append(int(l2[1])    )
    elif l2[0] == 'sort':
        l1.sort()  
    elif l2[0] == 'pop':
        l1.pop() 
    elif l2[0] == 'reverse':
        l1.reverse()
