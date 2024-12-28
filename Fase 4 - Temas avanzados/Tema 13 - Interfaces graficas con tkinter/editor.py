from tkinter import *
from tkinter import filedialog
from io import open
ruta = ""#almacenamiento de la ruta del fichero
def nuevo():
    global ruta#asignamos la variable a global para que no halla problemas con la memoria
    mensaje.set("Nuevo archivo")
    ruta = ""
    texto.delete(1.0, "end")#se borra el texto desde el caracter 1 hasta el final


def abrir():
	global ruta
	mensaje.set("Abrir fichero")
	ruta = filedialog.askopenfilename(
		initialdir='.', 
		filetype=(("Ficheros de texto", "*.txt"),),
		title="Abrir un fichero de texto")

	if ruta != "":
		fichero = open(ruta, 'r')
		contenido = fichero.read()
		texto.delete(1.0,'end')
		texto.insert('insert', contenido)
		fichero.close()
		root.title(ruta + " - Mi editor")


def guardar():
    global ruta
    mensaje.set("Guardar archivo....")
    if ruta != "":
        contenido = texto.get(1.0, "end")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        mensaje.set("Fichero guardado correctamente...")
        fichero.close()
    else:
        guardar_como()

def guardar_como():
    mensaje.set("Guardando archivo como...")





root = Tk()
root.title("Editor de texto")

menubar = Menu(root)
root.config(menu=menubar)



filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)

#Campo de texto
texto = Text(root)
texto.pack(fill="both", expand="1")
texto.config(bd=2, padx=10, pady=10, )

#texto de la parte inferior
mensaje = StringVar()
monitor = Label(root, textvariable=mensaje,justify="left").pack(side="left")
mensaje.set("Bienvenido a tu editor de texto")
root.mainloop()