import turtle

#setting up 
wn = turtle.Screen()
wn.title("Pong in Python")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#creating the left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

#creating the left paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

#creating the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


while True:
    wn.update()