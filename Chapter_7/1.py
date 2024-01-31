# 1. Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items, and print the
# result.
# g) Print how many integers in the list are less than 5.

# a
L = eval(input('Enter a list: '))
print(len(L))

# b
print(L[-1])

# c
print(L[::-1])

# d
if 5 in L:
    print("Yes")
else:
    print("No")

# e
count = 0
for i in L:
    if i == 5:
        count = count + 1
print(count)

# f
new_list = L[1:-1]
print(new_list)
new_list.sort()
print(new_list)

# g
count = 0
for i in L:
    if i > 5:
        count = count + 1
print(count)
