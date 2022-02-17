import turtle

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("blue")
rafael = turtle.Turtle()
rafael.shape("turtle")
rafael.color("red")
donatello = turtle.Turtle()
donatello.shape("turtle")
donatello.color("green")


def make_square(the_turtle):
    for i in range(4):
        the_turtle.forward(100)
        the_turtle.right(90)


def make_spiral(the_turtle):
    for i in range(36):
        make_square(the_turtle)
        the_turtle.right(10)


donatello.penup()
donatello.setposition(-380, 320)
donatello.right(40)
donatello.pendown()
donatello.pencolor("green")
donatello.forward(990)

# make_spiral(leonardo)
# rafael.right(5)
# make_spiral(rafael)

turtle.mainloop()
