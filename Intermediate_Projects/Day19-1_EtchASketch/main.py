from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
 
def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def move_counter_clockwise():
    turtle.left(10)

def move_clockwise():
    turtle.right(10)

def clear_drawing():
    turtle.clear()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
