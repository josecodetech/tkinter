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
# creando primer boton
boton = ttk.Button(ventana, text='Pulsame')
boton.pack()
# poner siempre al final
ventana.mainloop()
