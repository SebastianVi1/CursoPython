from tkinter import *
def sumar():
    r.set(float(n1.get())+ float(n2.get()))

def vaciar():
    n1.set("")
    n2.set("")
    r.set("")
root = Tk()

n1 = StringVar()
n2 = StringVar()
r = StringVar()
Label(root, text="Numero 1: ").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Numero 2: ").pack()
Entry(root, justify="center", textvariable=n2).pack()

boton_sumar = Button(root, text="Sumar", command=sumar, padx=10, pady=10).pack()
boton_vaciar = Button(root, text="Vaciar", command=vaciar).pack()
Entry(root, textvariable=r, justify="center", state="readonly").pack()
root.mainloop()