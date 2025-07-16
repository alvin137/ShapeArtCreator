import tkinter as tk
from typing import Callable, Any

#Widget Wrapper
class Widget:
    def setPos(self, row: int, column: int):
        self.row = row
        self.column = column
        return self

    def setSize(self, size: int):
        self.size = size
        return self
    
    def setWidget(self, widget: tk.Widget):
        self.widget = widget
        return self
    
    def setParent(self, widget: tk.Widget):
        self.parent = widget
        return self
    
    def setRoot(self, root: tk.Tk):
        self.parent = root
        return self
    
    def assemble(self):
        pass

class LabelWidget(Widget):
    def __init__(self, text: str):
        self.text = text

    def assemble(self):
        self.setWidget(tk.Label(self.parent, text= self.text))

class StringVarLabelWidget(LabelWidget):
    def __init__(self, text: tk.StringVar):
        self.text = text
    
    def assemble(self):
        self.setWidget(tk.Label(self.parent, textvariable=self.text))


class ButtonWidget(Widget):
    def __init__(self, text: str, func: Callable[[], Any]):
        self.text =text
        self.func = func
    
    def assemble(self):
        self.setWidget(tk.Button(self.parent, text= self.text, command= self.func))

class EntryWidget(Widget):
    def __init__(self, value: tk.StringVar):
        self.value = value
        
    def assemble(self):
        self.setWidget(tk.Entry(self.parent, textvariable=self.value))

    def getValue(self):
        return self.value
    
class OptionMenuWidget(Widget):
    def __init__(self, value: tk.StringVar, options: list[str]):
        self.value = value
        self.options = options
        self.value.set(options[0])

    def assemble(self):
        self.setWidget(tk.OptionMenu(self.parent, self.value, *self.options))

    def getValue(self):
        return self.value
    
class CanvasWidget(Widget):
    def __init__(self, sizeX: int, sizeY: int, afterCreate: Callable[[tk.Canvas], Any]):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.afterCreate = afterCreate

    def assemble(self):
        self.setWidget(tk.Canvas(self.parent, width=self.sizeX, height=self.sizeY))
        self.afterCreate(self.widget) # type: ignore

class FrameWidget(Widget):
    def assemble(self):
        self.setWidget(tk.Frame(self.parent))

    