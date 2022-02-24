from paddle import Paddle
from config import Config
from ball import Ball
from time import sleep
from score import Score

paddle1 = Paddle(360, 0)
paddle2 = Paddle(-360, 0)
config = Config(paddle1, paddle2)
ball = Ball()
score = Score()

game_is_on = True
while game_is_on:
    config.screen.update()
    sleep(ball.move_speed)

    if (ball.distance(paddle1) < 54 and ball.xcor() > 320 and ball.xcor() < 350) or (ball.distance(paddle2) < 54 and ball.xcor() < -320 and ball.xcor() > -350):
            ball.bounce_paddle()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.xcor() > 400:
        ball.res()
        score.update_score1()
        score.draw_scoreboard()
    if ball.xcor() < -400:
        ball.res()
        score.update_score2()
        score.draw_scoreboard()
    
    ball.move()

config.screen.exitonclick()