# Create a 'painting' with turtle module, with 10x10 spots using the colors from color_list.
# dots should be 20 in size and spaced 50 apart

import turtle as t
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)

turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

start_x = -250
start_y = -250

turtle.goto(start_x, start_y)

for y in range(10):
    for x in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)
    turtle.goto(start_x, start_y + (y + 1) * 50 )

screen.exitonclick()