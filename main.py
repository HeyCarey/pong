from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#8c0000")
screen.title("Carey's Pong Game")
screen.tracer(0)

#paddles
paddle_b = Paddle((350, 0))
paddle_a = Paddle((-350, 0))

ball = Ball()

#scoring
score = Scoreboard()



#move paddles
screen.listen()
screen.onkey(paddle_b.go_up, "Up")
screen.onkey(paddle_b.go_down, "Down")
screen.onkey(paddle_a.go_up, "w")
screen.onkey(paddle_a.go_down, "s")

game_on = True
while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision of wall
    if ball.ycor() > 280 or ball.ycor() < -285:
        ball.bounce_y()

    #detect collision of paddle
    if ball.distance(paddle_b) < 50 and ball.xcor() > 320 or ball.distance(paddle_a) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if ball goes out of bound - reset ball to center of screen and start ball moving toward other player.
    #a
    if ball.xcor() < -380:
        ball.reset_position()
        score.scoring_b()
    #b
    elif ball.xcor() > 380:
        ball.reset_position()
        score.scoring_a()




screen.exitonclick()