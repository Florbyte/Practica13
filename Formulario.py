import tkinter as tk
from tkinter import messagebox
import re




class FormularioRegistro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Registro de Usuario")
        self.root.geometry("450x650")
        self.root.resizable(False, False)


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


        tk.Label(
            frame,
            text="Registro de Usuario",
            font=("Arial", 18, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=15)


        # Nombre y Email
        campos = [
            ("Nombre completo:", self.nombre),
            ("Email:", self.email),
        ]


        for i, (label, var) in enumerate(campos, start=1):
            tk.Label(frame, text=label).grid(
                row=i, column=0, sticky="e", pady=7
            )
            entry = tk.Entry(frame, textvariable=var, width=35)
            entry.grid(row=i, column=1, pady=7)


            if i == 1:
                entry.focus()


        # Contraseña
        tk.Label(frame, text="Contraseña:").grid(
            row=3, column=0, sticky="e", pady=7
        )
        tk.Entry(
            frame, textvariable=self.password,
            show="*", width=35
        ).grid(row=3, column=1)


        # Confirmar contraseña
        tk.Label(frame, text="Confirmar:").grid(
            row=4, column=0, sticky="e", pady=7
        )
        tk.Entry(
            frame, textvariable=self.confirm,
            show="*", width=35
        ).grid(row=4, column=1)


        # Edad
        tk.Label(frame, text="Edad:").grid(
            row=5, column=0, sticky="e", pady=7
        )
        tk.Entry(
            frame, textvariable=self.edad, width=10
        ).grid(row=5, column=1, sticky="w")


        # Género
        tk.Label(frame, text="Género:").grid(
            row=6, column=0, sticky="e", pady=7
        )


        gf = tk.Frame(frame)
        gf.grid(row=6, column=1, sticky="w")


        for txt in ["Masculino", "Femenino", "Otro"]:
            tk.Radiobutton(
                gf, text=txt,
                variable=self.genero, value=txt
            ).pack(side="left")


        # Checkbox
        chk_acepto = tk.Checkbutton(
            frame,
            text="Acepto los términos",
            variable=self.acepto
        )
        chk_acepto.grid(
            row=7, column=0, columnspan=2, pady=12
        )


        # Botones Registrar y Limpiar
        bf = tk.Frame(frame)
        bf.grid(row=8, column=0, columnspan=2, pady=10)


        tk.Button(
            bf,
            text="Registrar",
            command=self.validar,
            width=15
        ).pack(side="left", padx=5)


        tk.Button(
            bf,
            text="Limpiar",
            command=self.limpiar,
            width=15
        ).pack(side="left", padx=5)


        # Botón Iniciar sesión con Google
        tk.Button(
            frame,
            text=" 🌐 Iniciar sesión con Google",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#0A0A0A",
            relief="solid",
            cursor="hand2",
            width=30,
            height=2,
            command=self.login_google
        ).grid(row=10, column=0, columnspan=2, pady=5)


        # Enter para registrar
        self.root.bind(
            "<Return>",
            lambda event: self.validar()
        )


    def login_google(self):
        messagebox.showinfo(
            "Google",
            "Has seleccionado iniciar sesión con Google."
        )


    def validar(self):
        errores = []


        # Nombre y Email
        if not self.nombre.get().strip():
            errores.append(
                "• El nombre completo es obligatorio."
            )


        if not re.match(
            r"[^@]+@[^@]+\.[^@]+",
            self.email.get().strip()
        ):
            errores.append(
                "• El formato del email es inválido."
            )


        # Contraseñas
        if len(self.password.get()) < 8:
            errores.append(
                "• La contraseña debe tener al menos 8 caracteres."
            )


        if self.password.get() != self.confirm.get():
            errores.append(
                "• Las contraseñas no coinciden."
            )


        # Edad
        edad_str = self.edad.get().strip()


        if not edad_str.isdigit() or not (
            15 <= int(edad_str) <= 99
        ):
            errores.append(
                "• La edad debe ser un número entre 15 y 99."
            )


        # Términos
        if not self.acepto.get():
            errores.append(
                "• Debes aceptar los términos y condiciones."
            )


        # Resultado
        if errores:
            messagebox.showerror(
                "Errores de validación",
                "\n".join(errores)
            )
        else:
            messagebox.showinfo(
                "Éxito",
                f"¡Bienvenido {self.nombre.get().strip()}!"
            )


    def limpiar(self):
        self.nombre.set("")
        self.email.set("")
        self.password.set("")
        self.confirm.set("")
        self.edad.set("")
        self.genero.set("")
        self.acepto.set(False)

if __name__ == "__main__":
    app = FormularioRegistro()
    app.root.mainloop()