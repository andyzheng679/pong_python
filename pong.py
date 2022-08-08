import turtle

# setting up 
wn = turtle.Screen()
wn.title("Pong in Python")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# creating the left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# creating the left paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# creating the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.xspeed = .3
ball.yspeed = -.3

# moving the paddles
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")


while True:
    wn.update()


    # moving ball
    ball.setx(ball.xcor() + ball.xspeed)
    ball.sety(ball.ycor() + ball.yspeed)

    # borders

    # top and botton borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.yspeed *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yspeed *= -1

    # right and left ball reset 
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.xspeed *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.xspeed *= -1

    #
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() -50):
        ball.setx(340)
        ball.xspeed *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() -50):
        ball.setx(-340)
        ball.xspeed *= -1
