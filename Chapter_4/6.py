# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

item = int(input("How many item you want to buy"))
if item < 10:
    cost = 12 * item
    print(cost)
elif 10 < item < 99:
    cost = 10 * item
    print(cost)
else:
    cost = item * 7
    print(cost)
