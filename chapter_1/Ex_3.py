num = int(input("number of row"))
for i in range(num):
    for j in range(i+1):
        print("*",end='')
    print()
