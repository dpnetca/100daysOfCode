# import turtle


# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse3")
# timmy.forward(100)

# my_screen = turtle.Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# change to left align
table.align = "l"

print(table)
