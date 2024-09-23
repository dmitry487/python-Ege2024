from turtle import *

tracer(0)
screensize(5000, 2000)
k = 30


for i in range (2):
    fd(9 * k)
    rt(90)
    fd(15 * k)
    rt(90)


up()

fd(12 * k)
rt(90)

down()

for i in range (2):
    fd(6 * k)
    rt(90)
    fd(12 * k)
    rt(90)


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')


input()