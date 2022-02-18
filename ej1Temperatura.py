from tkinter import *

vent = Tk()
vent.title("Temperatura")
vent.geometry("500x200")


def fnConvertir():
    centigrado = txt1.get()
    fahrenheit = 32 + (9 * (float(centigrado)/5)) 

    txt2.delete(0,'end')
    txt2.insert(0,fahrenheit)


lbl1 = Label(vent, text="Grados Centígrados:", bg="black", fg="white" )
txt1 = Entry(vent, bg="white")
btn1 = Button(vent, text="Convertir", command=fnConvertir)
lbl2 = Label(vent, text="Grados Fahrenheit", bg="black", fg="white")
txt2 = Entry(vent, bg="green", fg="white")



lbl1.place(x=10, y=10, width=125, height=30)
txt1.place(x=165, y=10, width=130, height=30)
btn1.place(x=320, y=10, width=100, height=30)
lbl2.place(x=10, y=50, width=125, height=30)
txt2.place(x=165, y=50, width=130, height=30)




vent.mainloop()