# Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.
sum = 0
for NUM in range(1, 2001):
       series = NUM - (NUM + 1) + (NUM - 1)
       sum += series
print(sum)
