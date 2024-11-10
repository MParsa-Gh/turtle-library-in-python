import turtle
t=turtle.Turtle()
t.speed(2)
t.pensize(3)




t.penup()
t.goto(-100,-100)
t.pendown()
t.goto(100,-100)
t.goto(100,100)
t.goto(-100,100)
t.goto(-100,-100)
t.goto(-80,-100)
t.fillcolor("#9bd658")

t.penup()
t.goto(80,80)
t.left(-180)
t.pendown()

t.goto(40,80)
t.goto(40,40)
t.goto(80,40)
t.goto(80,80)

t.penup()
t.goto(-80,-100)
t.left(-180)
t.pendown()

t.goto(-80,-100)
t.goto(-20,-100)
t.goto(-20,0)
t.goto(-80,-0)
t.goto(-80,-100)

t.penup()
t.goto(-100,100)
t.pendown()

t.goto(0,200)
t.goto(100,100)
t.pendown()


turtle.done()