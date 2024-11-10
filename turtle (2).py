import turtle
t = turtle.Turtle()
colors = ["green", "red", "blue", "hotpink", "purple", "black"]
t.speed(5)
t.pensize(5)
i = 1
while i < 80:
    t.color(colors[i % 5])
    t.forward(i*2)
    t.left(71)
    i = i+1

turtle.done()
