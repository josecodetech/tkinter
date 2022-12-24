import tkinter as tk
from tkinter import ttk, messagebox
from time import sleep

# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 500
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Barra de progreso')
# icono
ventana.iconbitmap('icono.ico')


def comenzar():
    barra.start()
    barra['maximum'] = 10
    for valor in range(11):
        sleep(0.2)
        barra['value'] = valor
        barra.update()
    barra['value'] = 0
    barra.stop()


def parar():
    barra.stop()


barra = ttk.Progressbar(ventana, orient='horizontal', length=450)
barra.grid(row=0, column=1, padx=15, pady=15, columnspan=3)
btn_comenzar = ttk.Button(ventana, text='comenzar', command=comenzar)
btn_comenzar.grid(row=1, column=2)
btn_parar = ttk.Button(ventana, text='parar', command=parar)
btn_parar.grid(row=1, column=3)

# poner siempre al final
ventana.mainloop()
