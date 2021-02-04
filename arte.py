import turtle

def draw(turtle, length):
    if length > 0:
        turtle.forward(length)
        turtle.left(90)
        draw(turtle, length-10)


if __name__ == '__main__':
    blastoise = turtle.Turtle()
    field = turtle.Screen()
    draw(blastoise, 100)
    field.exitonclick()
