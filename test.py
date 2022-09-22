#2021741034 백종욱
import turtle as t

def setup(width = 550, height = 550, speed = 0, color = "gray"):
    t.setup(width, height)
    t.speed(speed)
    t.bgcolor(color)
    t.hideturtle()

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def drawcircle(color, radius):
    move(0, -radius)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def drawoval(color, smallradius, bigradius, smallangle):
    bigangle = 180 - smallangle
    t.seth(-smallangle // 2)
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.circle(bigradius, smallangle)
        t.circle(smallradius, bigangle)
    t.end_fill()

def drawsmile(color, width, height):
    move(0, -170)
    drawcircle("red", 80)

    move(0, -150)
    drawcircle("goldenrod", 100)

setup()

drawcircle("white", 250)
drawcircle("goldenrod", 245)

drawsmile("red", 20, )

move(0, -170)
drawcircle("red", 80)

move(0, -150)
drawcircle("goldenrod", 100)

drawcircle("orange", 25)

move(-145, 45)
drawoval("black", 20, 145, 50)

move(-142.5, 50)
drawoval("cyan", 15, 140, 50)

move(42.5, 50)
drawoval("black", 25, 50, 100)

move(50, 57.5)
drawoval("blue", 15, 40, 100)

t.done()