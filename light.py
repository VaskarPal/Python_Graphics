import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(3)
turtle.pencolor("blue")
def circle(radius):
    for i in range(15):
        turtle.circle(radius)
        radius = radius - 4
def degine():
    for i in range(15):
        circle(180)
        turtle.right(30)
degine()
turtle.done()