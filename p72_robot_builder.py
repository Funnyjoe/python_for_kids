import turtle as t


def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
        # The turtle moves forward x pixels, turns right 90 degrees, then moves forward y pixels
    t.end_fill()
    t.penup()

# 1.Set the background color and the turtle’s speed


t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')


# 2.feet
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')
# 3.legs
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')
# 4.body
t.goto(-90, 100)
rectangle(100, 150, 'red')
# 5.arms
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 40, 'grey')
t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')
# 6.neck
t.goto(-50, 120)
rectangle(15, 20, 'grey')
# 7.head
t.goto(-85, 170)
rectangle(80, 50, 'red')
# 8.eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')
# 9.mouth
t.goto(-65, 135)
rectangle(40, 5, 'black')
t.hideturtle()
