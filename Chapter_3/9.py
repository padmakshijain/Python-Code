# Write a program that asks the user for an hour between 1 and 12 and for how many hours in
# the future they want to go. Print out what the hour will be that many hours into the future.
# An example is shown below.
# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 o'clock

hour = int(input("Enter an hour between 1 and 12"))
hour_ahead = int(input("How many hours ahead?"))
new_hour = hour + hour_ahead
if new_hour > 24:
    print("Can't convert in hour")
elif new_hour > 12:
    new_hour_1 = new_hour - 12
    print("New hour:", new_hour_1,"o'clock")
else:
    print(new_hour)
