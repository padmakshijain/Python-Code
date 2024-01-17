# Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an
# inch.

num = int(input("Enter a length in centimeters"))
if num <= 0:
    print("entry is invalid.")
else:
    print(2.54*num)