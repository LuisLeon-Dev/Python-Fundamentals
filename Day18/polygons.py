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
]


def draw_polygon(turtle, sides, len):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(len)
        turtle.right(angle)


side = 3
while side <= 10:
    timy.color(random.choice(colors_list))
    draw_polygon(timy, side, 100)
    side += 1

screen = Screen()
screen.exitonclick()
