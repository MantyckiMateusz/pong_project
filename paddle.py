from turtle import Turtle

SPEED = 20

class Paddle(Turtle):

    def __init__(self, x ,y):
        super().__init__()
    
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        if not self.ycor() > 240:
            self.goto(self.xcor(), self.ycor()+SPEED)

    def move_down(self):
        if not self.ycor() < -230:
            self.goto(self.xcor(), self.ycor()-SPEED)