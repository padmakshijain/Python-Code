# Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

kilo = int(input("Enter a weight in kilogram"))
pound = 2.20462 * kilo
print(round(pound,2))