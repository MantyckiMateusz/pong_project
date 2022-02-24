from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.vx = 10
        self.vy = 10
        self.res()
        self.move_speed = 0.05

    def move(self):
        self.goto(self.xcor()+self.vx, self.ycor()+self.vy)
    
    def bounce_wall(self):
        self.vy *= -1

    def bounce_paddle(self):
        self.vx *= -1
        self.move_speed *= 0.9

    def res(self):
        self.goto(0, 0)
        self.vx *= -1
        self.move_speed = 0.05
        