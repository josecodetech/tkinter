import tkinter as tk
from tkinter import ttk
# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 400
alto = 300
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Creando boton')
# icono
ventana.iconbitmap('icono.ico')


def click():
    print("Boton pulsado")
    boton01.config(text='Has pulsado el boton 02')


# creando primer boton
boton01 = ttk.Button(ventana, text='Pulsame')
boton01.pack()
boton02 = ttk.Button(ventana, text='click', command=click)
boton02.pack()
# poner siempre al final
ventana.mainloop()
