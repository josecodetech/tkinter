import tkinter as tk
from tkinter import ttk


def pulsar():
    print(entradaTextos01.get())
    boton01.config(text=entradaTextos01.get())  # usamos el componente
    entradaTextos01.delete(0, tk.END)  # borra desde indice 0 hasta final
    entradaTextos02.focus()


def cambiar():
    # variable en vez de por el componente
    boton02.config(text=textoCaja.get())
    # asignando a la variable
    textoCaja01.set('Cambiando texto por el de variable')
    entradaTextos02.insert(0, textoCaja)  # asignando al componente


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 700
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Creando boton')
# icono
ventana.iconbitmap('icono.ico')
# variables
textoCaja = tk.StringVar(value='valor por defecto')
textoCaja01 = tk.StringVar()
# entrada de textos
entradaTextos01 = ttk.Entry(
    ventana,  textvariable=textoCaja01, width=40, justify=tk.LEFT)  # CENTER RIGHT LEFT
entradaTextos01.grid(row=2, column=4, padx=20, pady=20, ipadx=10, ipady=10)
entradaTextos01.insert(0, 'Cadena de textos por defecto')
entradaTextos01.insert(tk.END, '////')
entradaTextos01.insert(7, "....")
# entradaTextos01.config(state='readonly')
# otras propiedades entry
entradaTextos02 = ttk.Entry(ventana, width=40, justify=tk.RIGHT, show='*')
entradaTextos02.grid(row=3, column=4, padx=20, pady=20, ipadx=10, ipady=10)
# entradaTextos02.config(state=tk.DISABLED)
entradaTextos03 = ttk.Entry(
    ventana, width=40, textvariable=textoCaja, justify=tk.LEFT)
entradaTextos03.grid(row=4, column=4, padx=20, pady=20, ipadx=10, ipady=10)
# creando boton
boton01 = ttk.Button(ventana, text='Pulsame', command=pulsar)
boton01.grid(row=5, column=2, padx=20, pady=20, ipadx=10, ipady=10)
boton02 = ttk.Button(ventana, text='Cambiar', command=cambiar)
boton02.grid(row=5, column=4, padx=20, pady=20, ipadx=10, ipady=10)
# poner siempre al final
ventana.mainloop()
