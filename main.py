import tkinter as tk
from tkinter import ttk, messagebox
from functions import *

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("400x300")

        # Centrar la ventana
        self.center_window()

        if hay_admin():
            self.open_login_window()
        else:
            self.create_register_window()


    def center_window(self):
        window_width = 400
        window_height = 420
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.master.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    def create_register_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Registrar Cuenta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.master, text="Tipo de cuenta:", font=("Arial", 12)).pack(pady=10)
        self.account_type = ttk.Combobox(self.master, values=["Usuario", "Administrador"], font=("Arial", 12), state="readonly")
        self.account_type.pack(pady=10)

        tk.Label(self.master, text="Usuario:", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Registrar", command=self.register_user, font=("Arial", 12)).pack(pady=10)

        tk.Button(self.master, text="< Volver", command=self.open_login_window, font=("Arial", 10)).pack(side="left", anchor="sw", padx=10, pady=10)

    def register_user(self):
        account = self.account_type.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password or not account:
            messagebox.showerror("Error", "Debe ingresar un tipo de usuario, nombre de usuario y contraseña")
        elif not existe_usuario(username):
            messagebox.showerror("Error", "Usuario ya registrado.")
            

        else:
             ## funcion para enviar el usuario y contrasenia a la base de datos
            registrar_usuario(username, password, account)  
            messagebox.showinfo("Registro", f"Administrador {username} registrado correctamente")
            self.open_login_window()

    def open_login_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Seleccione tipo de cuenta:", font=("Arial", 14)).pack(pady=20)
        self.account_type = ttk.Combobox(self.master, values=["Usuario", "Administrador"], font=("Arial", 12), state="readonly")
        self.account_type.pack(pady=10)

        tk.Label(self.master, text="Usuario:", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Aceptar", command=self.login, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.master, text="Registrar cuenta", command=self.create_register_window, font=("Arial", 10)).pack(pady=5)
        tk.Button(self.master, text="Recuperar cuenta", command=self.open_recover_window, font=("Arial", 10)).pack(pady=5)

    def open_recover_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Recuperar Cuenta", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.master, text="ID de recuperación:", font=("Arial", 12)).pack(pady=5)
        self.recover_id_entry = tk.Entry(self.master, font=("Arial", 12))
        validate_id = self.master.register(self.validate_numeric_input)
        self.recover_id_entry.config(validate="key", validatecommand=(validate_id, "%P"))
        self.recover_id_entry.pack(pady=10)

        tk.Button(self.master, text="Aceptar", command=self.recover_account, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.master, text="< Volver", command=self.open_login_window, font=("Arial", 10)).pack(side="left", anchor="sw", padx=10, pady=10)

    def validate_numeric_input(self, input_value):
        return input_value.isdigit() or input_value == ""

    def recover_account(self):
        recover_id = self.recover_id_entry.get()
        if not recover_id:
            messagebox.showerror("Error", "Debe ingresar el ID de recuperación")
        else:
            self.open_reset_password_window()

    def open_reset_password_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Reestablecer Contraseña", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.master, text="Contraseña nueva:", font=("Arial", 12)).pack(pady=5)
        self.new_password_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.new_password_entry.pack(pady=5)

        tk.Label(self.master, text="Repetir contraseña:", font=("Arial", 12)).pack(pady=5)
        self.repeat_password_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.repeat_password_entry.pack(pady=5)

        tk.Button(self.master, text="Aceptar", command=self.confirm_password, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.master, text="<< Volver", command=self.open_login_window, font=("Arial", 10)).pack(side="left", anchor="sw", padx=10, pady=10)

    def confirm_password(self):
        new_password = self.new_password_entry.get()
        repeat_password = self.repeat_password_entry.get()

        if not new_password or not repeat_password:
            messagebox.showerror("Error", "Las contraseñas no pueden estar vacías")
        elif new_password != repeat_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
        else:
            messagebox.showinfo("Recuperación", "Contraseña reestablecida correctamente")
            self.open_login_window()

    def login(self):
        account = self.account_type.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Debe ingresar un nombre de usuario y una contraseña")
        elif not account:
            messagebox.showerror("Error", "Debe seleccionar un tipo de cuenta")
        elif existe_usuario(username):
            messagebox.showerror("Error", "Usuario no encontrado.")
            
        elif verificar_contrasenia(password, username, account):
            messagebox.showerror("Error", "Contraseña incorrecta o tipo de usuario mal seleccionado.")

        else:
            messagebox.showinfo("Acceso", f"Accediendo como {account} con usuario {username}")
            self.master.destroy()  # Cerrar la ventana principal
            
# Crear la ventana principal
root = tk.Tk()
app = Login(root)
root.mainloop()