import tkinter as tk
from typing import Callable, Any

#Widget Wrapper
class Widget:
    def __init__(self, root: tk.Tk):
        self.root = root

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
    
    def assemble(self):
        pass

class LabelWidget(Widget):
    def __init__(self, root: tk.Tk, text: str):
        super().__init__(root)
        self.text = text

    def assemble(self):
        self.setWidget(tk.Label(self.root, text= self.text))

class StringVarLabelWidget(LabelWidget):
    def __init__(self, root: tk.Tk, text: tk.StringVar):
        super().__init__(root, text.get())
        self.text = text
    
    def assemble(self):
        self.setWidget(tk.Label(self.root, textvariable=self.text))


class ButtonWidget(Widget):
    def __init__(self,root: tk.Tk, text: str, func: Callable[[], Any]):
        super().__init__(root)
        self.text =text
        self.func = func
    
    def assemble(self):
        self.setWidget(tk.Button(self.root, text= self.text, command= self.func))

class EntryWidget(Widget):
    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.textValue: tk.StringVar = tk.StringVar()
        
    def assemble(self):
        self.setWidget(tk.Entry(self.root, textvariable=self.textValue))

    def getText(self):
        return self.textValue

    