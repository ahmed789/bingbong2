from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# initialize the screen#
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
# position of right and left paddle#
r_position = (360, 0)
l_position = (-360, 0)
# create right and left paddle object
r_paddle = Paddle(r_position)
r_paddle.color("red")
l_paddle = Paddle(l_position)
l_paddle.color("green")
# create ball object
ball = Ball()
# scoreboard object
scoreboard = Scoreboard()

screen.listen()

# detect paddle move
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# game loop control
game_is_on = True
while game_is_on:
    time.sleep(.00000001)
    screen.update()
    ball.move()

    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.y_bounce()

    if ball.distance(r_paddle) < 63 and ball.xcor() == 340 or \
            ball.distance(l_paddle) < 63 and ball.xcor() == -340:
        ball.x_bounce()

    if ball.xcor() > 390:
        ball.reposition()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reposition()
        scoreboard.r_point()

screen.exitonclick()
