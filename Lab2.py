# CIS41A: Lab2: Nandhini Pandurangan
# This program solves the problems in Lab 0 using user defined classes for each of the assigned problems

import math

# 1) The volume of a sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with radius 5?
class Sphere:

    # constructor
    def __init__(self, radius):
        self.radius = radius
        self.volume = 0

    # overloading str function
    def __str__(self):
        return "The volume of a sphere with radius " + str(self.radius) + " is " + str(self.calculate_volume()) + " cubic units"

    # calculating the volume
    def calculate_volume(self):
        self.volume = (4 / 3) * math.pi * math.pow(self.radius, 3)
        return round(self.volume, 2)


# 2) Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first
# copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
class Book:

    # constructor
    def __init__(self, book_price, discount, initial_shipping_cost, additional_copy_cost, number_of_copies):
        self.book_price = book_price
        self.discount = discount
        self.initial_shipping_cost = initial_shipping_cost
        self.additional_copy_cost = additional_copy_cost
        self.number_of_copies = number_of_copies

        self.discounted_price = 0
        self.total_book_cost = 0
        self.total_shipping_cost = 0
        self.total_wholesale_cost = 0

    # overloading str function
    def __str__(self):
        return "The total wholesale cost for " + str(self.number_of_copies)+ " copies is $" + str(self.calculate_wholesale_cost())

    # performs the wholesale cost calculation
    def calculate_wholesale_cost(self):
        self.discounted_price = self.book_price - (self.book_price * self.discount)
        self.total_book_cost = self.discounted_price * self.number_of_copies
        self.total_shipping_cost = self.initial_shipping_cost + ((self.number_of_copies - 1) * self.additional_copy_cost)
        self.total_wholesale_cost = self.total_book_cost + self.total_shipping_cost
        return round(self.total_wholesale_cost, 2)


# 3)If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
class Running:
    def __init__(self, initial_hours, initial_minutes, initial_seconds, distance, pace_minutes, pace_seconds):

        # initializing class variables
        self.initial_hours = initial_hours
        self.initial_minutes = initial_minutes
        self.initial_seconds = initial_seconds
        self.distance = distance
        self.pace_minutes = pace_minutes
        self.pace_seconds = pace_seconds

        # calculating total time for initial run
        self.total_run_minutes = self.distance * self.pace_minutes
        self.total_run_seconds = self.distance * self.pace_seconds

        # initializing end time
        self.end_hour = self.initial_hours
        self.end_minutes = self.initial_minutes + self.total_run_minutes
        self.end_seconds = self.initial_seconds + self.total_run_seconds

        # deciding time of day
        if self.end_hour < 12:
            self.time_of_day = "am"
        else:
            self.time_of_day = 'pm'

    # overloading str function
    def __str__(self):
        return "You arrive home at " + str(self.end_hour) + ":" + str(self.end_minutes) + " " + self.time_of_day

    # This function is called several times for each portion of the run
    def calculate_total_time(self, distance, pace_minutes, pace_seconds):
       self.end_minutes += (distance * pace_minutes)
       self.end_seconds += (distance * pace_seconds)

       self.finalize_output()

    # formats the output according to time rules
    def finalize_output(self):
        # deciding if total minutes need to be incremented
        if self.end_seconds > 60:
            self.end_minutes += self.end_seconds // 60
            self.end_seconds %= 60

        # deciding if total hours need to be incremented
        if self.end_minutes > 60:
            self.end_hour += self.end_minutes // 60
            self.end_minutes %= 60

        # deciding the time of day
        if self.end_hour >= 12:
            self.time_of_day = "pm"

        return self.end_hour, self.end_minutes, self.end_seconds


# Using the classes to solve problems 1-3 by entering appropriate values

#1
mySphere = Sphere(5)
print(mySphere)  # printing the volume of the sphere given radius 5

#2
schoolBook = Book(24.95, 0.40, 3, 0.75, 60)
print(schoolBook)

#3
myRun = Running(6, 52, 0, 1, 8, 15)
myRun.calculate_total_time(3, 7, 12)
myRun.calculate_total_time(1, 8, 15)
print(myRun)








