# Write a program that generates a random decimal number between 1 and 10 with two decimal
# places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
import random
from random import randint
x = random.uniform(1,10)
print(round(x,2))