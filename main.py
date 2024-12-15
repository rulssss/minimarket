import tkinter as tk
from tkinter import ttk, messagebox
from functions import *

## VENTANA DE LOGINS 


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

        tk.Label(self.master, text="Registrar Cuenta", font=("Segoe UI", 14)).pack(pady=20)
        tk.Label(self.master, text="Tipo de cuenta:", font=("Segoe UI", 12)).pack(pady=10)
        self.account_type = ttk.Combobox(self.master, values=["Usuario", "Administrador"], font=("Segoe UI", 12), state="readonly")
        self.account_type.set("Administrador")  # Establecer "Administrador" como valor predeterminado
        self.account_type.pack(pady=10)

        tk.Label(self.master, text="Usuario:", font=("Segoe UI", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Segoe UI", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Contraseña:", font=("Segoe UI", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*", font=("Segoe UI", 12))
        self.password_entry.pack(pady=5)


         # Crear el botón "Aceptar"
        register_button = tk.Button(self.master, text="Registrar", command=self.login, font=("Segoe UI", 12))
        register_button.pack(pady=10)
        # Vincular la tecla Enter al comando del botón "Aceptar"
        self.master.bind("<Return>", lambda event: register_button.invoke())


        tk.Button(self.master, text="< Volver", command=self.open_login_window, font=("Segoe UI", 10)).pack(side="left", anchor="sw", padx=10, pady=10)

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

        tk.Label(self.master, text="Seleccione tipo de cuenta:", font=("Segoe UI", 14)).pack(pady=20)
        self.account_type = ttk.Combobox(self.master, values=["Usuario", "Administrador"], font=("Arial", 12), state="readonly")
        self.account_type.set("Administrador")  # Establecer "Administrador" como valor predeterminado
        self.account_type.pack(pady=10)

        tk.Label(self.master, text="Usuario:", font=("Segoe UI", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Segoe UI", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Contraseña:", font=("Segoe UI", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*", font=("Segoe UI", 12))
        self.password_entry.pack(pady=5)

         # Crear el botón "Aceptar"
        aceptar_button = tk.Button(self.master, text="Aceptar", command=self.login, font=("Segoe UI", 12))
        aceptar_button.pack(pady=10)
        # Vincular la tecla Enter al comando del botón "Aceptar"
        self.master.bind("<Return>", lambda event: aceptar_button.invoke())

        tk.Button(self.master, text="Registrar cuenta", command=self.create_register_window, font=("Segoe UI", 10)).pack(pady=5)
        tk.Button(self.master, text="Recuperar cuenta", command=self.open_recover_window, font=("Segoe UI", 10)).pack(pady=5)

    def open_recover_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Recuperar Cuenta", font=("Segoe UI", 14)).pack(pady=20)
        tk.Label(self.master, text="ID de recuperación:", font=("Segoe UI", 12)).pack(pady=5)
        self.recover_id_entry = tk.Entry(self.master, font=("Segoe UI", 12))
        validate_id = self.master.register(self.validate_numeric_input)
        self.recover_id_entry.config(validate="key", validatecommand=(validate_id, "%P"))
        self.recover_id_entry.pack(pady=10)

        tk.Button(self.master, text="Aceptar", command=self.recover_account, font=("Segoe UI", 12)).pack(pady=10)
        tk.Button(self.master, text="< Volver", command=self.open_login_window, font=("Segoe UI", 10)).pack(side="left", anchor="sw", padx=10, pady=10)

    def validate_numeric_input(self, input_value):
        return input_value.isdigit() or input_value == ""

    def recover_account(self):
        global recover_id
        recover_id = self.recover_id_entry.get()
        
        if not recover_id:
            messagebox.showerror("Error", "Debe ingresar el ID de recuperación")
        elif existencia_de_id(recover_id):
            messagebox.showerror("Error", "ID Incorrecto")
        else:
            self.open_reset_password_window()

    def open_reset_password_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        

        tk.Label(self.master, text="Reestablecer Contraseña", font=("Segoe UI", 14)).pack(pady=20)
        tk.Label(self.master, text="Contraseña nueva:", font=("Segoe UI", 12)).pack(pady=5)
        self.new_password_entry = tk.Entry(self.master, show="*", font=("Segoe UI", 12))
        self.new_password_entry.pack(pady=5)

        tk.Label(self.master, text="Repetir contraseña:", font=("Segoe UI", 12)).pack(pady=5)
        self.repeat_password_entry = tk.Entry(self.master, show="*", font=("Segoe UI", 12))
        self.repeat_password_entry.pack(pady=5)

        tk.Button(self.master, text="Aceptar", command=self.confirm_password, font=("Segoe UI", 12)).pack(pady=10)
        tk.Button(self.master, text="<< Volver", command=self.open_login_window, font=("Segoe UI", 10)).pack(side="left", anchor="sw", padx=10, pady=10)

    def confirm_password(self):
        new_password = self.new_password_entry.get()
        repeat_password = self.repeat_password_entry.get()

        if not new_password or not repeat_password:
            messagebox.showerror("Error", "Las contraseñas no pueden estar vacías")
        elif new_password != repeat_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
        else:
            actualizar_contrasena(new_password, recover_id)
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
            self.master.destroy()
            minimarket_root = tk.Tk()
            Minimarket(minimarket_root, username, account)
            minimarket_root.mainloop()


### TODA LA VENTANA DE EL MINIMARKET 


class Datos:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        # Limpiar el contenedor principal
        for widget in self.master.winfo_children():
            widget.destroy()

        # Etiqueta inicial
        tk.Label(self.master, text="Contenido de Datos", bg="white", font=("Segoe UI", 10, "bold")).pack(pady=10)

        # Crear botones
        botones = [
            ("Agregar Producto", self.agregar_producto),
            ("Borrar Producto", self.borrar_producto),
            ("Visualizar Productos", self.visualizar_productos),
            ("Agregar Proveedor", self.agregar_proveedor),
            ("Borrar Proveedor", self.borrar_proveedor),
            ("Visualizar Proveedores", self.visualizar_proveedores),
            ("Agregar Categoría", self.agregar_categoria),
            ("Borrar Categoría", self.borrar_categoria),
            ("Visualizar Categorías", self.visualizar_categorias),
            ("Actualizar Precio", self.actualizar_precio)
        ]

        c = 0
        for texto, comando in botones:
            c += 1
    
            tk.Button(self.master,text=texto,command=comando,height=1,  width=20,  bg="#e0e0e0",  fg="black", font=("Segoe UI", 12, "bold"),  activebackground="#c0c0c0",  activeforeground="white", relief="groove",  bd=2  ).pack(pady=9)
            if c == 3:
                c = 0
                # Agregar una línea sutil estilo "hr"
                tk.Frame(self.master, bg="gray", height=2, width=300).pack(pady=10, fill="x")        

        # Agregar una línea sutil estilo "hr"
        tk.Frame(self.master, bg="gray", height=2, width=300).pack(pady=10, fill="x")
        # Botón "Borrar Datos" en la parte inferior
        boton_borrar_datos = tk.Button(self.master, text="Borrar Datos", height=1, command=self.borrar_datos,  bg="red", fg="white", width=15, font=("Segoe UI", 12, "bold"), bd=2)
        boton_borrar_datos.pack(pady=30)

    # Métodos de ejemplo para los botones
    def agregar_producto(self):
        print("Agregar Producto")

    def borrar_producto(self):
        print("Borrar Producto")

    def visualizar_productos(self):
        pass

    def agregar_proveedor(self):
        print("Agregar Proveedor")

    def borrar_proveedor(self):
        print("Borrar Proveedor")

    def visualizar_proveedores(self):
        pass

    def agregar_categoria(self):
        print("Agregar Categoría")

    def borrar_categoria(self):
        print("Borrar Categoría")
    
    def visualizar_categorias(self):
        pass

    def actualizar_precio(self):
        print("actualizar precio")

    def borrar_datos(self):
        print("Borrar Datos")

    

       

class BuscarDatos:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text="Contenido de Buscar Datos", bg="white",font=("Segoe UI", 10, "bold") ).pack(pady=10)


        # Botones "Datos por Día" y "Datos por Mes"
        botones = [
            ("Datos por Día", self.datos_por_dia),
            ("Datos por Mes", self.datos_por_mes)
        ]

        for texto, comando in botones:
            tk.Button(self.master,text=texto,command=comando,height=1,  width=20,  bg="#e0e0e0",  fg="black", font=("Segoe UI", 12, "bold"),  activebackground="#c0c0c0",  activeforeground="white", relief="groove",  bd=2  ).pack(pady=9)

    # Métodos de ejemplo para los botones
    def datos_por_dia(self):
        print("Datos por Día")

    def datos_por_mes(self):
        print("Datos por Mes")




class Administracion:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text="Contenido de Administración", bg="white", font=("Segoe UI", 10, "bold")).pack(pady=10)
        # Botones "Facturero" y "Compras"
        botones = [
            ("Facturero", self.facturero),
            ("Compras", self.compras)
        ]

        for texto, comando in botones:
            tk.Button(self.master,text=texto,command=comando,height=1,  width=20,  bg="#e0e0e0",  fg="black", font=("Segoe UI", 12, "bold"),  activebackground="#c0c0c0",  activeforeground="white", relief="groove",  bd=2  ).pack(pady=9)

    # Métodos de ejemplo para los botones
    def facturero(self):
        print("Facturero")

    def compras(self):
        print("Compras")

## ventana para el minimarket 

class Minimarket:
    def __init__(self, master, username, account_type):
        self.master = master
        self.master.title("rls")

        # Configurar la ventana para que tome el tamaño de la pantalla sin ser pantalla completa
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.master.geometry(f"{screen_width}x{screen_height}")

        ######### Crear el Notebook vertical a la izquierda #########
        self.notebook = ttk.Notebook(self.master, style="CustomNotebook.TNotebook")
        self.notebook.place(x=0, y=0, width=310, height=screen_height)

        # Crear pestañas del Notebook
        self.tab_datos = tk.Frame(self.notebook, bg="#d7d7d7")
        self.tab_buscar_datos = tk.Frame(self.notebook, bg="#d7d7d7")
        self.tab_administracion = tk.Frame(self.notebook, bg="#d7d7d7")

        self.notebook.add(self.tab_datos, text="Datos")
        self.notebook.add(self.tab_buscar_datos, text="Buscar Datos")
        self.notebook.add(self.tab_administracion, text="Administración")

        # Vincular el cambio de pestaña a un evento
        self.notebook.bind("<<NotebookTabChanged>>", self.cambiar_pestana)

        ######### Crear el área blanca dinámica justo debajo del Notebook #########
        self.contenido = tk.Frame(self.tab_datos, bg="white", bd=0, highlightthickness=0)
        self.contenido.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.contenido_bd = tk.Frame(self.tab_buscar_datos, bg="white", bd=0, highlightthickness=0)
        self.contenido_bd.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.contenido_ad = tk.Frame(self.tab_administracion, bg="white", bd=0, highlightthickness=0)
        self.contenido_ad.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear instancias de las clases de contenido
        self.datos = Datos(self.contenido)
        self.buscar_datos = BuscarDatos(self.contenido_bd)
        self.administracion = Administracion(self.contenido_ad)

        # Configurar estilo para eliminar bordes del Notebook
        # Configurar estilo para aumentar tamaño de fuente y cambiar colores de las pestañas
        style = ttk.Style()
        style.configure("CustomNotebook.TNotebook", borderwidth=0, background="white")
        style.configure("CustomNotebook.TNotebook.Tab", font=("Arial", 11), padding=[10, 5])
        style.map("CustomNotebook.TNotebook.Tab", background=[("selected", "#d1e0e0")], foreground=[("selected", "#000000")])

        # Mostrar contenido inicial
        self.mostrar_datos()

    def cambiar_pestana(self, event):
        pestaña_actual = self.notebook.index(self.notebook.select())
        if pestaña_actual == 0:
            self.mostrar_datos()
        elif pestaña_actual == 1:
            self.mostrar_buscar_datos()
        elif pestaña_actual == 2:
            self.mostrar_administracion()

    def mostrar_datos(self):
        self.datos.mostrar()

    def mostrar_buscar_datos(self):
        self.buscar_datos.mostrar()

    def mostrar_administracion(self):
        self.administracion.mostrar()


            
# Crear la ventana principal
root = tk.Tk()
app = Login(root)
root.mainloop()