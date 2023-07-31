from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)


scoreboard = Scoreboard()


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
# keybind keys to moves
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    # update screen to disable init animation
    screen.update()

    # move the ball
    ball.move()

    #detect the collision with the top and bottom wall 
    if ball.ycor() > 290 or ball.ycor() < -290:
        # needs to bounce
        ball.bounce_y()

    # detect collision with right_paddle and left_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 335 or ball.distance(left_paddle) < 50 and ball.xcor() > -335:
        ball.bounce_x()

    # detect if the  R paddle misses
    if ball.xcor() > 390:
        print("Out of bounds")
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()


    # detect if the  L paddle misses
    if ball.xcor() < -390:
        print("Out of bounds")
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
screen.exitonclick()