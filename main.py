from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

tv = Screen()
tv.setup(height=600, width=600)
tv.bgcolor("black")
tv.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()
game = True

tv.listen()
tv.onkey(snake.up, "Up")
tv.onkey(snake.down, "Down")
tv.onkey(snake.right, "Right")
tv.onkey(snake.left, "Left")


while game:
    tv.update()
    time.sleep(0.3)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor() > 296 or snake.head.xcor() < -296 or snake.head.ycor() > 296 or snake.head.ycor() < -296:
        scoreboard.reset()
        snake.reset()
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

tv.exitonclick()
