import random
from turtle import getturtle, getscreen

t = getturtle()
t.shape("turtle")
t.color("green")
t.goto(0, 100)
colors = ["blue", "lime", "red", "dark magenta", "gold", "magenta", "dark green", "maroon",
          ]


def draw_shape(no_of_sides):
    angle = 360/no_of_sides
    for _ in range(no_of_sides):
        t.forward(100)
        t.right(angle)


for shape_side in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(shape_side)


screen = getscreen()
screen.exitonclick()
