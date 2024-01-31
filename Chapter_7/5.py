# Ask the user to enter a list of strings. Create a new list that consists of those strings with their
# first characters removed.

l1=[]
l = eval(input('Enter a list: '))
for i in range(len(l)):
    l1.append(l[i][1:])

print(l1)