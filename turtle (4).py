import turtle
p=turtle.Turtle()
color1=["red","purple","blue","green","orange"]
for x in range(1,222):
    p.color(color1[x%5])
    p.right(179)
    p.forward(x*5)
    p.speed(x*10)
turtle.done()