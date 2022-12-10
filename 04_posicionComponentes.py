import tkinter as tk
from tkinter import ttk
# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 600
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Posicion componentes')
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=9)
ventana.columnconfigure(0,weight=3)
ventana.columnconfigure(1,weight=7)
boton01 = ttk.Button(ventana, text='Boton 01')
boton01.grid(row=0, column=1, sticky='NE')
boton02 = ttk.Button(ventana, text='Boton 02')
boton02.grid(row=0, column=0, sticky='N')
boton03 = ttk.Button(ventana, text='Boton 03')
boton03.grid(row=1, column=1, sticky='N')
boton04 = ttk.Button(ventana, text='Boton 04')
boton04.grid(row=1, column=0, sticky='S')
# poner siempre al final
ventana.mainloop()
