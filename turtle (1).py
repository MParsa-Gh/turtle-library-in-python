import turtle 
for i in range(7):
    for colours in{"red","green","blue","yellow","black"}:
        turtle.pensize(3)
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
        turtle.speed(1000)
turtle.done()

