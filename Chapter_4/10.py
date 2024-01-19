# Write a multiplication game program for kids. The program should give the player ten randomly generated
# multiplication questions to do. After each, the program should tell them whether they got it right or wrong and
# what the correct answer is. Question 1: 3 x 4 = 12 Right! Question 2: 8 x 6 = 44 Wrong. The answer is 48. ... ...
# Question 10: 7 x 7 = 49 Right.
import random

num1 = random.randint(1, 10)
print(num1)
num2 = random.randint(1, 10)
print(num2)
res = num2 * num1
ans = int(input("Enter your ans"))
print(num1, "x", num2, "=", ans)
if res == ans:
    print("Right!")
else:
    print("Wrong. The answer is ", res)
