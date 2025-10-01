
# cd /Users/rayametche/PycharmProjects/MYProjects && python3 PingPongGame.py

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off screen updates for better performance

# Create the paddles
left_paddle = turtle.Turtle()
left_paddle.speed(2)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(2)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1  # Ball movement in x direction
ball.dy = 0.1  # Ball movement in y direction

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

# Initialize scores
left_score = 0
right_score = 0

# Paddle movement functions
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:  # Prevent paddle from going off screen
        y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -250:  # Prevent paddle from going off screen
        y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:  # Prevent paddle from going off screen
        y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -250:  # Prevent paddle from going off screen
        y -= 20
    right_paddle.sety(y)

# Keyboard bindings
screen.listen()
screen.onkey(left_paddle_up, "w")
screen.onkey(left_paddle_down, "s")
screen.onkey(right_paddle_up, "Up")
screen.onkey(right_paddle_down, "Down")

def update_score():
    score_display.clear()
    score_display.write(f"Left Player: {left_score}  Right Player: {right_score}", 
                       align="center", font=("Arial", 24, "normal"))

def reset_ball():
    ball.goto(0, 0)
    ball.dx *= random.choice([-1, 1])  # Random direction
    ball.dy *= random.choice([-1, 1])

# Initial score display
update_score()

# Main game loop
try:
    while True:
        screen.update()
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # Ball collision with top and bottom walls
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1
        
        # Ball goes off the left side
        if ball.xcor() < -390:
            right_score += 1
            update_score()
            reset_ball()
        
        # Ball goes off the right side
        if ball.xcor() > 390:
            left_score += 1
            update_score()
            reset_ball()
        
        # Ball collision with paddles
        # Right paddle collision
        if (ball.xcor() > 340 and ball.xcor() < 350 and 
            ball.ycor() < right_paddle.ycor() + 60 and 
            ball.ycor() > right_paddle.ycor() - 60):
            ball.setx(340)
            ball.dx *= -1
        
        # Left paddle collision
        if (ball.xcor() < -340 and ball.xcor() > -350 and 
            ball.ycor() < left_paddle.ycor() + 60 and 
            ball.ycor() > left_paddle.ycor() - 60):
            ball.setx(-340)
            ball.dx *= -1

except turtle.Terminator:
    pass  # Handle window closing gracefully
