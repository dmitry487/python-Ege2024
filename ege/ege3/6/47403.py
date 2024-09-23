from turtle import *

screensize(5000, 2000)
tracer(0)
k = 50



for i in range(4):
    fd(12 * k)
    rt(90)


rt(30)

for i in range (3):
    fd(8 * k)
    rt(60)
    fd(8 * k)
    rt(120)


up()


for x in range (-50, 50):
    for y in range (-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')



input()