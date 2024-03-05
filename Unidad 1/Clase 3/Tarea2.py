#hecho por: juan manuel quintero y juan camilo villa


import tkinter
from tkinter import messagebox


def mostrar_error(mensaje):
    error_label.config(text=mensaje)


def evento1(evento):
    if not (evento.char.isalpha() or evento.char == ' ' or evento.char == 'supr'):
        mostrar_error("Error: Solo se permiten letras.")
        nombre2.delete("end", "insert")

def evento2(evento):
    if not (evento.char.isdigit() or evento.char == '/'):
        mostrar_error4("Error: Solo se permiten números.")
        edad2.delete("end", "insert")

def mostrar_error4(mensaje):
    error_label4.config(text=mensaje)



def evento5(evento):
    if not (evento.char.isdigit() or evento.char == '/'):
        mostrar_error5("Error: Solo se permiten números.")
        fecha_nacimiento2.delete("end", "insert")

def mostrar_error5(mensaje):
    error_label5.config(text=mensaje)

def mostrar_error2(mensaje):
    error_label2.config(text=mensaje)

def evento3(evento):
    if not (evento.char.isalpha() or evento.char == ' '):
        mostrar_error2("Error: Solo se permiten letras.")
        apellido2.delete("end", "insert")

def mostrar_error3(mensaje):
    error_label3.config(text=mensaje)

# esta funcion no nos dio
def evento4(texto_ingresado):
     texto_ingresado = correo2.get()

     lista_correo=["a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z . @ "]

     if texto_ingresado == lista_correo:
         pass
     else:
         mostrar_error3("error")
         correo2.delete("end", "insert")




        




ventana=tkinter.Tk()
ventana.geometry("700x700")
ventana.title("formulario")


nombre=tkinter.Label(ventana, text="nombre")
nombre.grid(row=1, column=1)

error_label = tkinter.Label(ventana, text="", fg="red")
error_label.grid(row=2, column=2)

nombre2=tkinter.Entry(ventana)
nombre2.grid(row=1, column=2)
nombre2.bind("<Key>", evento1)

apellido=tkinter.Label(ventana, text="apellido")
apellido.grid(row=3, column=1)

error_label2 = tkinter.Label(ventana, text="", fg="red")
error_label2.grid(row=4, column=2)

apellido2=tkinter.Entry(ventana)
apellido2.grid(row=3, column=2)
apellido2.bind("<Key>", evento3)

correo=tkinter.Label(ventana, text="correo")
correo.grid(row=5, column=1)

correo2=tkinter.Entry(ventana)
correo2.grid(row=5, column=2)
correo2.bind("<Key>", evento4)


error_label3 = tkinter.Label(ventana, text="", fg="red")
error_label3.grid(row=6, column=2)


edad=tkinter.Label(ventana, text="edad")
edad.grid(row=7, column=1)

error_label4 = tkinter.Label(ventana, text="", fg="red")
error_label4.grid(row=8, column=2)

edad2=tkinter.Entry(ventana)
edad2.grid(row=7, column=2)
edad2.bind("<Key>", evento2)

fecha_nacimiento=tkinter.Label(ventana, text="fecha de nacimiento")
fecha_nacimiento.grid(row=9, column=1)

error_label5 = tkinter.Label(ventana, text="", fg="red")
error_label5.grid(row=10, column=2)


fecha_nacimiento2=tkinter.Entry(ventana)
fecha_nacimiento2.grid(row=9, column=2)
fecha_nacimiento2.bind("<Key>", evento5)



ventana.mainloop()