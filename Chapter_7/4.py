# Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
# entries in the list that are greater than 10 with 10.

L = eval(input('Enter a list: '))
print(L)
for i in range(len(L)):
    if L[i] > 10:
        L[i] = 10
print(L)
