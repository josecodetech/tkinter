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
ventana.title('Tabs')
# icono
ventana.iconbitmap('icono.ico')
control_tab = ttk.Notebook(ventana)
# Primer tab
tab01 = ttk.Frame(control_tab)
control_tab.add(tab01, text='Tab 01')
control_tab.pack(fill='both')  # rellena todo el espacio
txt_nombre = ttk.Entry(tab01, width=40)
txt_nombre.grid(row=0, column=0, padx=10, pady=10)
# Segundo tab
tab02 = ttk.LabelFrame(control_tab, text='Tab con etiqueta')
control_tab.add(tab02, text='Tab 02')
txt_nombre = ttk.Entry(tab02, width=40)
txt_nombre.grid(row=3, column=2, padx=10, pady=10)
btn_pulsar = ttk.Button(tab02, text='Pulsar')
btn_pulsar.grid(row=0, column=0, padx=10, pady=10)
# poner siempre al final
ventana.mainloop()
