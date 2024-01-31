# . People often forget closing parentheses when entering formulas. Write a program that asks
# the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses.

str = input("Enter a formula: ")
count = 0

for ch in str :
    if ch == '(' :
        count += 1
    elif ch == ')' :
        count -= 1

if count == 0 :
    print("Formula has same number of opening and closing parentheses")
else :
    print("Formula has unequal number of opening and closing parentheses")