import turtle as t
import random

ts = t.Turtle()
ts.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


ts.speed("fast")


for _ in range(200):
    ts.circle(100)
    ts.color(random_color())
    current_heading = ts.heading()
    ts.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()
