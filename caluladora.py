import re
import tkinter as tk
from tkinter import messagebox


class Calculadora:

  def __init__(self):
    # Paso 1: Crear la ventana principal
    self.ventana = tk.Tk()
    self.ventana.title("Calculadora")
    self.ventana.resizable(False, False)

    # Paso 2: Crear la pantalla (Entry)
    self.display = tk.Entry(
        self.ventana, font=("Arial", 24), borderwidth=5, justify="right"
    )
    self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

    # Paso 3: Agregar los botones
    botones = [
      
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("C", "0", "=", "+"),
       
    ]

    for i, fila in enumerate(botones):
      for j, texto in enumerate(fila):
        btn = tk.Button(
            self.ventana,
            text=texto,
            font=("Arial", 14),
            width=4,
            height=2,
            command=lambda t=texto: self.click(t),
        )
        btn.grid(row=i + 1, column=j, padx=2, pady=2)

  # Paso 4: Implementar la lógica de eventos con validación
  def click(self, valor):
    if valor == "C":
      self.display.delete(0, tk.END)
    elif valor == "=":
      expresion = self.display.get().strip()
      try:
        # 1. Validar que no esté vacío y solo tenga números/operadores permitidos
        if not expresion or not re.fullmatch(r"[0-9+\-*/.]+", expresion):
          raise ValueError("Caracteres inválidos")

        # 2. Bloquear operadores consecutivos como ++, --, +*, //, etc.
        if re.search(r"[+\-*/]{2,}", expresion):
          raise ValueError("Operadores consecutivos")

        # 3. Bloquear operadores mal ubicados al inicio o al final
        if expresion[0] in "*/" or expresion[-1] in "+-*/.":
          raise ValueError("Operador mal ubicado")

        resultado = eval(expresion)
        self.display.delete(0, tk.END)
        self.display.insert(0, str(resultado))
      except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero")
        self.display.delete(0, tk.END)
      except Exception:
        messagebox.showerror("Error", "Expresión inválida")
        self.display.delete(0, tk.END)
    else:
      self.display.insert(tk.END, valor)

  def run(self):
    self.ventana.mainloop()


if __name__ == "__main__":
  Calculadora().run()