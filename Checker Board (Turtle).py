import turtle
pen = turtle.Turtle()
pen.speed("fastest")

TILE_SIZE = 50
COLOR_ONE_ID = "red"
COLOR_TWO_ID = "black"

def drawBox(xPos, yPos, size, color):
    pen.pu()
    pen.setposition(xPos, yPos)
    pen.pd()
    pen.color(color)
    pen.begin_fill()
    for i in range(4):
        pen.left(90)
        pen.fd(size)
    pen.end_fill()

ogY = 150
ogX = -160
reverse = False

def drawRow(x, y, c1):
    val = c1
    for i in range(8):
        if(val):
            drawBox(x, y, TILE_SIZE, COLOR_ONE_ID)
            x += TILE_SIZE
            val = False
        else:
            drawBox(x, y, TILE_SIZE, COLOR_TWO_ID)
            x += TILE_SIZE
            val = True

for i in range(8):
    if(not(reverse)):
        drawRow(ogX, ogY, True)
        ogY = ogY - TILE_SIZE
        reverse = True
    else:
        drawRow(ogX, ogY, False)
        ogY = ogY - TILE_SIZE
        reverse = False
