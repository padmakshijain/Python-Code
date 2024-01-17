# Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in15◦
# increments. Each result should be rounded to 4 decimal places. Sample output is shown
# below:
# 0 --- 0.0 1.0
# 15 --- 0.2588 0.9659
# 30 --- 0.5 0.866
# ...
# 345 --- -0.2588 0.9659
import math

for i in range(0, 350, 15):
    sin = math.sin(math.radians(round(i,4)))
    cos = math.cos(math.radians(round(i, 4)))
    print(i,"---",round(sin,4),round(cos,4))