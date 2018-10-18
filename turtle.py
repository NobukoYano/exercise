import turtle
#from turtle import Turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()


draw_square()
