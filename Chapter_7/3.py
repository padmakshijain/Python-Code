# 3. Start with the list [8,9,10]. Do the following:
# (a) Set the second entry (index 1) to 17
# (b) Add 4, 5, and 6 to the end of the list
# (c) Remove the first entry from the list
# (d) Sort the list
# (e) Double the list
# (f) Insert 25 at index 3
# The final list should equal [4,5,6,25,10,17,4,5,6,10,17]

list = [8, 9, 10]
list[1]=17
print(list)
new_list = list + [4, 5, 6]
print(new_list)
del new_list[:2]
print(new_list)
new_list.sort()
print(new_list)
print(new_list * 2)
new_list.insert(3,25)
print(new_list)

