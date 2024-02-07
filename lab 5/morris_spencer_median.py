"""
    Author:"Spencer Morris"
    Write a program that takes in three integers and outputs the median value (not the largest or smallest
    value).
"""

# take ints an inputs
int_1 = int(input("Please enter the first integer: "))
int_2 = int(input("Please enter the second integer: "))
int_3 = int(input("Please enter the third integer: "))

# find the median; i.e. find the middle number
# 3 if statements that check if 1 <= 2 <= 3, etc. must be <= because there could be duplicate numbers
# check int 1
if int_2 <= int_1 <= int_3 or int_3 <= int_1 <= int_2:
    print(f"The median number is {int_1}")
# check int 2
elif int_1 <= int_2 <= int_3 or int_3 <= int_2 <= int_1:
    print(f"The median number is {int_2}")
# check int 3
elif int_1 <= int_3 <= int_2 or int_2 <= int_3 <= int_1:
    print(f"The median number is {int_3}")