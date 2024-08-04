from turtle import Turtle
from constants import (
    BALL_WIDTH_FACTOR, BALL_HEIGHT_FACTOR,
    BALL_COLOR, BALL_SHAPE, BALL_SPEED,
    SCREEN_HEIGHT_BOUNDARY,
    BALL_MOVING_DISTANCE
)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=BALL_WIDTH_FACTOR, stretch_len=BALL_HEIGHT_FACTOR)
        self.color(BALL_COLOR)
        self.speed(BALL_SPEED)
        self.ycor_change = BALL_MOVING_DISTANCE

    def move(self):
        new_x = self.xcor() + BALL_MOVING_DISTANCE
        if self.ycor() == SCREEN_HEIGHT_BOUNDARY or self.ycor() == -SCREEN_HEIGHT_BOUNDARY:
            self.bounce()
        new_y = self.ycor() + self.ycor_change
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        if self.ycor() > 0:
            self.ycor_change = -BALL_MOVING_DISTANCE
        else:
            self.ycor_change = BALL_MOVING_DISTANCE
