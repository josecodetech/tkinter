import tkinter as tk
from tkinter import filedialog, messagebox, font
def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Abrir archivo",filetypes=[("Texto","*.txt")])
    if archivo:
        try:
            with open(archivo,"r") as f:
                contenido = f.read()
                area_texto.delete(1.0,tk.END)
                area_texto.insert(tk.END,contenido)
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo abrir el archivo: {e}")
def guardar_archivo():
    archivo = filedialog.asksaveasfilename(title="Guardar archivo",defaultextension=".txt",filetypes=[("Texto","*.txt")])
    if archivo:
        try:
            contenido = area_texto.get(1.0,tk.END)
            with open(archivo,"w") as f:
                f.write(contenido)
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo guardar el archivo: {e}")
def nuevo_documento():
    area_texto.delete(1.0,tk.END)
def cambiar_negrita():
    texto = font.Font(font=area_texto["font"])
    if texto.actual()['weight']=='normal':
        area_texto.configure(font=(texto.actual()['family'],texto.actual()['size'],'bold'))
    else:
        area_texto.configure(font=(texto.actual()['family'],texto.actual()['size'],'normal'))
def cambiar_tamaño_fuente(tamaño):
    texto = font.Font(font=area_texto["font"])
    area_texto.configure(font=(texto.actual()['family'],tamaño))
# crear ventana principal
ventana = tk.Tk()
ventana.title("Bloc de notas")
# tamaño
ancho_pantalla = ventana.winfo_screenmmwidth()
alto_pantalla = ventana.winfo_screenmmheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
# area de texto
area_texto = tk.Text(ventana)
area_texto.pack(expand=True,fill=tk.BOTH)
# barra menu
menu_barra = tk.Menu(ventana)
ventana.config(menu=menu_barra)
# opciones de menu principal
archivo_menu = tk.Menu(menu_barra,tearoff=0)
archivo_menu.add_command(label="Nuevo",command=nuevo_documento)
archivo_menu.add_command(label="Abrir",command=abrir_archivo)
archivo_menu.add_command(label="Guardar",command=guardar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)
menu_barra.add_cascade(label="Archivo",menu=archivo_menu)
# opciones de menu formato
formato_menu = tk.Menu(menu_barra,tearoff=0)
formato_menu .add_command(label="Negrita",command=cambiar_negrita)
tamaño_menu = tk.Menu(formato_menu,tearoff=0)
formato_menu .add_cascade(label="Tamaño",menu=tamaño_menu)
for tamaño in range(8,24,2):
    tamaño_menu.add_command(label=f"{tamaño}", command=lambda t=tamaño:cambiar_tamaño_fuente(t))
menu_barra.add_cascade(label="Formato",menu=formato_menu)
# bucle ventana
ventana.mainloop()