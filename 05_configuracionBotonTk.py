import tkinter as tk

# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 600
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Posicion componentes')
#ventana.rowconfigure(0, weight=2)
#ventana.rowconfigure(1, weight=4)
boton01 = tk.Button(ventana, text='Boton 01')
boton01.config(text='Boton modificado', fg='blue', bg='red', relief=tk.GROOVE)
boton01.grid(row=0, column=0, sticky='N', padx=50, pady=80, columnspan=2)
boton02 = tk.Button(ventana, text='Boton 02')
boton02.config(text='Otro cambiado', fg='white', bg='black')
boton02.grid(row=0, column=1, sticky='N', ipadx=20, ipady=30, columnspan=2)
boton03 = tk.Button(ventana, text='Boton 03')
boton03.config(relief=tk.GROOVE)
boton03.grid(row=1, column=0, sticky='N', columnspan=2)
boton04 = tk.Button(ventana, text='Boton 04')
boton04.grid(row=1, column=1, sticky='N', rowspan=2)
# poner siempre al final
ventana.mainloop()
