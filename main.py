from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
import keyboard

# creating screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# creating boundary
boundary = Turtle(shape="blank")
boundary.setpos(0, 280)
boundary.setheading(270)
boundary.color("white")
boundary.pensize(5)
for i in range(22):
    boundary.penup()
    boundary.forward(15)
    boundary.pendown()
    boundary.forward(10)

# creating paddles
paddle = Paddle(1)
paddle2 = Paddle(2)
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle.down, "Down")
screen.onkeypress(paddle2.down, "s")
ball = Ball()
score_1 = Score(1)
score_2 = Score(2)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.speed(ball.speed() + 3)
        ball.bounce_paddle()
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            score_1.update()
        elif ball.xcor() < -380:
            score_2.update()
        ball.x_move *= -1
        ball.home()
        ball.speed(1)
        ball.move()
    if score_1.score == 5 or score_2.score == 5:
        game_is_on = False
    if keyboard.is_pressed("Escape"):
        screen.bye()
screen.exitonclick()
