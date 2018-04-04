import turtle
pen = turtle.Turtle()

def square(size):
    for i in range(4):
        pen.left(90)
        pen.forward(size)

def circleInSquare(size, squareColor, circleColor):
    pen.reset()
    pen.color(squareColor)
    square(size)
    pen.color(circleColor)
    pen.pu()
    pen.left(90)
    pen.forward(size / 2)
    pen.pd()
    pen.circle(size / 2)

circleInSquare(100, "red", "blue")
