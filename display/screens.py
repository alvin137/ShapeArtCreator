from screen import *
import typing

def clearScreenAndChangeTo():
    a.clearScreen()
    b.updateScreen()

def clearAndChangeTo():
    b.clearScreen()
    a.updateScreen()
    

root= tk.Tk()
a = Screen(root)
b = Screen(root)
rootb = tk.Tk()

a.addWidget("aaa", LabelWidget(root=root, text= "asdf").setPos(0, 0))
b.addWidget("asdf", LabelWidget(root= root, text= "asdfasdf").setPos(1, 0))

a.addWidget("aaa2", ButtonWidget(root, "asdfasfasdf", clearScreenAndChangeTo).setPos(2, 0))

b.addWidget("aaa3", ButtonWidget(root, "asdfasdfsadf", clearAndChangeTo).setPos(1, 0))

b.addWidget("entryTest", EntryWidget(root).setPos(1, 1))
b.addWidget("entryLabelTest", StringVarLabelWidget(root, typing.cast(EntryWidget, b.widgets["entryTest"]).getText()).setPos(2, 1))
#b.addWidget("entryButtonTest", ButtonWidget(root, "Entry Test", lambda : print(typing.cast(LabelWidget, b.widgets["entryLabelTest"]).update())).setPos(3, 1))

a.updateScreen()

root.mainloop()