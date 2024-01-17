# Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

num = int(input("How many credits you have taken"))
if num <= 23:
    print("You are freshman")
elif num >=24 and num <= 53:
    print("You are sophomore")
elif num >=54 and num<=83:
    print("You are juniors")
else:
    print("You are seniors")