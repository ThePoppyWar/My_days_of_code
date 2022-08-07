import turtle as t
import random

tim = t.Turtle()
colors = ['light gray', 'dark green', "teal", 'dark magenta', "medium purple", "gold"]
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape((shape_side))
