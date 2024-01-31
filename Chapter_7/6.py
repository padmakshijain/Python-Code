# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
#a
l =[]
for i in range(0,50):
    l.append(i)
print(l)
#b
k =[]
for i in range(1,51):
    k.append(i*i)
print(k)
#c
m = []
for i in range(0,27):
    m.append(chr(i + 96) * i)
print(m)
