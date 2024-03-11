import turtle as t
import random

timy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def draw_circles(angle):
    gap = int(360 / angle)
    for _ in range(gap):
        timy.color(random_color())
        timy.circle(100)
        timy.left(angle)


timy.speed(0)
draw_circles(5)


screen = t.Screen()
screen.exitonclick()
