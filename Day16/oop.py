from turtle import Turtle, Screen

tony = Turtle()
print(tony)
tony.shape("turtle")
tony.color("chocolate3")

for _ in range(3):
    tony.forward(100)
    tony.left(120)
    tony.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
