import turtle as t
import random


timy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


directions = [0, 90, 180, 270]

timy.pensize(5)
timy.speed(0)

for _ in range(200):
    timy.color(random_color())
    timy.forward(30)
    timy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
