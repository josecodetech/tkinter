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
ventana.title('Acceso')
# icono
ventana.iconbitmap('icono.ico')
# variables
usuario = tk.StringVar()
clave = tk.StringVar()
usuario_guardado = "jose"
clave_guardada = "123"


def mensaje(titulo, mensaje, pasar):
    if pasar == 1:
        messagebox.showinfo(titulo, mensaje)
    else:
        messagebox.showerror(titulo, mensaje)


def entrar():
    usuario_min = usuario.get()
    clave_min = clave.get()
    usuario_min = usuario_min.lower()
    clave_min = clave_min.lower()
    if (usuario_min == usuario_guardado) & (clave_min == clave_guardada):
        mensaje('Acceso permitido', 'Puedes pasar', 1)
    else:
        mensaje('Acceso denegado', 'Intentalo de nuevo', 0)
        borrar()


def borrar():
    usuario.set('')
    clave.set('')


lbl_usuario = ttk.Label(ventana, text='Usuario')
lbl_usuario.grid(row=2, column=2, padx=20, pady=20)
txt_usuario = ttk.Entry(ventana, textvariable=usuario,
                        width=20, justify=tk.RIGHT)
txt_usuario.grid(row=2, column=3, padx=20, pady=20)
lbl_clave = ttk.Label(ventana, text='Clave')
lbl_clave.grid(row=3, column=2, padx=20, pady=20)
txt_clave = ttk.Entry(ventana, textvariable=clave,
                      width=20, justify=tk.RIGHT, show='*')
txt_clave.grid(row=3, column=3, padx=20, pady=20)
btn_entrar = ttk.Button(ventana, text='Entrar', command=entrar)
btn_entrar.grid(row=4, column=2, padx=20, pady=20, ipadx=10, ipady=10)
btn_borrar = ttk.Button(ventana, text='Borrar', command=borrar)
btn_borrar.grid(row=4, column=3, padx=20, pady=20, ipadx=10, ipady=10)
# poner siempre al final
ventana.mainloop()
