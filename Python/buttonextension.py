from math import *
import random

from tkinter import *
from turtle import *
from math import *
from random import *
intnum = 0
counter = 0
master = Tk()
master.geometry('600x600+600+200')
master.title("Sunil Jain's Window")

def windowstuff():
        counter = 0

def controlturtle():
    setup(600, 600)
    Screen()
    title("Control The Turtle")
    t = Turtle()
    x = 0
    y = 0

    
    window.geometry("550x550+0+200")
    window.title("Control the Turtle")
    controls = Label(window, text="Controls:")
    controls.pack()
    instructionlabel = Label(window, text="- WASD is to move the turtle, , ")
    instructionlabel.pack()
    instructionlabel1 = Label(window, text="- v and i is to toggle visibility")
    instructionlabel1.pack()
    instructionlabel3 = Label(window, text="- c is to clear the board")
    instructionlabel3.pack()        
    instructionlabel2 = Label(window, text="- change colors with numbers")
    instructionlabel2.pack()

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

    window.mainloop()

def addCalc():
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    x = (a+b)
    print("your answer is: ", x)

def subCalc():
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    x = (a-b)
    print("your answer is: ", x)

def multiplyCalc():
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    x = (a*b)
    print("your answer is: ", x)

def divisionCalc():
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    x = (a/b)
    print("your answer is: ", x)

def averageCalc():
    count = 1
    x = 0
    while(count):
        intnum = input("What Number? ")
        if (intnum[0] == "q"):
            break
        else:
            x = x + int(intnum)
            print(x/count)
            count = count + 1

def Pyglatin():
        pyg = 'ay'

        original = input('Enter a word:')

        if len(original) > 0 and original.isalpha():
            word = original.lower()
            first = word[0]
            if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
                new_word = word + pyg
                print(new_word)
            else:
                new_word = word[1:] + first + pyg
                print (new_word)
        else:
            print ('empty')

def advancedAverageCalc():
    x = 0
    count = 1
    intnum = 0

    while (count):
       intnum = input("What Number? ")
       if (intnum[0] == "q"):
          break
       else:
          x = x + int(intnum)
          print(x/count)
       count = count + 1

def tkinter_tutorial1():
        tkinter_tutorial1 = Tk()
        tkinter_tutorial1.geometry("550x550+0+200")
        tkinter_tutorial1.title("Moving The Turtle")
        tkinter_tutorial1 = Text(tkinter_tutorial1, text="First you need to create the actual tkinter window. The way you do that is ")

def donothing():
   p = 0
 
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.quit)
menubar.add_cascade(label="File", menu=filemenu)
 
calculators = Menu(menubar, tearoff=0)
calculators.add_command(label="Advanced Average Calculator", command=advancedAverageCalc)
calculators.add_separator()
calculators.add_command(label="Average Calculator", command=averageCalc)
calculators.add_separator()
calculators.add_command(label="Division", command=divisionCalc)
calculators.add_separator()
calculators.add_command(label="Multiplication", command=multiplyCalc)
calculators.add_separator()
calculators.add_command(label="Subtraction", command=subCalc)
calculators.add_separator()
calculators.add_command(label="Addition", command=addCalc)
calculators.add_separator()
menubar.add_cascade(label="Calculators", menu=calculators)
 
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Duplicate Line", command=donothing)
editmenu.add_command(label="Toggle Case", command=tkinter_tutorial1)
menubar.add_cascade(label="Edit",menu=editmenu)
 
master.config(menu=menubar)

b = Button(master, text="Exit", command=master.destroy, background="black", fg="red", height=1, width=5)
b.pack()
b2 = Button(master, text="Control Turtle", command=controlturtle, background="white", fg="black", height=1, width=30)
b2.pack()
b3 = Button(master, text="Add Calculator", command=addCalc, background="white", fg="black", height=1, width=30)
b3.pack()
b4 = Button(master, text="Subtract Calculator", command=subCalc, background="white", fg="black", height=1, width=30)
b4.pack()
b5 = Button(master, text="multiply Calculator", command=multiplyCalc, background="white", fg="black", height=1, width=30)
b5.pack()
b6 = Button(master, text="Division Calculator", command=divisionCalc, background="white", fg="black", height=1, width=30)
b6.pack()
b7 = Button(master, text="Average Calculator", command=averageCalc, background="white", fg="black", height=1, width=30)
b7.pack()
b8 = Button(master, text="Advanced Average Calculator", command=advancedAverageCalc, background="white", fg="black", height=1, width=30)
b8.pack()
b9 = Button(master, text="Pyglatin word Converter", command=Pyglatin, background="white", fg="black", height=1, width=30)
b9.pack()

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

label = Label(master, fg="red", height=1, width=600,bg="black")
label.pack(side=BOTTOM)
counter_label(label)

S = Scrollbar(master)
T = Text(master, height=4, width=50)
S.pack(side=RIGHT)
T.pack(side=LEFT, fill=X)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
stufzz = "yuy"
exit_out = Button(master, text="quit", command=master.destroy)
exit_out.pack()
T.insert(END, stufzz)
mainloop()

master.mainloop()
mainloop()
