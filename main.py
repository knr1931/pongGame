from turtle import Screen
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
)

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

screen.exitonclick()