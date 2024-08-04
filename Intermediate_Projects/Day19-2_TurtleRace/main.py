from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Epic Turtle Racing")
is_race_started = False
user_choice = screen.textinput(title="Choose your champion", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_started = True

while is_race_started:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_started = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_choice:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()