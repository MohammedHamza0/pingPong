     
import turtle
import math

# Setup the window game
window = turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor(0.1, 0.1, 0.1)
window.setup(width=800, height=600)
window.tracer(0)

# Global variables
ball_speed = 1
score1 = 0
score2 = 0

# Ball setup
ball = turtle.Turtle()
ball.penup()
ball.color("white")
ball.shape("circle")
ball_dx, ball_dy = 1, 1

# Player setup
def create_player(color, position):
    player = turtle.Turtle()
    player.penup()
    player.color(color)
    player.shape("square")
    player.shapesize(stretch_len=1, stretch_wid=4)
    player.setposition(position)
    return player

player1 = create_player("red", (350, 0))
player2 = create_player("blue", (-360, 0))

# Movement functions
def move_player(player, dy):
    new_y = player.ycor() + dy
    if -255 < new_y < 260:
        player.sety(new_y)

def move_player1_up(): move_player(player1, 50)
def move_player1_down(): move_player(player1, -50)
def move_player2_up(): move_player(player2, 50)
def move_player2_down(): move_player(player2, -50)

# Center line
center_line = turtle.Turtle()
center_line.penup()
center_line.setposition(0, 0)
center_line.pendown()
center_line.color("white")
center_line.shape("square")
center_line.shapesize(stretch_len=.1, stretch_wid=25)

# Score display
score_display = turtle.Turtle()
score_display.penup()
score_display.setposition(-140, 260)
score_display.pendown()
score_display.color("white")
score_display.hideturtle()

def update_score():
    score_display.clear()
    score_display.write(f"Player2: {score1} | Player1: {score2}", align="left", font=("Arial", 22, "normal"))

update_score()

# Take the user input
window.listen()
window.onkey(move_player1_up, "Up")
window.onkey(move_player1_down, "Down")
window.onkey(move_player2_up, "w")
window.onkey(move_player2_down, "s")

# Function to check if the player hits the ball
def is_pushed(ball, player):
    return abs(ball.xcor() - player.xcor()) < 20 and abs(ball.ycor() - player.ycor()) < 50

# Game loop
while True:
    window.update()
    # Move the ball
    ball.setx(ball.xcor() + ball_dx * ball_speed)
    ball.sety(ball.ycor() + ball_dy * ball_speed)
    
    # Ball collision with top/bottom walls
    if abs(ball.ycor()) > 290:
        ball_dy *= -1
        ball.sety(290 if ball.ycor() > 0 else -290)

    # Ball collision with players
    if is_pushed(ball, player1) or is_pushed(ball, player2):
        ball_dx *= -1

    # Scoring logic
    if ball.xcor() > 385:
        ball.setposition(0, 0)
        ball_dx *= -1
        score1 += 1
        update_score()
        
    elif ball.xcor() < -385:
        ball.setposition(0, 0)
        ball_dx *= -1
        score2 += 1
        update_score()
