# Program to find HCF --> Heigest common factor
# supose number is 12 and 15 so 
# factor of 12 => 2,3,4,6,12
# factor of 15 => 3,5,15
# heigest common factor is 3

# -------------------------------------------------------------------------------------------

# f_no = int(input("Enter frist number :-  "))
# s_no = int(input("Enter secound number :-  "))

# big_no = f_no if f_no > s_no else s_no
# if f_no > s_no:
#     big_no = f_no
# else:
#     big_no = s_no
# for i in range(big_no,0,-1):
#     if f_no%i == 0 and s_no%i == 0:
#         print("HCF is ",i)
#         break

# -------------------------------------------------------------------------------------------------------
# big_no = f_no if f_no > s_no else s_no
# hcf = [i for i in range(big_no,0,-1) if f_no%i == 0 and s_no%i == 0]
# print(f"HCF is {hcf[0]}")

# -----------------------------------------------------------------------------------------------------

# hcf = [i for i in range(f_no if f_no > s_no else s_no,0,-1) if f_no%i == 0 and s_no%i == 0]
# print(f"HCF is {hcf[0]}")

# -------------------------------------------------------------------------------------------------------------


f_no,s_no = int(input("Enter frist number")),int(input("Enter Secound number"))
print(f"HCF is {[i for i in range(f_no if f_no > s_no else s_no,0,-1) if f_no%i == 0 and s_no%i == 0][0]}")
