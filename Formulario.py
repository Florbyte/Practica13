import tkinter as tk
from tkinter import messagebox
import re

class FormularioRegistro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Registro de Usuario")
        self.root.geometry("450x550")

        # Variables
        self.nombre = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm = tk.StringVar()
        self.edad = tk.StringVar()
        self.genero = tk.StringVar(value="")
        self.acepto = tk.BooleanVar()

        # Frame principal
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        campos = [
            ("Nombre completo:", self.nombre),
            ("Email:", self.email),
        ]
        for i, (label, var) in enumerate(campos):
            tk.Label(frame, text=label).grid(row=i, column=0, sticky="e", pady=5)
            entry = tk.Entry(frame, textvariable=var, width=35)
            entry.grid(row=i, column=1, pady=5)
            if i == 0:
                entry.focus()  # Pone el cursor en el primer campo al abrir

        # Password (show="*")
        tk.Label(frame, text="Contraseña:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Entry(frame, textvariable=self.password, show="*", width=35).grid(row=2, column=1)
        
        tk.Label(frame, text="Confirmar:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Entry(frame, textvariable=self.confirm, show="*", width=35).grid(row=3, column=1)

        # Edad
        tk.Label(frame, text="Edad:").grid(row=4, column=0, sticky="e", pady=5)
        tk.Entry(frame, textvariable=self.edad, width=10).grid(row=4, column=1, sticky="w")

        # Género
        tk.Label(frame, text="Género:").grid(row=5, column=0, sticky="e", pady=5)
        gf = tk.Frame(frame)
        gf.grid(row=5, column=1, sticky="w")
        for txt in ["Masculino", "Femenino", "Otro"]:
            tk.Radiobutton(gf, text=txt, variable=self.genero, value=txt).pack(side="left")

        # Checkbox + Botones
        chk_acepto = tk.Checkbutton(frame, text="Acepto los términos", variable=self.acepto)
        chk_acepto.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Accesibilidad: Enter en el último campo (o en la ventana) ejecuta submit
        chk_acepto.bind("<Return>", lambda event: self.validar())
        self.root.bind("<Return>", lambda event: self.validar())

        bf = tk.Frame(frame)
        bf.grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(bf, text="Registrar", command=self.validar, width=15).pack(side="left", padx=5)
        tk.Button(bf, text="Limpiar", command=self.limpiar, width=15).pack(side="left", padx=5)

    def validar(self):
        errores = []
        
        # 1 y 2. Nombre y Email
        if not self.nombre.get().strip():
            errores.append("• El nombre completo es obligatorio.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email.get().strip()):
            errores.append("• El formato del email es inválido (debe contener @ y .).")
            
        # 3 y 4. Contraseñas
        if len(self.password.get()) < 8:
            errores.append("• La contraseña debe tener al menos 8 caracteres.")
        if self.password.get() != self.confirm.get():
            errores.append("• Las contraseñas no coinciden.")
            
        # 5. Edad (número entre 15 y 99)
        edad_str = self.edad.get().strip()
        if not edad_str.isdigit() or not (15 <= int(edad_str) <= 99):
            errores.append("• La edad debe ser un número entre 15 y 99.")

        # 6. Checkbox Acepto
        if not self.acepto.get():
            errores.append("• Debes aceptar los términos y condiciones.")

        # Resultado
        if errores:
            messagebox.showerror("Errores de validación", "\n".join(errores))
        else:
            messagebox.showinfo("Éxito", f"¡Bienvenido {self.nombre.get().strip()}!")

    def limpiar(self):
        self.nombre.set("")
        self.email.set("")
        self.password.set("")
        self.confirm.set("")
        self.edad.set("")
        self.genero.set("")
        self.acepto.set(False)

if __name__ == "__main__":
    FormularioRegistro().root.mainloop()