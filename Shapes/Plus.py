import turtle
pen = turtle.Turtle()

def plus(xPos, yPos, length, width, color, fill):  
    pen.pu()
    pen.setposition(xPos, yPos)
    pen.pd()
    pen.color(color)
    if (fill):
        pen.begin_fill()
    pen.forward(length)  
    pen.left(90)  
    pen.forward(width)  
    pen.left(90)  
    pen.forward(length)  
    pen.left(-90)  
    pen.forward(length)  
    pen.right(-90)  
    pen.forward(width)  
    pen.right(-90)  
    pen.forward(length)  
    pen.left(-90)  
    pen.forward(length)  
    pen.left(90)  
    pen.forward(width)  
    pen.left(90)  
    pen.forward(length)  
    pen.left(-90)  
    pen.forward(length)  
    pen.left(90)  
    pen.forward(width)  
    pen.left(90)  
    pen.forward(length)
    if (fill):
        pen.end_fill()


plus(0, 0, 100, 40, "red", True)
