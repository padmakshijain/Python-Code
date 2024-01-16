n = int(input("Enter number"))
f ,s = 0,1
for i in range(0,n):
    if i<=1:
        result = i
    else:
        result= f+s
        f = s
        s = result
        print(result)