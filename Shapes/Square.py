import turtle
pen = turtle.Turtle()

def square (xPos, yPos, size, color, fill):
    pen.pu()
    pen.setposition(xPos, yPos)
    pen.pd()
    pen.color(color)
    if (fill):
        pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    if (fill):
        pen.end_fill()

square(0, 0, 100, "red", False)
