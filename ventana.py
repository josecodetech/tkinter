import tkinter as tk
from tkinter import ttk, messagebox
# clase que hereda de la clase tk


class Ventana(tk.Tk):
    def __init__(self, titulo, ancho, alto):
        super().__init__()
        tamaño = ancho+'x'+alto
        self.geometry(tamaño)
        self.title(titulo)
        self._crea_boton()

    def _crea_boton(self):
        self.btn_click = ttk.Button(self, text='click', command=self.click)
        self.btn_click.grid(row=3, column=3, padx=20,
                            pady=20, ipadx=10, ipady=10)

    def click(self):
        print('Has pulsado el boton')


if __name__ == '__main__':
    titulo = 'Mi ventana de clase'
    ancho = str(450)
    alto = str(200)
    ventana = Ventana(titulo, ancho, alto)
    ventana.mainloop()
