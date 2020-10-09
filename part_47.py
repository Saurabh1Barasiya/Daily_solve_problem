'''
s = 'ABCDCDC'
sub = 'CDC'
mid = len(s) // 2
print(mid,s[mid])
l1 = list(s)
l1.insert(mid+1,sub[0])
print(''.join(l1).count(sub))




def count_substring(string, sub_string):
    mid = len(string) // 2
    l1 = list(string)
    l1.insert(mid+1,sub_string[0])
    return ''.join(l1).count(sub_string)
'''




'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.


Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints.

1 <=len(string) <= 200 

Each character in the string is an ascii character.


Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC
CDC

Sample Output

2


'''






def count_substring(string, sub_string):
    counter,sum = 0,0
    for _ in range(0, len(string)):
        if matcher(string[counter:(len(sub_string)+counter)], sub_string):
            sum = sum + 1
        counter=counter + 1
    return sum

def matcher(sliced_str, sub_string):
    return sliced_str == sub_string
    
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
