import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Padding One
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0)

# Paddle Two
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .4
ball.dy = .4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Move paddle_one up by 20 pixels
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

# Move paddle_one down by 20 pixels
def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

# Move paddle_two up by 20 pixels
def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

# Move paddle_two down by 20 pixels
def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_one_up, "w") # Call paddle_one_up when w is pressed
window.onkeypress(paddle_one_down, "s") # Call paddle_one_up when s is pressed
window.onkeypress(paddle_two_up, "Up") # Call paddle_two_up when the up arrow is pressed
window.onkeypress(paddle_two_down, "Down") # Call paddle_two_up when the down arrow is pressed


# Main game loop
while True:
    window.update()

    # Move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Bottom Border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Right Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Left Border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Right Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_two.ycor() + 40 and ball.ycor() > paddle_two.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # Left Paddle and ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_one.ycor() + 40 and ball.ycor() > paddle_one.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")