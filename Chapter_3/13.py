# Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.

import math
n = int(input("Enter number"))
sine = math.sin(n)
cosine = math.cos(n)
tangent = math.tan(n)
print("sine:", sine)
print("cosine:",cosine)
print("tangent:",tangent)