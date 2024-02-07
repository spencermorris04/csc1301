"""
    Author: "Spencer Morris"
    Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and
    evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the
    primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90.
    Your program must also be able to detect invalid highway numbers. Note: 200 is not a valid auxiliary
    highway because 00 is not a valid primary highway number

    Given a highway number, indicate whether it is a primary, auxiliary highway or an invalid highway
    number. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs
    north/south or east/west.
"""

# take the highway number as input, handling text input errors
try:
  highway_number = int(input("Please enter an interstate number: "))
except ValueError:
  print("Invalid: Interstate numbers cannot include letters...")
else:
  # determine if the highway number is primary, auxillary, or invalid
  # the highway number is primary if it is between 1 and 90
  if 1 <= highway_number <= 90:
    # determine if the highway goes north/south; i.e. it is odd.
    if highway_number % 2 == 1:
        print(f"I-{highway_number} is primary, going north/south.")
    # determine if the highway goes east/west; i.e. it is even
    if highway_number % 2 == 0:
        print(f"I-{highway_number} is primary, going east/west.")
  # 200 is not a valid number
  elif highway_number == 200:
     print(f"{highway_number} is not a valid interstate highway number.")
  # the highway number is auxilliary if it is between 100 and 999
  elif 100 <= highway_number <= 999:
    # determine what primary highway is served; i.e. identify the rightmost digits
    primary_number = highway_number % 100
    # determine if the highway goes north/south; i.e. it is odd.
    if primary_number % 2 == 1:
        print(f"I-{highway_number} is auxillary, serving I-{primary_number}, going north/south.")
    # determine if the highway goes east/west; i.e. it is even
    if primary_number % 2 == 0:
        print(f"I-{highway_number} is auxillary, serving I-{primary_number}, going east/west.")
  else:
     print(f"{highway_number} is not a valid interstate highway number.")