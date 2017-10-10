from turtle import Turtle, Screen
import turtle


def set_up_window():
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    window.title("SHAPE PRESENTATION")

    # Show window in foreground.
    foreground = Screen()
    rootwindow = foreground.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')


def draw_circle():
    set_up_window()
    presentation_time = 4
    for i in range(presentation_time):
        turtle.circle(30)
    turtle.bye()


def draw_square():
    set_up_window()
    presentation_time = 3
    for i in range(presentation_time):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.bye()


def draw_rectangle():
    set_up_window()
    presentation_time = 3
    for i in range(presentation_time):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.bye()


def draw_triangle():
    set_up_window()
    presentation_time = 3
    for i in range(presentation_time):
        turtle.forward(320)
        turtle.left(120)
        turtle.forward(320)
        turtle.left(120)
        turtle.forward(320)
        turtle.left(120)
    turtle.bye()


def draw_star():
    set_up_window()
    for i in range(2):
        turtle.speed(0)
        for i in range(1):
            turtle.forward(100)
            turtle.left(175)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
            turtle.right(2)
    turtle.bye()


def draw_pentagon():
    set_up_window()
    presentation_time = 6
    for i in range(presentation_time):
        turtle.circle(40, steps=5)
    turtle.bye()
