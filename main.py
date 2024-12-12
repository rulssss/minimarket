import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla de Inicio de Sesión")
        self.root.geometry("400x300")

        # Etiqueta y ComboBox para seleccionar el tipo de cuenta
        self.label_role = tk.Label(self.root, text="Seleccione el tipo de cuenta:")
        self.label_role.pack(pady=10)

        self.combo_role = ttk.Combobox(self.root, values=["Usuario", "Administrador"], width=27)
        self.combo_role.pack(pady=5)
        self.combo_role.current(0)  # Establecer valor por defecto en "Usuario"

        # Etiquetas y campos de entrada para el nombre de usuario y contraseña
        self.label_user = tk.Label(self.root, text="Usuario:")
        self.label_user.pack(pady=10)
        self.entry_user = tk.Entry(self.root, width=30)
        self.entry_user.pack(pady=5)

        self.label_pass = tk.Label(self.root, text="Contraseña:")
        self.label_pass.pack(pady=10)
        self.entry_pass = tk.Entry(self.root, show="*", width=30)
        self.entry_pass.pack(pady=5)

        # Botón de login
        self.btn_login = tk.Button(self.root, text="Aceptar", command=self.login)
        self.btn_login.pack(pady=20)

    def login(self):
        user = self.entry_user.get()  # Obtener el nombre de usuario
        password = self.entry_pass.get()  # Obtener la contraseña
        role = self.combo_role.get()  # Obtener el rol seleccionado

        # Verificación simple de las credenciales (esto puede ser más avanzado con base de datos)
        if user == "admin" and password == "admin123" and role == "Administrador":
            messagebox.showinfo("Login", "Acceso como Administrador concedido")
        elif user == "usuario" and password == "user123" and role == "Usuario":
            messagebox.showinfo("Login", "Acceso como Usuario concedido")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")


# Crear la ventana principal y pasarla a la clase LoginScreen
if __name__ == "__main__":
    root = tk.Tk()
    login_screen = LoginScreen(root)
    root.mainloop()