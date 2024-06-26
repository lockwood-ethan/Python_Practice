from turtle import Screen, Turtle
from scoreboard import Scoreboard
import paddle
import ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

middle_line = Turtle()
r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
pongball = ball.Ball()
scoreboard = Scoreboard()

middle_line.color("white")
middle_line.shape("square")
middle_line.shapesize(stretch_wid=0.5, stretch_len=1)
middle_line.penup()
middle_line.goto(0, 325)
middle_line.setheading(270)
while middle_line.ycor() > -300:
    middle_line.forward(50)
    middle_line.stamp()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pongball.move_speed)
    screen.update()
    pongball.move()

    if pongball.ycor() > 280 or pongball.ycor() < -280:
        pongball.bounce_y()

    if pongball.distance(r_paddle) < 50 and pongball.xcor() > 325 or pongball.distance(l_paddle) < 50 and pongball.xcor() < -325:
        pongball.bounce_x()

    if pongball.xcor() > 380:
        pongball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()
    if pongball.xcor() < -380:
        pongball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()

screen.exitonclick()