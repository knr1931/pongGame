from turtle import Turtle
from constants import (
    PADDLE_WIDTH_FACTOR, PADDLE_HEIGHT_FACTOR,
    PADDLE_COLOR, PADDLE_SHAPE,
    PADDLE_MOVING_DISTANCE, PADDLE_SPEED,
    PADDLE_Y_COR_BOUNDARY,
    UP, DOWN
)


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH_FACTOR, stretch_len=PADDLE_HEIGHT_FACTOR)
        self.color(PADDLE_COLOR)
        self.setx(x_cor)
        self.sety(y_cor)
        self.setheading(UP)
        self.speed(PADDLE_SPEED)

    def up(self):
        self.setheading(UP)
        if self.ycor() <= PADDLE_Y_COR_BOUNDARY:
            self.sety(self.ycor() + PADDLE_MOVING_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        if self.ycor() > -PADDLE_Y_COR_BOUNDARY:
            self.sety(self.ycor() - PADDLE_MOVING_DISTANCE)
