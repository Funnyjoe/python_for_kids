import turtle as t
from random import randint, random


def draw_star(points, size, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180-(180/points)
    t.color(color)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()


# Main code
t.hideturtle()
t.Screen().bgcolor('dark blue')
while True:
    ranPts = randint(2, 5)*2+1
    ranSize = randint(10, 50)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)

    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
