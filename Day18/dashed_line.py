from turtle import Turtle, Screen

tom = Turtle()

# Draw a dashed line (10points draw, 10 points gap)

for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = Screen()
screen.exitonclick()
