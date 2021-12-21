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


ts.speed("fastest")


def draw_spirography(set_degree):
    for _ in range(int(360/set_degree)):
        ts.circle(50)
        ts.color(random_color())
        ts.setheading(ts.heading() + set_degree)


draw_spirography(5)

screen = t.Screen()
screen.exitonclick()
