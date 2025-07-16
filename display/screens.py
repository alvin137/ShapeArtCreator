from screen import *
from tkinter import Variable, IntVar, StringVar, colorchooser, Canvas, Frame # type: ignore

def changeScreen(a: Screen, b: Screen):
    a.clearScreen()
    b.updateScreen()

def openColorWindow(title: str, tag: str):
    shapeScreen.getData(tag).set(colorchooser.askcolor(title=title)[1]) # type: ignore

def canvasTest(c: Canvas):
    c.columnconfigure(0, weight=1)
    c.create_rectangle(10, 10, 100, 100)
    
    c.grid(sticky='NSEW')

def sendSomething():
    print("SendingMessageidk")


root= tk.Tk()

nameScreen = Screen(root)
shapeScreen = Screen(root)

frame = Frame(root)
frame.grid(row= 0, column= 0)

frame2 = Frame(root)
frame2.grid()

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
shapeScreen.addWidget("shapeFillColorLabel", LabelWidget("Select outline color: ").setPos(2, 0).setParent(frame))
shapeScreen.addWidget("shapeFillColorButton", ButtonWidget("Select", lambda : openColorWindow("test", "shapeFillColor")).setPos(2, 1).setParent(frame))
shapeScreen.addWidget("shapeXLabel", LabelWidget("X: ").setPos(3, 0).setParent(frame))
shapeScreen.addWidget("shapeXEntry", EntryWidget(shapeScreen.getData("shapeX")).setPos(3, 1).setParent(frame)) #type: ignore
shapeScreen.addWidget("shapeYLabel", LabelWidget("Y: ").setPos(3, 3).setParent(frame))
shapeScreen.addWidget("shapeYEntry", EntryWidget(shapeScreen.getData("shapeY")).setPos(3, 4).setParent(frame)) #type: ignore
shapeScreen.addWidget("shapeSizeLabel", LabelWidget("Radius/Length: ").setPos(4, 0).setParent(frame))
shapeScreen.addWidget("shapeSizeEntry", EntryWidget(shapeScreen.getData("shapeRadius")).setPos(4, 1).setParent(frame)) #type: ignore
shapeScreen.addWidget("confirmButton", ButtonWidget("Confirm", sendSomething).setPos(5, 5).setParent(frame))
shapeScreen.addWidget("testCanvas", CanvasWidget(500, 500, canvasTest).setPos(0, 1).setRoot(root))





# outline = input("Enter outline color: ")
#     fill = input("Enter fill color: ")
#     x = int(input("Enter X position: "))
#     y = int(input("Enter Y position: "))

#     if sides == 0:
#         radius = int(input("Enter radius: "))
#         draw_circle(radius, outline, fill, x, y)
#     else:
#         length = int(input("Enter side length: "))
#         draw_polygon(sides, length, outline, fill, x, y)

#     again = input("Draw another? (yes/no): ").lower()
#     if again != "yes":
#         break


nameScreen.updateScreen()
root.mainloop()