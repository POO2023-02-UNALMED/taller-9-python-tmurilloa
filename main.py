from tkinter import Tk, Button, Entry

numero_actual = ""
operador_actual = ""

def agregar_texto(texto):
    global numero_actual
    global operador_actual

    if texto in ['+', '-', '*', '/']:
        
        operador_actual = texto
        numero_actual = pantalla.get()
        pantalla.delete(0, "end")
        
    elif texto == "=":
        
        numero_actual2 = pantalla.get()
        if operador_actual == '+':
            resultado = str(float(numero_actual) + float(numero_actual2))
        elif operador_actual == "-":
            resultado =  str(float(numero_actual)- float(numero_actual2))
        elif operador_actual == "*":
            resultado = str(float(numero_actual)* float(numero_actual2))
        elif operador_actual == "/":
            resultado = str(float(numero_actual)/ float(numero_actual2))
        else:
            resultado = "Operación no admitida"

        pantalla.delete(0, "end")
        pantalla.insert(0, resultado)
        
    else:
        
        pantalla.insert("end", texto)



# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x300")

# Configuración pantalla de salida 

pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=90, padx=0, pady=0)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command = lambda: agregar_texto("9")).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",command = lambda: agregar_texto("=")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command = lambda: agregar_texto(".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: agregar_texto("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: agregar_texto("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: agregar_texto("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: agregar_texto("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()