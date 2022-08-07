from turtle import Turtle, Screen

tim = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('darkblue')
# timmy_the_turtle.forward(150)
# timmy_the_turtle.right(40)

for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()


