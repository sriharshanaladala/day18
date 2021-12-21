from turtle import Screen, Turtle
import random

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


direction = [0, 90, 180, 270]
tim.speed(0)
tim.pensize(10)

for i in range(200):
    tim.forward(30)
    # tim.color(random.random(), random.random(), random.random())
    tim.color(random_color())
    dirn = random.choice(direction)
    tim.setheading(dirn)

screen.exitonclick()
