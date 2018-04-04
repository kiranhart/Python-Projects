import turtle
pen = turtle.Turtle()

def spiral (color, expandSize, stopNumber):
    pen.color(color)
    lastLine = 0
    timer = 0
    size = expandSize

    while (timer <= stopNumber):
        lastLine += 1
        pen.left(90)
        pen.fd(size)

        if (lastLine == 1 or lastLine == 2):
            size += 10
        elif (lastLine == 3):
            size += 10
            lastLine = 0
        timer += 1

spiral("red", 50, 25)
