# alison heck
# s = '1 w 2 r 3g'
# l = s.split(' ') 
# l2 = []  
# for word in l:
#     l2.append(str.title(word))
# print(' '.join(l2))



# ------------------------------------------------------------------------------------------------------
# s ='1 w 2 r 3g'
# s = 'hello world'

 

# s.isalpha()   -- lagega
# s = 'hello   world  lol'
# s = '5'
# print(s.isalnum())





'''

-----------------------------------WORKING CODE---------------------------------------

def solve(s):
    s = s.replace(s[0],s[0].upper())
    i = 0
    while i < len(s):
        if s[i] == ' ':
            if s[i+1].isalnum() or s[i+1].isalpha():
                print(s[i+1],i)
                print('*****************************')
                s = s.replace(s[i+1],s[i+1].upper(),1)
        i = i + 1
    print(s)    


s = 'hello   world  lol'
# s = '1 w 2 r 3g'
solve(s)
'''

s = list('hello   world  lol')
# s = list('1 w 2 r 3g')
# s = list('hello world')
i = 0
while i < len(s):
    if s[i] == ' ':
        if s[i+1].isalnum() or s[i+1].isalpha():
            s[i+1] = s[i+1].upper() 
    i = i+ 1       
s[0] = s[0].upper()
print(''.join(s))
