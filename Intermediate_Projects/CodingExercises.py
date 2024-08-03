import random
import math
from turtle import Turtle, Screen


def turtle_practice():
    timmy_the_turtle = Turtle()
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.color("red")
    timmy_the_turtle.pencolor("red")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(94)

def turtle_draw_square():
    square_turtle = Turtle()
    square_turtle.shape("turtle")
    square_turtle.color("green")
    for _ in range(4):
        square_turtle.forward(200)
        square_turtle.right(90)

def turtle_draw_dashed_line():
    dashed_turtle = Turtle()
    dashed_turtle.shape("turtle")
    dashed_turtle.color("green")
    for _ in range(20):
        dashed_turtle.forward(10)
        dashed_turtle.penup()
        dashed_turtle.forward(10)
        dashed_turtle.pendown()

def turtle_draw_multishapes():
    ms_turtle = Turtle()
    ms_turtle.shape("turtle")

    shape_sides = 3
    while shape_sides < 10:
        ms_turtle.color(random.randrange(0, 256)/255.0, random.randrange(0, 256)/255.0, random.randrange(0, 256)/255.0)
        for _ in range(shape_sides):
            ms_turtle.forward(100)
            ms_turtle.right(360/shape_sides)
        shape_sides += 1

def turtle_draw_randomwalk():
    rw_turtle = Turtle()
    rw_turtle.pensize(15)
    rw_turtle.speed(9)
    steps = 100
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        rw_turtle.color(random.randrange(0, 256)/255.0, random.randrange(0, 256)/255.0, random.randrange(0, 256)/255.0)
        rw_turtle.forward(20)
        rw_turtle.setheading(random.choice(directions))

def turtle_draw_spirograph():
    sg_turtle = Turtle()
    sg_turtle.speed(0)
    size = 5
    for _ in range (int(360 / size)):
        sg_turtle.color(random.randrange(0, 256)/255.0, random.randrange(0, 256)/255.0, random.randrange(0, 256)/255.0)
        sg_turtle.circle(100)
        sg_turtle.setheading(sg_turtle.heading() + size)

screen = Screen()
screen.exitonclick()
