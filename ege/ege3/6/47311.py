from turtle import *

tracer(0)
screensize(5000, 2000)


k = 30


for i in range (4):
    fd(12 * k)
    rt(150)
    fd(12 * k)
    rt(30)


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')



input()