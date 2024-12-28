from tkinter import *

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)#tearoff = elemento por defecto
editmenu = Menu(menubar)
helpmenu = Menu(menubar)

menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Nuevo")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.mainloop()