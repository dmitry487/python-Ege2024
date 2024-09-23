from turtle import *


tracer(0)
screensize(5000, 4000)

k = 30


rt(180)
fd(5 * k)
rt(90)
fd(50 * k)
rt(90)
fd(5 * k)


for i in range (5):
    circle(5 * k, 180)
    


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')


input()