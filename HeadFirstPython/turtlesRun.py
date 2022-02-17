import turtle
import random

turtles = list()


def setup():
    global turtles
    startline = -740
    screen = turtle.Screen()
    screen.setup(1500, 800)

    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ["red", "black", "green", "blue", "yellow"]
    for i in range(len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)


def race():
    global turtles
    winner = False
    finishline = 700

    while not winner:
        for current_turtle in turtles:
            move = random.randint(0, 2)
            current_turtle.forward(move)
            xcor = current_turtle.xcor()
            if xcor >= finishline:
                winner = True
                winner_color = current_turtle.color()
                print(f"Winner is {winner_color[0]}")


setup()
race()
turtle.mainloop()
