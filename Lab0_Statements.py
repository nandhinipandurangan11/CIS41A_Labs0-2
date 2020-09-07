import math

# 1) The volume of a sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with radius 5?
volume = (4 / 3) * math.pi * math.pow(5, 3)
print("The volume of a sphere with radius 5 is", round(volume, 2), "cubic units")
print()

#--------------------------------------------------------------------------------------------------------------------
# 2) Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first
    # copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

    #finding the values needed for calculations
cover_price = 24.95
discount = 0.40
discounted_price = cover_price - (cover_price * discount)
num_copies = 60

    #calculating total prices 
cost_of_books = discounted_price*num_copies
shipping_cost =  0.75*(num_copies-1) + 3
total_cost = cost_of_books + shipping_cost

    #printing result
print("The total wholesale cost for 60 copies is $",round(total_cost,2))
print()

#--------------------------------------------------------------------------------------------------------------------
#3)If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
    # tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

    #initializing variables with given information
initial_hours = 6
initial_minutes = 52
easy_minutes = 8
easy_seconds = 15
tempo_minutes = 7
tempo_seconds = 12

    #finding the respective minutes and seconds for 2 miles in easy pace and 3 miles in tempo pace
total_easy_minutes = 2 * easy_minutes
total_easy_seconds = 2 * easy_seconds
total_tempo_minutes = 3 * tempo_minutes
total_tempo_seconds = 3 * tempo_seconds

    #calculating total minutes and total seconds 
total_minutes = initial_minutes + total_easy_minutes + total_tempo_minutes
total_seconds = total_easy_seconds + total_tempo_seconds

    #the following variables will be initialized in the if/else statementes 
final_hours = 0
final_minutes = 0
final_seconds = 0
time_of_day = ""

    #deciding if total minutes need to be incremented 
if (total_seconds > 60):
    additional_minutes = total_seconds //60
    total_minutes += additional_minutes
    final_seconds = total_seconds - (additional_minutes * 60)

else:
    final_seconds = total_seconds

    #deciding if total hours need to be incremented 
if (total_minutes > 60):
    additional_hours = total_minutes//60
    final_hours = initial_hours + additional_hours
    final_minutes += total_minutes - (additional_hours * 60)
else:
    final_minutes = total_minutes

    #deciding the time of day
if (final_hours < 12):
    time_of_day = "am"
else:
    time_of_day = "pm"

    #print result
print("After running 2 miles at easy pace and 3 miles in tempo speed, you arrive home at",
      final_hours,":", final_minutes,time_of_day)


''' 
Output: 

The volume of a sphere with radius 5 is 523.6 cubic units

The total wholesale cost for 60 copies is $ 945.45

After running 2 miles at easy pace and 3 miles in tempo speed, you arrive home at 7 : 30 am

'''