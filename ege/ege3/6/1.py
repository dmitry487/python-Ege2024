from turtle import *

tracer(0)
screensize(5000, 2000)


k = 30


rt(270)
for i in range (2):
    fd(6 * k)
    rt(120)


rt(120)

for i in range (2):
    rt(120)
    fd(3 * k)
    rt(240)

rt(240)

for i in range (2):
    fd(12 * k)
    rt(120)


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')


input()