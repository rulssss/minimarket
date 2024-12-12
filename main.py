import tkinter as tk
from tkinter import ttk, messagebox

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("400x300")  # Tamaño adecuado de la ventana

        # Centrar la ventana
        self.center_window()

        # Verificar si ya existe un administrador, solo se abre la ventana de login si existe
        if self.hay_admin():
            self.open_login_window()
        else:
            self.create_register_window()

    def hay_admin(self):
        """Función que simula verificar si ya existe un administrador"""
        # Retorna True para simular que existe un administrador
        return True  # Cambiar a False para probar la ventana de registro

    def center_window(self):
        """Centrar la ventana en la pantalla"""
        window_width = 400
        window_height = 400

        # Obtener la resolución de la pantalla
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Establecer la nueva posición de la ventana
        self.master.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    def create_register_window(self):
        """Crea la ventana para registrar un nuevo administrador"""
        # Limpiar la ventana actual de login
        for widget in self.master.winfo_children():
            widget.destroy()

        # Campos para ingresar el nombre de usuario y contraseña
        tk.Label(self.master, text="Registrar Administrador", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.master, text="Usuario:", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Arial", 12))
        self.username_entry.pack(pady=5)
        
        tk.Label(self.master, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)
        
        tk.Button(self.master, text="Registrar", command=self.register_user, font=("Arial", 12)).pack(pady=10)

    def register_user(self):
        """Simula el proceso de registro de un nuevo administrador"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Debe ingresar un nombre de usuario y una contraseña")
        else:
            # Aquí agregarías la lógica para guardar el nuevo administrador en la base de datos o archivo
            messagebox.showinfo("Registro", f"Administrador {username} registrado correctamente")
            
            ### FUNCION PARA ENVIAR CONTRASENIA Y USUARIO

            # Limpiar los widgets de la ventana de registro
            for widget in self.master.winfo_children():
                widget.destroy()

            # Abrir la ventana de login en la misma ventana
            self.open_login_window()

    def open_login_window(self):
        """Abre la ventana de login dentro de la misma ventana principal"""
        tk.Label(self.master, text="Seleccione tipo de cuenta:", font=("Arial", 14)).pack(pady=20)

        # ComboBox para seleccionar entre "Usuario" o "Administrador"
        self.account_type = ttk.Combobox(self.master, values=["Usuario", "Administrador"], font=("Arial", 12))
        self.account_type.pack(pady=10)
        
        tk.Label(self.master, text="Usuario:", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Arial", 12))
        self.username_entry.pack(pady=5)
        
        tk.Label(self.master, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)
        
        tk.Button(self.master, text="Aceptar", command=self.login, font=("Arial", 12)).pack(pady=10)

        # Botón "Registrar cuenta" más pequeño
        tk.Button(self.master, text="Registrar cuenta", command=self.create_register_window, font=("Arial", 10)).pack(pady=5)

        # Botón "Recuperar cuenta"
        tk.Button(self.master, text="Recuperar cuenta", command=self.open_recover_window, font=("Arial", 10)).pack(pady=5)
    
    
    def login(self):
        """Simula el proceso de login con validación"""
        account = self.account_type.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validar que los campos no estén vacíos}
        if not username or not password:
            messagebox.showerror("Error", "Debe ingresar un nombre de usuario y una contraseña")
            return

        # Validar que se haya seleccionado un tipo de cuenta en el ComboBox
        if not account:
            messagebox.showerror("Error", "Debe seleccionar un tipo de cuenta (Usuario o Administrador)")
            return

        # Aquí agregarías la validación con la base de datos o archivo de cuentas
        messagebox.showinfo("Acceso", f"Accediendo como {account} con usuario {username}")

        # Cerrar la ventana de login después de la acción
        self.master.destroy()  # Cierra la ventana principal (login)

        
    def open_recover_window(self):
        """Abre la ventana para recuperar la cuenta"""
        # Limpiar la ventana actual
        for widget in self.master.winfo_children():
            widget.destroy()
    
        # Etiqueta que informa al usuario sobre el ID de recuperación
        tk.Label(self.master, text="Al ingresar se le brindó un ID para poder\n recuperar su contraseña.\n \nIngréselo aquí:", font=("Arial", 12)).pack(pady=20)
    
        # Campo para ingresar solo números (ID de recuperación)
        self.recover_id_entry = tk.Entry(self.master, font=("Arial", 12))
    
        # Validar que solo se ingrese un número
        validate_id = self.master.register(self.validate_numeric_input)
        
        self.recover_id_entry.config(validate="key", validatecommand=(validate_id, "%P"))
        self.recover_id_entry.pack(pady=10)
    
        # Botón para aceptar
        tk.Button(self.master, text="Aceptar", command=self.recover_account, font=("Arial", 12)).pack(pady=10)
    
    def validate_numeric_input(self, input_value):
        """Valida que el valor ingresado sea un número"""
        if input_value.isdigit() or input_value == "":
            return True
        return False
    
    def recover_account(self):
        """Simula la recuperación de la cuenta"""
        recover_id = self.recover_id_entry.get()
        
        if not recover_id:
            messagebox.showerror("Error", "Debe ingresar el ID de recuperación")
            return
    
        ### Aquí agregarías la lógica para verificar el ID de recuperación en la base de datos ###
    
        # Cerrar la ventana de login después de la acción
        self.master.destroy()  # Cierra la ventana principal (login)
    
    


# Crear la ventana principal
root = tk.Tk()
app = Login(root)
root.mainloop()