import tkinter as tk
from tkinter import ttk, Menu
import sys  # para salir de la aplicacion


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
# menu


def salir():
    print('Has salido de la aplicacion, hasta pronto')
    ventana.quit()  # sale de ventana
    ventana.destroy()  # destruye el objeto creado
    sys.exit()  # sale del proceso


def menu():
    menu_Principal = Menu(ventana)
    menu_Archivo = Menu(menu_Principal, tearoff=0)
    menu_Archivo.add_command(label='Nuevo')
    menu_Archivo.add_separator()
    menu_Archivo.add_command(label='Salir', command=salir)
    menu_Ayuda = Menu(menu_Principal, tearoff=0)
    menu_Ayuda.add_command(label='Acerca de')
    menu_Principal.add_cascade(menu=menu_Archivo, label='Archivo')
    menu_Principal.add_cascade(menu=menu_Ayuda, label='Ayuda')
    ventana.config(menu=menu_Principal)


menu()
# poner siempre al final
ventana.mainloop()
