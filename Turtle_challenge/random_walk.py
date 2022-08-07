import random
import turtle as t


tim = t.Turtle()
colors = ['light gray', 'dark green', "teal", 'dark magenta', "medium purple", "gold"]
diractions = [0, 100, 90, 180, 250]

tim.pensize(15)
tim.speed("slowest")




for _ in range(300):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(diractions))