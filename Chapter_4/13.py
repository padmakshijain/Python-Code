# . Write a program that lets the user play Rock-Paper-Scissors against the computer. There
# should be five rounds, and after those five rounds, your program should print out who won
# and lost or that there is a tie.
from random import randint

t = ["rock","paper","scissor"]
print(t)
computer = t[randint(0,2)]
# print(computer)
player = input("Enter your choice")
if player == computer:
    print("You win!")
else :
    print("no")
