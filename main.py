from turtle import getturtle, getscreen

t = getturtle()
t.shape("turtle")
t.color("green")
print(t.position())
t.goto(0, 100)
# drawing a square with turtle module
# t = ninja_turtle
# for _ in range(4):
#     t.forward(200)
#     t.right(90)
# drawing a dotted line with turtle module
# for _ in range(10):
#     t.forward(10)
#     t.pendown()
#     t  .forward(10)
#     t.penup()
# for _ in range(3):
#     t.forward(100)
#     t.right(120)
# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# for _ in range(5):
#     t.forward(100)
#     t.right(72)
# for _ in range(6):
#     t.forward(100)
#     t.right(60)
# for _ in range(7):
#     t.forward(100)
#     t.right(51)
# for _ in range(8):
#     t.forward(100)
#     t.right(45)
# for _ in range(9):
#     t.forward(100)
#     t.right(40)
# for _ in range(10):
#     t.forward(100)
#     t.right(36)
def draw_shape(no_of_sides):
    angle = 360/no_of_sides
    for _ in range(no_of_sides):
        t.forward(100)
        t.right(angle)

for shape_side in range(3 , 11):
    draw_shape(shape_side)


screen = getscreen()
screen.exitonclick()
