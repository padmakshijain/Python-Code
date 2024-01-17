# Generate a random number between 1 and 10. Ask the user to guess the number and print a
# message based on whether they get it right or not.
import random

guess= int(input("Enter number"))
num = random.randint(1,10)
print(num)
if num == guess:
    print("you are right")
else: print("you are wrong")
