from turtle import Screen, Turtle
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake1 = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()

    if snake1.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()


screen.exitonclick()
