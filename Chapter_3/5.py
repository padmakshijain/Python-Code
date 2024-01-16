# Write a program that generates 50 random numbers such that the first number is between 1
# and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
# 1 and 51

import random

random_number = []

random_number.append(random.randint(1,2))
random_number.append(random.randint(1,3))
random_number.append(random.randint(1,4))
for i in range(47):
    random_number.append(random.randint(1,51))

print(random_number)