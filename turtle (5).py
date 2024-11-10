import turtle
p=turtle.Turtle()
i=1
list1=["red","purple","blue","green","orenge"]
while i<=5:
    p.forward(300)
    p.right(144)
    p.color(list1[i-1])
    i=i+1
turtle.done()

