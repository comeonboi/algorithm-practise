from random import random
from turtle import *
import time
colormode(1)
n = 50
penup()
goto(0, 300)
pendown()
speed(50)
flag2 = 0
for i in range(1, 11):
    right(120)
    for j in range(1, 25):
        if flag2 != 0:
            right(89)
            forward(n - j * 2)
    setheading(0)
    flag2 += 1
    penup()
    goto(0, 300-60 * flag2)
    pendown()
    pencolor(random(), random(), random())
time.sleep(60)
exit(0)