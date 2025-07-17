import turtle
from .screen import Screen
from .widget import LabelWidget, EntryWidget, FrameWidget, ButtonWidget, CanvasWidget, StringVarLabelWidget, OptionMenuWidget #type: ignore
from tkinter import Tk, IntVar, StringVar, colorchooser, Canvas, Frame, PhotoImage
import animation
from .drawing import *

def changeScreen(a: Screen, b: Screen):
    global t
    a.clearScreen()
    b.updateScreen()
    animation.clear(canvas) #type: ignore
    animation.ask_again(canvas, root, dog_img) #type: ignore
    frame2.grid_remove()
    #why removing
    t = turtle.RawTurtle(canvas)
    t.showturtle()

def drawSomething():
    shape = shapeScreen.getData("shapeOption").get()#type: ignore
    outline = shapeScreen.getData("shapeOutlineColor").get()#type: ignore
    fill = shapeScreen.getData("shapeFillColor").get()#type: ignore
    x = shapeScreen.getData("shapeX").get()#type: ignore
    y = shapeScreen.getData("shapeY").get()#type: ignore
    radius = shapeScreen.getData("shapeRadius").get() #type: ignore
    if shape == "Circle" : #type: ignore
        draw_circle(t, radius, outline, fill, x, y) #type: ignore
    else:
        edges = 3 if shape == "Triangle" else 4 if shape == "Square" else 6
        draw_polygon(t, edges, radius, outline, fill, x, y) #type: ignore

def openColorWindow(title: str, tag: str):
    initialColor = shapeScreen.getData(tag).get() # type: ignore
    shapeScreen.getData(tag).set(colorchooser.askcolor(title=title, color= initialColor)[1]) # type: ignore

root= Tk()

nameScreen = Screen(root)
shapeScreen = Screen(root)

frame = Frame(root)
frame.grid(row= 0, column= 0)

frame2 = Frame(root)
frame2.grid(row=0, column = 0)

canvas = Canvas(root, width=500, height=500)
canvas.grid(row= 0, column = 1)

t = turtle.RawTurtle(canvas)
t.speed(2)
t.hideturtle()

dog_img = PhotoImage(file="dog.gif").subsample(10, 10)

nameScreen.addWidget("nameLabel", LabelWidget("Name: ").setPos(0, 0).setParent(frame2))

nameScreen.setData("name", StringVar())
nameScreen.addWidget("nameEntry", EntryWidget(nameScreen.getData("name")).setPos(0, 1).setParent(frame2)) # type: ignore

nameScreen.addWidget("okButton", ButtonWidget("Ok", lambda : changeScreen(nameScreen, shapeScreen)).setPos(1, 1).setParent(frame2))

shapeScreen.setData("shapeOption", StringVar())
shapeScreen.setData("shapeOutlineColor", StringVar())
shapeScreen.setData("shapeFillColor", StringVar())
shapeScreen.setData("shapeX", IntVar())
shapeScreen.setData("shapeY", IntVar())
shapeScreen.setData("shapeRadius", IntVar())

shapeScreen.addWidget("shapeLabel", LabelWidget("Select Shape: ").setPos(0, 0).setParent(frame))
shapeScreen.addWidget("shapeOptionMenu", OptionMenuWidget(shapeScreen.getData("shapeOption"), ["Triangle", "Square", "Circle", "Hexagon"]).setPos(0, 1).setParent(frame)) #type: ignore
shapeScreen.addWidget("shapeOutlineColorLabel", LabelWidget("Select outline color: ").setPos(1, 0).setParent(frame))
shapeScreen.addWidget("shapeOutlineColorButton", ButtonWidget("Select", lambda : openColorWindow("test", "shapeOutlineColor")).setPos(1, 1).setParent(frame))
shapeScreen.addWidget("shapeFillColorLabel", LabelWidget("Select fill color: ").setPos(2, 0).setParent(frame))
shapeScreen.addWidget("shapeFillColorButton", ButtonWidget("Select", lambda : openColorWindow("test2", "shapeFillColor")).setPos(2, 1).setParent(frame))
shapeScreen.addWidget("shapeXLabel", LabelWidget("X: ").setPos(3, 0).setParent(frame))
shapeScreen.addWidget("shapeXEntry", EntryWidget(shapeScreen.getData("shapeX")).setPos(3, 1).setParent(frame)) #type: ignore
shapeScreen.addWidget("shapeYLabel", LabelWidget("Y: ").setPos(3, 2).setParent(frame))
shapeScreen.addWidget("shapeYEntry", EntryWidget(shapeScreen.getData("shapeY")).setPos(3, 3).setParent(frame)) #type: ignore
shapeScreen.addWidget("shapeSizeLabel", LabelWidget("Radius/Length: ").setPos(4, 0).setParent(frame))
shapeScreen.addWidget("shapeSizeEntry", EntryWidget(shapeScreen.getData("shapeRadius")).setPos(4, 1).setParent(frame)) #type: ignore
shapeScreen.addWidget("confirmButton", ButtonWidget("Confirm", drawSomething).setPos(5, 5).setParent(frame))

nameScreen.updateScreen()
#root.mainloop()