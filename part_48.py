# def case1(s):
    
#     s = ''+ s +''
#     if  s.isalnum():
#         print(True)
#     else:
#         print(False)   

# def case2(s):
#     l1 = ['A' ,'B' ,'C' ,'D', 'E' ,'F' ,'G' ,'H', 'I','J' 'K', 'L', 'M' ,'N', 'O' ,'P', 'Q' 'R' ,'S' ,'T','V','W' ,'X' ,'Y' ,'Z']
#     l2 = ['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','w','r','s','t','v','w','x','y','z']         
#     for word in s:
#         if word in l1 or word in l2:
#             print(True)
#             break
#     else:
#         print(False)


# def case3(s):
#     if s.isalnum():
#         print(True)
#     else:
#         print(False)  


# def case4(s):
#     l2 = ['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','w','r','s','t','v','w','x','y','z']
#     for word in s:
#         if word in l2:
#             print(True)
#             break 
#     else:
#         print(False) 



# def case5(s):
#     l1 = ['A' ,'B' ,'C' ,'D', 'E' ,'F' ,'G' ,'H', 'I','J' 'K', 'L', 'M' ,'N', 'O' ,'P', 'Q' 'R' ,'S' ,'T','V','W' ,'X' ,'Y' ,'Z']
#     for word in s:
#         if word in l1:
#             print(True)
#             break   
#     else:
#         print(False) 



if __name__ == '__main__':
    s = input()
    if len(s) > 0 and len(s) < 1000:
#         case1(s)
#         case2(s)
#         case3(s)
#         case4(s)
#         case5(s) 
          for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
            print(any(method(c) for c in s))   
   




      
        

        
