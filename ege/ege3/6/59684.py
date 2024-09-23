from turtle import *


tracer(0)
screensize(5000, 2000)

k = 30

for i in range (2):
    fd(10 * k)
    rt(90)
    fd(18 * k)
    rt(90)


up()

fd(5 * k)
rt(90)
fd(7 * k)
lt(90)


down()

for i in range (2):
    fd(10 * k)
    rt(90)
    fd(7 * k)
    rt(90)


up()

for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')


input()