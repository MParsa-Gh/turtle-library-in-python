import turtle
import random
p=turtle.Turtle()
p.pensize(20)
color1=["red","purple","blue","green","orange"]
for x in range(1,100001):
    b=random.randint(0,4)
    p.color(color1[b])
    p.right(144)
    p.forward(x*5)
    p.speed(x*10)
turtle.done()