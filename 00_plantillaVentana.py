import tkinter as tk
from tkinter import ttk, messagebox


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 700
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Titulo')
# icono
ventana.iconbitmap('icono.ico')


# poner siempre al final
ventana.mainloop()
