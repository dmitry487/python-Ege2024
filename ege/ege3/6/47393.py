from turtle import *


k = 30
tracer(0)
screensize(5000, 2000)



for i in range (6):
    rt(36)
    fd(10 * k)
    rt(36)


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')


input()






