import tkinter as tk
from tkinter import ttk, scrolledtext


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 500
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Varios, scroll / combo')
# icono
ventana.iconbitmap('icono.ico')
# scrolled text
texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
scroll = scrolledtext.ScrolledText(ventana, width=60, height=15, wrap=tk.WORD)
scroll.insert(tk.INSERT, texto)
scroll.grid(row=1, column=1)
# combo box
datos = [x*3 for x in range(20)]
combobox = ttk.Combobox(ventana, width=15, value=datos)
combobox.grid(row=5, column=1, padx=15, pady=15)
combobox.current(3)
print(f'Mostrando el valor del combo al iniciar ventana {combobox.get()}')
# imagen en el boton
imagen = tk.PhotoImage(file='logo.png')
boton = ttk.Button(ventana, image=imagen)
boton.grid(row=6, column=1)
# poner siempre al final
ventana.mainloop()
