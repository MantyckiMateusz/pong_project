
from ast import arg
from re import S
from turtle import Turtle, goto

FONT = ('Arial', 16, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color('white')
        self.draw_line()
        self.hideturtle()
        self.draw_scoreboard()
        
    def draw_scoreboard(self):
        self.clear()
        self.draw_line()
        self.penup()
        self.goto(-20, 270)
        self.pendown()
        self.write(arg=f"{self.score1}", move=False,  align='center', font=FONT)

        self.penup()
        self.goto(20, 270)
        self.pendown()
        self.write(arg=f"{self.score2}", move=False,  align='center', font=FONT)

    

    def draw_line(self):
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(30):
            self.penup() if self.isdown() else self.pendown()
            self.fd(20)

    def update_score1(self):
        self.score1 += 1
        
    def update_score2(self):
        self.score2 += 1
        