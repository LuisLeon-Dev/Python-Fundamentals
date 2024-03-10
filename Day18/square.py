from turtle import Turtle, Screen

tomy = Turtle()

# Draw a square 100x100
for _ in range(4):
    tomy.forward(100)
    tomy.left(90)

screen = Screen()
screen.exitonclick()
