from turtle import Screen
import paddle
import ball
import time
import scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball = ball.Ball()
r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
score = scoreboard.Scoreboard()

screen.listen()

# Key press states
r_paddle_up = False
r_paddle_down = False
l_paddle_up = False
l_paddle_down = False

# Functions to handle key presses
def r_paddle_up_press():
    global r_paddle_up
    r_paddle_up = True

def r_paddle_down_press():
    global r_paddle_down
    r_paddle_down = True

def l_paddle_up_press():
    global l_paddle_up
    l_paddle_up = True

def l_paddle_down_press():
    global l_paddle_down
    l_paddle_down = True

# Functions to handle key releases
def r_paddle_up_release():
    global r_paddle_up
    r_paddle_up = False

def r_paddle_down_release():
    global r_paddle_down
    r_paddle_down = False

def l_paddle_up_release():
    global l_paddle_up
    l_paddle_up = False

def l_paddle_down_release():
    global l_paddle_down
    l_paddle_down = False

# Bind key press and release events
screen.onkeypress(r_paddle_up_press, "Up")
screen.onkeyrelease(r_paddle_up_release, "Up")
screen.onkeypress(r_paddle_down_press, "Down")
screen.onkeyrelease(r_paddle_down_release, "Down")
screen.onkeypress(l_paddle_up_press, "w")
screen.onkeyrelease(l_paddle_up_release, "w")
screen.onkeypress(l_paddle_down_press, "s")
screen.onkeyrelease(l_paddle_down_release, "s")

game_is_on = True

while game_is_on:
    # Move paddles based on key states
    if r_paddle_up:
        r_paddle.up()
    if r_paddle_down:
        r_paddle.down()
    if l_paddle_up:
        l_paddle.up()
    if l_paddle_down:
        l_paddle.down()

    ball.move()
    time.sleep(ball.movespeed)
    screen.update()

    # Ball collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Ball collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.pbounce()

    # Ball out of bounds
    if ball.xcor() > 350:
        ball.lose()
        score.l_increment()
    if ball.xcor() < -350:
        ball.lose()
        score.r_increment()

screen.exitonclick()