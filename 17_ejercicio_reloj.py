import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class RelojDigital:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Reloj Digital')
        self.ventana.geometry("300x200")
        # etiqueta hora
        self.lbl_hora=tk.Label(ventana, text="", font=("Arial",24))
        self.lbl_hora.pack(pady=20)
        # botones para cronometro
        self.btn_iniciar_cronometro = tk.Button(ventana, text="Iniciar Cronometro", command=self.iniciar_cronometro)
        self.btn_iniciar_cronometro.pack()
        self.btn_detener_cronometro = tk.Button(ventana, text="Detener Cronometro", command=self.detener_cronometro, state="disabled")
        self.btn_detener_cronometro.pack()
        # botones para alarma
        self.btn_configurar_alarma = tk.Button(ventana, text="Configurar Alarma", command=self.configurar_alarma)
        self.btn_configurar_alarma.pack()
        self.btn_activar_alarma = tk.Button(ventana, text="Activar Alarma", command=self.activar_alarma, state="disabled")
        self.btn_activar_alarma.pack()
        # variable estado cronometro
        self.cronometro_activo = False
    def iniciar_reloj(self):
        if self.cronometro_activo==False:
            hora_actual = time.strftime("%H:%M:%S")
            self.lbl_hora.config(text=hora_actual)
            self.lbl_hora.after(1000, self.iniciar_reloj)
    def iniciar_cronometro(self):
        self.tiempo_inicio = time.time()
        self.btn_iniciar_cronometro.config(state="disabled")
        self.btn_detener_cronometro.config(state="normal")
        self.cronometro_activo = True
        self.actualizar_cronometro()
    def detener_cronometro(self):
        self.btn_iniciar_cronometro.config(state="normal")
        self.btn_detener_cronometro.config(state="disabled")
        self.cronometro_activo=False
        self.iniciar_reloj()
    def actualizar_cronometro(self):
        if self.cronometro_activo:
            tiempo_transcurrido = time.time() - self.tiempo_inicio
            tiempo_formato = time.strftime("%H:%M:%S", time.gmtime(tiempo_transcurrido))
            self.lbl_hora.config(text=tiempo_formato)
            self.lbl_hora.after(1000, self.actualizar_cronometro)
    def configurar_alarma(self):
        self.hora_alarma = tk.simpledialog.askstring("Configurar alarma", "Introduce la hora de la alarma (formato: HH:MM)")
        self.btn_activar_alarma.config(state="normal")
    def activar_alarma(self):
        hora_actual = time.strftime("%H:%M")
        if hora_actual == self.hora_alarma:
            messagebox.showinfo("Alarma", "Es la hora que indicastes")
            self.btn_activar_alarma.config(state="disabled")
        else:
            self.ventana.after(60000, self.activar_alarma)
if __name__ == "__main__":
    ventana = tk.Tk()
    reloj_digital = RelojDigital(ventana)
    reloj_digital.iniciar_reloj()
    ventana.mainloop()
    