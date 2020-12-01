# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

# Input Format

# The first line contains the first name, and the second line contains the last name.

# Constraints

# The length of the first and last name ≤ 10.

# Output Format

# Print the output as mentioned above.

def print_full_name(a, b):
    if len(a) <= 10 and len(b) <= 10:
        print(f"Hello {a} {b}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)