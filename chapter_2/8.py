# Write a program that asks the user for their name and how many times to print it.The program should print out the user’s name the specified number of time

name = input("Enter your name")
n = int(input("Enter how much you want to print"))
for i in range(n):
    print(name)