import tkinter as tk
from tkinter import ttk, Frame, PhotoImage


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 500
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Imagen en Frame')
# icono
ventana.iconbitmap('icono.ico')
# creamos marco
frame = Frame(ventana)
# posicionamos
frame.pack(padx=10, pady=10)
frame.config(bg='lightblue')
frame.config(width=400, height=300)
frame.config(cursor="pirate")  # arrow
frame.config(relief="sunken")  # ridge
frame.config(bd=25)
# imagen
imagen = PhotoImage(file='logo.png')
lbl_imagen = ttk.Label(frame, image=imagen).pack()
# poner siempre al final
ventana.mainloop()
