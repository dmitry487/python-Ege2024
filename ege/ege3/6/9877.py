from turtle import *

tracer(0)
screensize(5000, 2000)

k = 30

for i in range (3):
    fd(8 * k)
    lt(90)
    fd(14 * k)
    lt(90)


up()

fd(4 * k)
rt(90)
backward(3 * k)
lt(90)


down()

for i in range (2):
    fd(7 * k)
    lt(90)
    fd(5 * k)
    lt(90)


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')


input()