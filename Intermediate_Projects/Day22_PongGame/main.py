from turtle import Turtle, Screen
from paddle import Paddle

#Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Game Initialization
game_active = True

# Game Controls
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

#Game Loop
while game_active:
    screen.update()

screen.exitonclick()