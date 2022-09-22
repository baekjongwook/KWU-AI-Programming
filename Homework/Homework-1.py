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

setup()

move(0, -250)
drawcircle("white", 250)

move(0, -245)
drawcircle("goldenrod", 245)

move(0, -180)
drawcircle("red", 100)

move(0, -160)
drawcircle("goldenrod", 110)

move(0, -30)
drawcircle("orange", 25)

move(-145, 45)
drawoval("black", 20, 145, 50)

move(-142.5, 50)
drawoval("cyan", 15, 140, 50)

move(40, 65)
drawoval("black", 25, 50, 135)

move(50, 70)
drawoval("blue", 15, 40, 135)

t.done()