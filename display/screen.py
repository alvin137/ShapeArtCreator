import tkinter as tk
from .widget import *

#Class for a screen
class Screen:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.widgets: dict[str, Widget] = dict()
        self.datas: dict[str, tk.Variable] = dict()

    def addWidget(self,tag: str, widget: Widget):
        self.widgets[tag] = widget
   
    def updateScreen(self):
        for e in self.widgets.values():
            e.assemble()
            e.widget.grid(row= e.row, column= e.column)

    def clearScreen(self):
        for e in self.widgets.values():
            print(e)
            e.widget.destroy()
        print(self.widgets.values())

    def getData(self, tag: str):
        return self.datas[tag]
    
    def setData(self, tag: str, value: Any):
        self.datas[tag] = value
