import turtle
import random
pen = turtle.Turtle()

def quadrantCross(size, randomColor, singleColor):

    rangeVal = 11
    #Change this value if you want to make the quadrant cross larger.
    xYVal = size

    #Left Quadrant
    for i in range(0, rangeVal):
        if (randomColor):
            pen.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            pen.color(singleColor)
        yFrom = 10 - i
        xTo = i
        pen.pu()
        pen.goto(0, xYVal * yFrom)
        pen.pd()
        pen.goto(-xYVal * xTo, 0)

    #Bottom Left Quadrant
    for i in range(0, rangeVal):
        if (randomColor):
            pen.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            pen.color(singleColor)
        yFrom = -10 + i
        xTo = i
        pen.pu()
        pen.goto(0, xYVal * yFrom)
        pen.pd()
        pen.goto(xYVal * -xTo, 0)

    #Bottom Right Quadrant
    for i in range(0, rangeVal):
        if (randomColor):
            pen.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            pen.color(singleColor)
        yFrom = -10 + i
        xTo = -i
        pen.pu()
        pen.goto(-i + i, xYVal * yFrom)
        pen.pd()
        pen.goto(-xYVal * xTo, 0)

    #Top Right Quadrant
    for i in range(0, rangeVal):
        if (randomColor):
            pen.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            pen.color(singleColor)
        yFrom = 10 - i
        xTo = i
        pen.pu()
        pen.goto(0, xYVal * yFrom)
        pen.pd()
        pen.goto(xYVal * xTo, 0)

quadrantCross(25, False, "red")
