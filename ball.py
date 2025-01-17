from turtle import Turtle
from constants import (
    BALL_WIDTH_FACTOR, BALL_HEIGHT_FACTOR,
    BALL_COLOR, BALL_SHAPE, INITIAL_BALL_SPEED, BALL_SPEED_INCREASE_FACTOR,
    BALL_MOVING_DISTANCE
)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=BALL_WIDTH_FACTOR, stretch_len=BALL_HEIGHT_FACTOR)
        self.color(BALL_COLOR)
        self.move_speed = INITIAL_BALL_SPEED
        self.x_move = BALL_MOVING_DISTANCE
        self.y_move = BALL_MOVING_DISTANCE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= BALL_SPEED_INCREASE_FACTOR

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = INITIAL_BALL_SPEED
        self.bounce_x()
