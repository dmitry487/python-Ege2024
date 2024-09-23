from turtle import *


tracer(0)
k = 30

screensize(5000, 2000)

for i in range (7):
    fd(10 * k)
    rt(120)


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')



input()