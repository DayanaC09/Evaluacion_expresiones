import tkinter as tk
from tkinter import messagebox


def evaluar_expresion(expresion):
    pila = []
    tokens = expresion.split()

    try:
        for token in tokens:
            if token.isdigit(): 
                pila.append(int(token))
            elif token in "+-*/":
                b = pila.pop()
                a = pila.pop()
                if token == "+":
                    pila.append(a + b)
                elif token == "-":
                    pila.append(a - b)
                elif token == "*":
                    pila.append(a * b)
                elif token == "/":
                    pila.append(a / b)
            else:
                raise ValueError("Token inválido")
            
        if len(pila) == 1:
            return pila.pop()
        else:
            raise ValueError("Expresión mal formada")
    except (IndexError, ValueError) as e:
        raise ValueError("Error al evaluar la expresión: " + str(e))

def manejar_evaluacion():
    expresion = entrada.get()
    try:
        resultado = evaluar_expresion(expresion)
        messagebox.showinfo("Resultado", f"El resultado de la expresión es: {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Evaluador de Notación Postfija")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Introduce una expresión en notación postfija:")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Evaluar", command=manejar_evaluacion)
boton.pack(pady=10)

ventana.mainloop()
