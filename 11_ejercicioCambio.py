import tkinter as tk
from tkinter import ttk, messagebox


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 400
alto = 300
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Cambio de moneda')
# icono
ventana.iconbitmap('icono.ico')
# variables
euro = tk.StringVar()
dolar = tk.StringVar()
cambio = 1.06


def cambiar():

    if (euro.get() != '') & (euro.get().isdigit()) & (dolar.get() == ''):
        euro_importe = float(euro.get())
        resultado = round(euro_importe * cambio, 2)
        dolar.set(str(resultado))
    elif (dolar.get() != '') & (dolar.get().isdigit()) & (euro.get() == ''):
        dolar_importe = float(dolar.get())
        resultado = round(dolar_importe / cambio, 2)
        euro.set(str(resultado))
    else:
        if (euro.get() == '') & (dolar.get() == ''):
            mensaje('Error', 'introduce un dato y se cambiara el otro', 0)
            borrar()
        else:
            mensaje('Info', 'Introduce un dato numerico en euro o dolar', 1)
            borrar()


def borrar():
    euro.set('')
    dolar.set('')


def mensaje(titulo, mensaje, tipo):
    if tipo == 1:
        messagebox.showinfo(titulo, mensaje)
    else:
        messagebox.showerror(titulo, mensaje)


lbl_euro = ttk.Label(ventana, text='Euro')
lbl_euro.grid(row=2, column=2, padx=20, pady=20)
txt_euro = ttk.Entry(ventana, textvariable=euro, width=15, justify=tk.RIGHT)
txt_euro.grid(row=2, column=3, padx=20, pady=20)
lbl_dolar = ttk.Label(ventana, text='Dolar')
lbl_dolar.grid(row=3, column=2, padx=20, pady=20)
txt_dolar = ttk.Entry(ventana, textvariable=dolar, width=15, justify=tk.RIGHT)
txt_dolar.grid(row=3, column=3, padx=20, pady=20)
btn_cambiar = ttk.Button(ventana, text='Cambiar', command=cambiar)
btn_cambiar.grid(row=4, column=2, padx=20, pady=20, ipadx=10, ipady=10)
btn_borrar = ttk.Button(ventana, text='Borrar', command=borrar)
btn_borrar.grid(row=4, column=4, padx=20, pady=20, ipadx=10, ipady=10)
# poner siempre al final
ventana.mainloop()
