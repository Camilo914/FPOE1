#hecho por: juan manuel quintero y juan camilo villa


import tkinter
from tkinter import messagebox


def evento1(evento):
      if not evento.char.isalpha():
        print("Error: Solo se permiten letras.", repr(evento.char))

def evento2(evento):
    if not (evento.char.isdigit() or evento.char == '/'):
        print("Error: Solo se permiten números.", repr(evento.char))

    

ventana=tkinter.Tk()
ventana.geometry("500x500")
ventana.title("formulario")

ventana2=tkinter.LabelFrame(ventana, width=400, height=300)
ventana2.grid(row=1, column=1) 

nombre=tkinter.Label(ventana2, text="nombre")
nombre.grid(row=1, column=1)

nombre2=tkinter.Entry(ventana2)
nombre2.grid(row=1, column=2)
nombre2.bind("<Key>", evento1)

apellido=tkinter.Label(ventana2, text="apellido")
apellido.grid(row=2, column=1)

apellido2=tkinter.Entry(ventana2)
apellido2.grid(row=2, column=2)
apellido2.bind("<Key>", evento1)

correo=tkinter.Label(ventana2, text="correo")
correo.grid(row=3, column=1)

correo2=tkinter.Entry(ventana2)
correo2.grid(row=3, column=2)

edad=tkinter.Label(ventana2, text="edad")
edad.grid(row=4, column=1)

edad2=tkinter.Entry(ventana2)
edad2.grid(row=4, column=2)
edad2.bind("<Key>", evento2)

fecha_nacimiento=tkinter.Label(ventana2, text="fecha de nacimiento")
fecha_nacimiento.grid(row=5, column=1)

fecha_nacimiento2=tkinter.Entry(ventana2)
fecha_nacimiento2.grid(row=5, column=2)
fecha_nacimiento2.bind("<Key>", evento2)



ventana.mainloop()