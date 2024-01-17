# Write a program that asks the user for a number and prints out the factorial of that number.

num = int(input("Enter a number"))
fact = 1
if num >1:
    for i in range(1, num+1):
        fact = fact * i
print("factorial of ",num,"is",fact)