"""
    Author: "Spencer Morris"
    Write a program that is given two integers representing a speed limit and driving speed in miles per hour
    (mph) and outputs the traffic ticket amount.
    Speed Conditions:
        1. Driving 10 mph under the speed limit (or slower) receives a $50 ticket.
        2. Driving 6 - 20 mph over the speed limit receives a $75 ticket.
        3. Driving 21 - 40 mph over the speed limit receives a $150 ticket.
        4. Driving faster than 40 mph over the speed limit receives a $300 ticket.
        5. Otherwise, no ticket is received.
"""

# take the speed limit and car speed as input
speed_limit = int(input("What is the speed limit of the road? Answer Below: \n"))
car_speed = int(input("What is the speed of the car? Answer Below: \n"))

# calculate the difference between the cars speed and the speed limit
speed_differential = car_speed - speed_limit

# determine the fine
speeding_fine = 0
if speed_differential <= -10:
    speeding_fine = 50
elif 20 >= speed_differential >= 6:
    speeding_fine = 75
elif 40 >= speed_differential > 20:
    speeding_fine = 150
elif speed_differential > 40:
    speeding_fine = 300
else:
    speeding_fine = 0

# print the fine amount
if speed_differential <= -10:
    print(f"The fine is ${speeding_fine} for going {abs(speed_differential)} mph under the speed limit.")
elif speed_differential >= 6:
    print(f"The fine is ${speeding_fine} for going {speed_differential} mph over the speed limit.")
else:
    print("There is no fine.")