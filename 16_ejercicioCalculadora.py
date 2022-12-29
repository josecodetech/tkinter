import tkinter as tk
from tkinter import ttk, messagebox


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 420
alto = 250
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Calculadora')
# icono
ventana.iconbitmap('icono.ico')
ventana.resizable(0, 0)
# variables
texto = tk.StringVar()
primerOperador = True
operador01 = 0
operador02 = 0
resultado = 0
opcion_elegida = ''
# funciones


def borrar():
    texto.set('')


def operacion(opcion):
    global primerOperador
    global opcion_elegida
    global operador01
    if (opcion != '') and (texto.get != '') and (primerOperador):
        opcion_elegida = opcion
        operador01 = float(texto.get())
        borrar()
        primerOperador = False


def numero_pulsado(numero):
    numero = texto.get()+numero
    texto.set(numero)


def punto():
    if '.' not in texto.get():
        numero = texto.get()+'.'
        texto.set(numero)


def resultado():
    global operador01, operador02, opcion_elegida, primerOperador, resultado
    if (primerOperador == False) and (texto.get() != ''):
        operador02 = float(texto.get())
        if opcion_elegida == '+':
            resultado = operador01+operador02
        if opcion_elegida == '-':
            resultado = operador01-operador02
        if opcion_elegida == '*':
            resultado = operador01*operador02
        if opcion_elegida == '/':
            try:
                resultado = operador01/operador02
            except:
                messagebox.showerror('Error', 'Error en la division')
        texto.set(str(resultado))
        opcion_elegida = ''
        operador01 = 0
        operador02 = 0
        primerOperador = True

    # creamos frames
frm_sup = tk.Frame(ventana, height=50)
frm_inf = tk.Frame(ventana)
# posicionar
frm_sup.pack(side=tk.TOP, fill='x')
frm_sup.config(height=50)
frm_inf.pack(fill='both')
frm_inf.config(bg='gray')
# botonera
txt_resultado = ttk.Entry(frm_sup, font=(
    'arial', 22, 'bold'), state="readonly", textvariable=texto, justify=tk.RIGHT, width=24)
txt_resultado.grid(row=0, column=0,
                   ipadx=5, ipady=5, padx=10, pady=5)
btn_borrar = ttk.Button(frm_inf, text='Borrar', command=borrar, width=10)
btn_borrar.grid(row=0, column=0, padx=5, pady=5)
btn_dividir = ttk.Button(
    frm_inf, text='/', command=lambda: operacion('/'), width=10)
btn_dividir.grid(row=0, column=1, padx=5, pady=5)
btn_multiplicar = ttk.Button(
    frm_inf, text='*', command=lambda: operacion('*'), width=10)
btn_multiplicar.grid(row=0, column=2, padx=5, pady=5)
btn_restar = ttk.Button(
    frm_inf, text='-', command=lambda: operacion('-'), width=10)
btn_restar.grid(row=0, column=3, padx=5, pady=5)
btn_07 = ttk.Button(
    frm_inf, text='7', command=lambda: numero_pulsado('7'), width=10)
btn_07.grid(row=1, column=0, padx=5, pady=5)
btn_08 = ttk.Button(
    frm_inf, text='8', command=lambda: numero_pulsado('8'), width=10)
btn_08.grid(row=1, column=1, padx=5, pady=5)
btn_09 = ttk.Button(
    frm_inf, text='9', command=lambda: numero_pulsado('9'), width=10)
btn_09.grid(row=1, column=2, padx=5, pady=5)
btn_sumar = ttk.Button(
    frm_inf, text='+', command=lambda: operacion('+'), width=10)
btn_sumar.grid(row=1, column=3, padx=5, pady=5)
btn_04 = ttk.Button(
    frm_inf, text='4', command=lambda: numero_pulsado('4'), width=10)
btn_04.grid(row=2, column=0, padx=5, pady=5)
btn_05 = ttk.Button(
    frm_inf, text='5', command=lambda: numero_pulsado('5'), width=10)
btn_05.grid(row=2, column=1, padx=5, pady=5)
btn_06 = ttk.Button(
    frm_inf, text='6', command=lambda: numero_pulsado('6'), width=10)
btn_06.grid(row=2, column=2, padx=5, pady=5)
btn_igual = ttk.Button(
    frm_inf, text='=', command=resultado, width=10)
btn_igual.grid(row=2, column=3, rowspan=3, padx=5, pady=5)
btn_01 = ttk.Button(
    frm_inf, text='1', command=lambda: numero_pulsado('1'), width=10)
btn_01.grid(row=3, column=0, padx=5, pady=5)
btn_02 = ttk.Button(
    frm_inf, text='2', command=lambda: numero_pulsado('2'), width=10)
btn_02.grid(row=3, column=1, padx=5, pady=5)
btn_03 = ttk.Button(
    frm_inf, text='3', command=lambda: numero_pulsado('3'), width=10)
btn_03.grid(row=3, column=2, padx=5, pady=5)
btn_00 = ttk.Button(
    frm_inf, text='0', command=lambda: numero_pulsado('0'), width=25)
btn_00.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
btn_punto = ttk.Button(
    frm_inf, text='.', command=punto, width=25)
btn_punto.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
# poner siempre al final
ventana.mainloop()
