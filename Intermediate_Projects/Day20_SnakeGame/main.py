from turtle import Turtle, Screen

#Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Game Initialization
game_active = True

# Initial Snake
total_snake = []
for snake in range(0, 3):
    segment = Turtle("square")
    segment.color("white")
    segment_position = snake * -20
    segment.goto(segment_position, 0)
    total_snake.append(segment)

while game_active:
    pass






screen.exitonclick()