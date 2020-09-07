# CIS41A: Lab1: Nandhini Pandurangan
# This program solves the problems in Lab 0 using user defined functions for each of the assigned problems

import math


# 1) The volume of a sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with radius 5?
def calculate_volume(radius):
    volume = (4 / 3) * math.pi * math.pow(radius, 3)
    return round(volume, 2)

#--------------------------------------------------------------------------------------------------------------------
# 2) Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first
# copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

def calculate_wholesale_cost(book_price, discount, initial_shipping_cost, additional_copy_cost, number_of_copies):
    discounted_price = book_price - (book_price * discount)
    total_book_cost = discounted_price * number_of_copies
    total_shipping_cost = initial_shipping_cost + ((number_of_copies - 1) * additional_copy_cost)
    total_wholesale_cost = total_book_cost + total_shipping_cost
    return round(total_wholesale_cost, 2)


#--------------------------------------------------------------------------------------------------------------------
# 3)If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

def calculate_arrival_time(initial_hours, initial_minutes, initial_seconds, distance, pace_minutes, pace_seconds):
    # calculating the total run time in minutes and seconds
    total_run_minutes = distance * pace_minutes
    total_run_seconds = distance * pace_seconds

    # initializing return variables
    end_hour = initial_hours
    end_minutes = initial_minutes + total_run_minutes
    end_seconds = initial_seconds + total_run_seconds
    am_pm = "am"

    # deciding if total minutes need to be incremented
    if end_seconds > 60:
        end_minutes += end_seconds // 60
        end_seconds %= 60

    # deciding if total hours need to be incremented
    if end_minutes > 60:
        end_hour += end_minutes // 60
        end_minutes %= 60

    # deciding the time of day
    if end_hour >= 12:
        am_pm = "pm"

    return end_hour, end_minutes, end_seconds, am_pm

#--------------------------------------------------------------------------------------------------------------------
# calling the user-defined functions and printing the output
print("The volume of a sphere with radius 5 is", calculate_volume(5), "cubic units")
print()

print("The total wholesale cost for 60 copies is $", calculate_wholesale_cost(24.95, 0.40, 3, 0.75, 60))
print()

hour, minute, second, time_of_day = calculate_arrival_time(6, 52, 0, 1, 8, 15)
hour, minute, second, time_of_day = calculate_arrival_time(hour, minute, second, 3, 7, 12)
hour, minute, second, time_of_day = calculate_arrival_time(hour, minute, second, 1, 8, 15)

print("After running 2 miles at easy pace and 3 miles in tempo speed, you arrive home at %d:%d %s" % (
hour, minute, time_of_day))
