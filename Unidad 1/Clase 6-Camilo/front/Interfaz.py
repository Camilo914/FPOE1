import tkinter as tk
from tkinter import messagebox
import re

import requests

response = requests.get("http://localhost:8000")


def validar_informacion():   

    
    # Obtener el texto de cada campo de entrada
    modelo = modelo2.get()
    gb_ram = gb_ram2.get()
    tipo_pantalla = Pantalla2.get()
    nombre_procesador = Procesador2.get()
    
    # Validar modelo (solo letras)
    if not re.match("^[a-zA-Z0-9]+$", modelo):
        messagebox.showerror("Error", "El modelo solo debe contener letrad y numeros.")
        return
    
    # Validar gb_ram (solo números y letras)
    if not re.match("^[0-9]+$", gb_ram):
        messagebox.showerror("Error", "La cantidad de RAM solo debe contener números.")
        return
    
    # Validar tipo_pantalla (solo números y letras)
    if not re.match("^[a-zA-Z0-9]+$", tipo_pantalla):
        messagebox.showerror("Error", "El tipo de pantalla solo debe contener números y letras.")
        return
    
    # Validar nombre_procesador (solo números y letras)
    if not re.match("^[a-zA-Z0-9]+$", nombre_procesador):
        messagebox.showerror("Error", "El nombre del procesador solo debe contener números y letras.")
        return 
    
    # Si todas las validaciones pasan, mostrar mensaje de éxito
    modelo_valido= re.match("^[a-zA-Z0-9]+$", modelo2.get())
    gb_ram_valida= re.match("^[0-9]+$", gb_ram2.get ())
    pantalla_valida= re.match("^[a-zA-Z0-9]+$", Pantalla2.get())
    procesador_valido= re.match("^[a-zA-Z0-9]+$", Procesador2.get ())

    if modelo_valido and gb_ram_valida and pantalla_valida and procesador_valido:
        messagebox.showinfo("Información validada", "La información ha sido validada correctamente.")

        data = {
            "modelo": modelo2.get(),
            "cuantas_GB_Ram": gb_ram2.get(),
            "Tipo_pantalla": Pantalla2.get(),
            "Nombre_Procesador": Procesador2.get()

        }

        response = requests.post("http://127.0.0.1:8000/v1/celular",data)
        print(response.status_code)
        print(response.content)


    else:
        pass


ventana = tk.Tk()
ventana.geometry("500x300")
ventana.title("Celular")
ventana.configure(bg='black')
ventana.resizable(False, False)

ventana2 = tk.LabelFrame(ventana, padx=20, pady=20, bg='black')
ventana2.pack(expand=True, fill='both')

style_label = dict(fg='white', bg='black', font=("Arial Bold", 14))
style_entry = dict(fg='white', bg='black', font=("Arial Bold", 14))

modelo = tk.Label(ventana2, text="Modelo", **style_label)
modelo.grid(row=1, column=1, padx=10, pady=10, sticky="w")
modelo2 = tk.Entry(ventana2, **style_entry)
modelo2.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

gb_ram = tk.Label(ventana2, text="Cuantas Gb ram", **style_label)
gb_ram.grid(row=2, column=1, padx=10, pady=10, sticky="w")
gb_ram2 = tk.Entry(ventana2, **style_entry)
gb_ram2.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

Pantalla = tk.Label(ventana2, text="Tipo Pantalla", **style_label)
Pantalla.grid(row=3, column=1, padx=10, pady=10, sticky="w")
Pantalla2 = tk.Entry(ventana2, **style_entry)
Pantalla2.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

Procesador = tk.Label(ventana2, text="Nombre_Procesador", **style_label)
Procesador.grid(row=4, column=1, padx=10, pady=10, sticky="w")
Procesador2 = tk.Entry(ventana2, **style_entry)
Procesador2.grid(row=4, column=2, padx=10, pady=10, sticky="ew")

boton_validar = tk.Button(ventana, text="Validar Información", bg="red", fg="white", font=("Arial Bold", 14), command=validar_informacion)
boton_validar.pack(pady=20)


ventana.mainloop()
