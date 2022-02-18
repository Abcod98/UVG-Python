from cProfile import label
from tkinter import *

def miFuncion():
    print("Mensaje de boton")


ventana = Tk()
ventana.title("UVG_Python")
ventana.geometry("400x300")

lbl = Label(ventana, text="Job Abraham Tun Sanchez")
lbl.config(bg="black", fg="white")
lbl.pack()

btn = Button(ventana, text="Presionar", fg="white" ,bg = "green", command = miFuncion)
btn.pack()

ventana.mainloop()