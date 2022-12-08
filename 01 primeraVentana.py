import tkinter as tk
# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 600
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Titulo de la ventana')
# poner siempre al final
ventana.mainloop()
