import tkinter as tk
from widget import *

#Class for a screen
class Screen:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.widgets: dict[str, Widget] = dict()

    def addWidget(self,tag: str, widget: Widget):
        self.widgets[tag] = widget

    def addButton(self, tag: str, text: str, func: Callable[[], Any]):
        self.addWidget(tag, ButtonWidget(self.root, text, func))

    def addLabel(self, tag: str, text: str):
        self.addWidget(tag, LabelWidget(self.root, text))
   
    def updateScreen(self):
        for e in self.widgets.values():
            e.assemble()
            e.widget.grid(row= e.row, column= e.column)

    def clearScreen(self):
        for e in self.widgets.values():
            print(e)
            e.widget.destroy()
        print(self.widgets.values())
