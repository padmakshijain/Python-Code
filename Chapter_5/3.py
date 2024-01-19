import math

n = int(input("Enter the value"))
s = 0
for i in range(1,n+1):
    s = s + (1/i)
    res = s - math.log(n)
print(round((res),2))

