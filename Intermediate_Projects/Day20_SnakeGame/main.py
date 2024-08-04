from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

# Game Initialization
game_active = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Snake Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game Loop
while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect snake and food collision  
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect snake and wall collision
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -280:
        game_active = False
        scoreboard.game_over()
    
    # Detect snake and tail collision
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_active = False
            scoreboard.game_over()


screen.exitonclick()