import tkinter as tk
from tkinter import ttk, messagebox


def click():
    lblMensaje.config(text=cajaNombre.get())  # txtNombre.get()


def mensaje():
    mensaje = "Hola, "+txtNombre.get()+", bienvenid@"
    messagebox.showinfo("Mensaje", mensaje)  # showerror showinfo showwarning


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 700
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Etiqueta / Mensaje')
# icono
ventana.iconbitmap('icono.ico')
# variables
txtNombre = tk.StringVar()
# etiqueta
lblNombre = ttk.Label(ventana, text='Nombre')
lblNombre.grid(row=2, column=1, columnspan=2)
lblMensaje = ttk.Label(ventana, text='Nombre')
lblMensaje.grid(row=5, column=3, columnspan=2)
# entrada de textos
cajaNombre = ttk.Entry(
    ventana,  textvariable=txtNombre, width=20, justify=tk.RIGHT)  # CENTER RIGHT LEFT
cajaNombre.grid(row=2, column=3, padx=20, pady=20, ipadx=5, ipady=5)


# creando boton
btnClick = ttk.Button(ventana, text='Pulsame', command=click)
btnClick.grid(row=3, column=3, padx=20, pady=20, ipadx=10, ipady=10)
btnMensaje = ttk.Button(ventana, text='Mensaje', command=mensaje)
btnMensaje.grid(row=3, column=5, padx=20, pady=20, ipadx=10, ipady=10)
# poner siempre al final
ventana.mainloop()
