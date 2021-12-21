from turtle import getturtle, getscreen
import random
tw = getturtle()
tw.shape("turtle")
tw.color("green")
colors = ["blue", "lime", "red", "dark magenta", "gold", "magenta", "dark green", "maroon"]
direction = [0, 90, 180, 270]

for _ in range(200):
    tw.speed("fastest")
    tw.pensize(20)
    tw.width(7)
    tw.color(random.choice(colors))
    tw.forward(20)
    tw.setheading(random.choice(direction))
screen = getscreen()
screen.exitonclick()
