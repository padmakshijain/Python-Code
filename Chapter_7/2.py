# 2. Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list
# (e) Print how many even numbers are in the list.

# a
from random import randint

L = []
for i in range(20):
    L.append(randint(1, 100))
print(L)

# b
average = sum(L) / len(L)
print(average)

# c
print(min(L), "small")
print(max(L), "Large")

# d
L.sort()
# print(L)
print("second largest",L[-2])
print("second smallest",L[2])

#e
count = 0
for i in L:
    if i % 2 == 0 :
        count = count+1
    else:
        pass
print(count)