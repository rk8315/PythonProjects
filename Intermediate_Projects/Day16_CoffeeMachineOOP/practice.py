# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()

# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.align = "c"
table.field_names = ["Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Rodent"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

print(table)
