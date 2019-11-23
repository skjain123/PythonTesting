from tkinter import *
from turtle import *

setup(550, 550)
Screen()
title("Control The Turtle")
t = Turtle()
x = 0
y = 0

window = Tk()
window.geometry("550x550")
window.title("Test")

def left(event):
    t.left(45)
def back(event):
    t.back(45)
def forward(event):
    t.forward(45)
def right(event):
    t.right(45)
def clear(event):
    t.goto(x,y)
    t.clear()
    t.color("black")
def red(event):
    t.color("red")
def blue(event):
    t.color("blue")
def yellow(event):
    t.color("yellow")
def cyan(event):
    t.color("cyan")
def green(event):
    t.color("green")
def magenta(event):
    t.color("magenta")
def orange(event):
    t.color("orange")
def black(event):
    t.color("black")
def invisible(event):
    t.hideturtle()
def notinvisible(event):
    t.showturtle()

def quitting(event):
    quit()

window.bind("a", left)
window.bind("s", back)
window.bind("d", right)
window.bind("w", forward)
window.bind("c", clear)
window.bind("1", red)
window.bind("2", blue)
window.bind("3", yellow)
window.bind("4", cyan)
window.bind("5", green)
window.bind("6", magenta)
window.bind("7", orange)
window.bind("8", black)
window.bind("v", invisible)
window.bind("i", notinvisible)
window.bind("q", quitting)

window.mainloop()
