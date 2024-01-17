# Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
# operator to get minutes and the % operator to get seconds.

sec = int(input("Enter the number of seconds"))
min = sec//60
secs = sec % 60

print(min,"minutes",secs,"seconds")