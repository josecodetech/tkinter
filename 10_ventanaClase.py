from ventana import *


class Ventana_plus(Ventana):
    def __init__(self, titulo, ancho, alto, texto):
        super().__init__(titulo, ancho, alto)
        self._boton_nuevo(texto)

    def _boton_nuevo(self, texto):
        btn_nuevo = ttk.Button(text=texto)
        btn_nuevo.grid(row=3, column=5, padx=20, pady=20)


titulo = 'Ventana desde otro script'
ancho = str(400)
alto = str(200)
ventana = Ventana_plus(titulo, ancho, alto, 'titulo boton')
#btn_nuevo = ttk.Button(text='Nuevo')
#btn_nuevo.grid(row=3, column=5, padx=20, pady=20)
ventana.mainloop()
