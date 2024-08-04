from turtle import Screen
from paddle import Paddle
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    RIGHT_PADDLE_XCOR, RIGHT_PADDLE_YCOR,
    RIGHT_PADDLE_UP_KEY, RIGHT_PADDLE_DOWN_KEY,
    LEFT_PADDLE_XCOR, LEFT_PADDLE_YCOR,
    LEFT_PADDLE_UP_KEY, LEFT_PADDLE_DOWN_KEY,
    BALL_YCOR_BOUNDARY, BALL_RIGHT_PADDLE_BOUNDARY, BALL_LEFT_PADDLE_BOUNDARY,
    BALL_PADDLE_COLLISION_DISTANCE
)
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

screen.listen()

# Right Paddle functionality
right_paddle = Paddle(x_cor=RIGHT_PADDLE_XCOR, y_cor=RIGHT_PADDLE_YCOR)

screen.onkey(key=RIGHT_PADDLE_UP_KEY, fun=right_paddle.up)
screen.onkey(key=RIGHT_PADDLE_DOWN_KEY, fun=right_paddle.down)

# Left Paddle functionality
left_paddle = Paddle(x_cor=LEFT_PADDLE_XCOR, y_cor=LEFT_PADDLE_YCOR)

screen.onkey(key=LEFT_PADDLE_UP_KEY, fun=left_paddle.up)
screen.onkey(key=LEFT_PADDLE_DOWN_KEY, fun=left_paddle.down)


ball = Ball()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    if ball.ycor() == BALL_YCOR_BOUNDARY or ball.ycor() == -BALL_YCOR_BOUNDARY:
        ball.bounce_y()

    if ((ball.distance(right_paddle) < BALL_PADDLE_COLLISION_DISTANCE and ball.xcor() == BALL_RIGHT_PADDLE_BOUNDARY) or
            (ball.distance(left_paddle) < BALL_PADDLE_COLLISION_DISTANCE and ball.xcor() == BALL_LEFT_PADDLE_BOUNDARY)):
        ball.bounce_x()

screen.exitonclick()
