import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


diractions = [0, 100, 90, 180, 250]

tim.pensize(15)
tim.speed("slow")

for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(diractions))
