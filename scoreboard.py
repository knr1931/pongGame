from turtle import Turtle
from constants import LEFT_PLAYER_SCORE_POSITION, RIGHT_PLAYER_SCORE_POSITION, SCOREBOARD_CENTER_ALIGN, SCOREBOARD_FONT


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LEFT_PLAYER_SCORE_POSITION)
        self.write(arg=self.l_score, move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)
        self.goto(RIGHT_PLAYER_SCORE_POSITION)
        self.write(arg=self.r_score, move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)

    def increase_left_player_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_right_player_score(self):
        self.r_score += 1
        self.update_scoreboard()
