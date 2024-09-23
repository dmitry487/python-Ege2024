from turtle import *

tracer(0)
screensize(7000, 4000)

k = 30


for i in range (2):
    fd(23 * k)
    lt(90)
    bk(27 * k)
    lt(90)


up()

bk(5 * k)
rt(90)
fd(11 * k)
lt(90)


down()

for i in range (2):
    fd(26 * k)
    rt(90)
    fd(32 * k)
    rt(90)


up()

for x in range (-80, 80):
    for y in range (-40, 40):
        goto(x * k, y * k)
        dot(3, 'red')


input()