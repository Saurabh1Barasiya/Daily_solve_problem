# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa


# Input Format

# A single line containing a string S.

# Constraints

# 0 < len(s) <= 1000

# Output Format

# Print the modified string S.


def swap_case(s):
    if len(s) > 0 and len(s) <= 1000:
        l = []
        capital_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letter = "abcdefghijklmnopqrstuvwxyz"
        for char in s:
            if  char in lower_letter:
                l.append(char.upper())
            else:
                l.append(char.lower())     
        return ''.join(l)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

