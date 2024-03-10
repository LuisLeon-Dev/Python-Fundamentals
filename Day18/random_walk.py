from turtle import Turtle, Screen
import random

# draw a triangule, square, pentagone, hexagon, heptagon
# octagon, nonagon and decagon
timy = Turtle()

colors_list = [
    "DeepPink",
    "DarkRed",
    "coral3",
    "DarkOrange2",
    "chartreuse",
    "CornflowerBlue",
    "DarkOrchid2",
    "DarkOliveGreen4",
    "chocolate",
    "brown2",
    "aquamarine",
    "DarkSlateBlue",
]
directions = [0, 90, 180, 270]

timy.pensize(5)
timy.speed(0)
for _ in range(200):
    timy.color(random.choice(colors_list))
    timy.forward(30)
    timy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
