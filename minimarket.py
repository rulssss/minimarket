import tkinter as tk
from tkinter import ttk, messagebox
from functions import *
from tkinter import Toplevel, Label, Entry, Button, Frame
import re


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


    global ventana_anadir_abierta
    ventana_anadir_abierta = False # controla que la ventana pueda abrirse solo una vez
    def agregar_producto(self):

        global ventana_anadir_abierta    # Usar la variable global

        if ventana_anadir_abierta:
            return

        ventana_anadir_abierta = True # abre la ventana


        # Crear una ventana secundaria
        ventana = Toplevel()
        ventana.title("Añadir Producto")
        ventana.geometry("1200x300")  # Ajusta el tamaño según necesites
        ventana.resizable(False, False)  # Evita que se redimensione
        ventana.configure(bg="white")

         # Hacer la ventana modal
        ventana.grab_set()

        # Centrar la ventana en la pantalla
        ventana.update_idletasks()
        ancho_ventana = 1200
        alto_ventana = 300
        x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un frame contenedor central en la ventana secundaria
        frame = Frame(ventana, bg="white")
        frame.pack(fill="both", expand=False)

        # Título central
        Label(frame, text="Ingrese los datos del producto:", bg="white", font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=5, pady=(10, 30)
        )

        # Etiquetas e Inputs
        Label(frame, text="Nombre del producto", bg="white", font=("Segoe UI", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
        input_nombre = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        input_nombre.grid(row=2, column=0, padx=(30,10), pady=5)

        # Función de validación
        def solo_numeros(char):
            return char.isdigit()  # Verifica si el carácter ingresado es un número
        
        # Registro de la validación
        validacion = root.register(solo_numeros)          
        


        Label(frame, text="Precio de Venta", bg="white", font=("Segoe UI", 12, "bold")).grid(row=1, column=1, padx=10, pady=5)
        input_precio = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(validacion, "%S"))
        input_precio.grid(row=2, column=1, padx=10, pady=5)

        Label(frame, text="Cantidad", bg="white", font=("Segoe UI", 12, "bold")).grid(row=1, column=2, padx=10, pady=5)
        input_cantidad = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(validacion, "%S"))
        input_cantidad.grid(row=2, column=2, padx=10, pady=5)
        
        # Combobox para categorias

        ##########

        # Obtener las categorías
        categorias = traer_categorias()

        # Crear el Combobox
        Label(frame, text="Categoria", bg="white", font=("Segoe UI", 12, "bold")).grid(row=1, column=3, padx=10, pady=5)
        combobox_busqueda1 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda1['values'] = categorias
        combobox_busqueda1.grid(row=2, column=3, padx=10, pady=5)

        # Configurar el tamaño de la fuente de las opciones del Combobox
        combobox_busqueda1.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        ########

        # Combobox para proveedores

        ########

        # Obtener las categorías
        proveedores = traer_proveedores()

        # Crear el Combobox
        Label(frame, text="Proveedores", bg="white", font=("Segoe UI", 12, "bold")).grid(row=1, column=4, padx=10, pady=5)
        combobox_busqueda2 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda2['values'] = proveedores
        combobox_busqueda2.grid(row=2, column=4, padx=10, pady=5)

        # Configurar el tamaño de la fuente de las opciones del Combobox
        combobox_busqueda2.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))



        ######

        # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        def es_numero_decimal(valor):
            try:
                float(valor)  # Intenta convertir a número flotante
                return True
            except ValueError:
                return False

        def on_yes():

            nombre_producto = input_nombre.get()
            precio_producto = input_precio.get()
            cantidad_producto = input_cantidad.get()
            categoria_producto = combobox_busqueda1.get()
            proveedor_producto = combobox_busqueda2.get()

            # Verifica si los valores de precio y cantidad son válidos (números enteros o decimales)
            if not (es_numero_decimal(precio_producto) and es_numero_decimal(cantidad_producto) and bool(re.match("^[A-Za-z0-9 ]*$", nombre_producto))):
                advertencia_label.config(text="No acepta vacios ni ',.-/()'")
                return

            
            categoria_producto = traer_id_categoria(categoria_producto)
            proveedor_producto = traer_id_proveedor(proveedor_producto)

            cargar_producto_actualizacion(nombre_producto, precio_producto, cantidad_producto, categoria_producto, proveedor_producto)
            on_no()



        def on_no():

            global ventana_anadir_abierta
            ventana.destroy()
            ventana_anadir_abierta = False

        # Botones
        btn_aceptar = Button(frame, command=on_yes, text="Aceptar", bg="#e0e0e0", activebackground="#c0c0c0", activeforeground="white", fg="black", font=("Segoe UI", 15, "bold"),height=1, relief="groove", bd=2, width=12)
        btn_aceptar.grid(row=3, column=2, padx=10, pady=(30, 10))

        btn_cancelar = Button(frame, text="Cancelar", command=on_no, bg="#e74c3c", fg="white", activebackground="#c0c0c0", activeforeground="white", font=("Segoe UI", 12, "bold"), relief="groove", bd=2, width=9)
        btn_cancelar.grid(row=4, column=2, padx=10, pady=(10,20))

        # Configurar peso de filas y columnas para centrar
        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        ventana.protocol("WM_DELETE_WINDOW", on_no)
        
        

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
        screen_width = self.master.winfo_screenwidth() #minimo = 1152 
        screen_height = self.master.winfo_screenheight() # minimo = 864 
        self.master.geometry(f"{screen_width}x{screen_height}")

            # Mostrar mensaje de bienvenida como un título en la parte superior
        self.bienvenida = tk.Label(self.master, text="Bienvenido!", font=("Segoe UI", 50))
        self.bienvenida.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Mostrar ID del usuario de forma transparente
        self.mostrar_id_inicio(username)
        

        ######### Crear el Notebook vertical a la izquierda #########
        self.notebook = ttk.Notebook(self.master, style="CustomNotebook.TNotebook")
        self.notebook.place(x=0, y=0, width=310, height=screen_height)


        # Mostrar pestañas según el tipo de cuenta
        if account_type:  # Si es True, mostrar todas las pestañas

            # Crear pestañas del Notebook
            self.tab_datos = tk.Frame(self.notebook, bg="#d7d7d7")
            self.tab_buscar_datos = tk.Frame(self.notebook, bg="#d7d7d7")
            self.tab_administracion = tk.Frame(self.notebook, bg="#d7d7d7")

            self.notebook.add(self.tab_datos, text="Datos")
            self.notebook.add(self.tab_buscar_datos, text="Buscar Datos")
            self.notebook.add(self.tab_administracion, text="Administración")
            
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


                 # Vincular el cambio de pestaña a un evento
            self.notebook.bind("<<NotebookTabChanged>>", self.cambiar_pestana_administrador)


        else:  # Si es False, mostrar solo Buscar Datos y Administración

            # Crear pestañas del Notebook
            self.tab_buscar_datos = tk.Frame(self.notebook, bg="#d7d7d7")
            self.tab_administracion = tk.Frame(self.notebook, bg="#d7d7d7")

            self.notebook.add(self.tab_buscar_datos, text="Buscar Datos")
            self.notebook.add(self.tab_administracion, text="Administración")

                ######### Crear el área blanca dinámica justo debajo del Notebook ########
            self.contenido_bd = tk.Frame(self.tab_buscar_datos, bg="white", bd=0, highlightthickness=0)
            self.contenido_bd.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.contenido_ad = tk.Frame(self.tab_administracion, bg="white", bd=0, highlightthickness=0)
            self.contenido_ad.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.buscar_datos = BuscarDatos(self.contenido_bd)
            self.administracion = Administracion(self.contenido_ad)

            # Vincular el cambio de pestaña a un evento
            self.notebook.bind("<<NotebookTabChanged>>", self.cambiar_pestana_usuario)

            
        # Configurar estilo para eliminar bordes del Notebook
        # Configurar estilo para aumentar tamaño de fuente y cambiar colores de las pestañas
        style = ttk.Style()
        style.configure("CustomNotebook.TNotebook", borderwidth=0, background="white")
        style.configure("CustomNotebook.TNotebook.Tab", font=("Segoe UI", 11), padding=[10, 5])
        style.map("CustomNotebook.TNotebook.Tab", background=[("selected", "#d1e0e0")], foreground=[("selected", "#000000")])


        # Mostrar contenido inicial según el tipo de cuenta
        if account_type:  # Si es True, mostrar la pestaña de Datos
            self.mostrar_datos()
        else:  # Si es False, mostrar la pestaña de Buscar Datos por defecto
            self.mostrar_buscar_datos()


    def mostrar_id_inicio(self, username):
            
            # Simular la obtención del ID del usuario
            id_usuario = obtener_id_usuario(username)  # Método que debes implementar
    
            # Etiqueta transparente para mostrar el ID
            self.id_label = tk.Label(
                self.master,
                text=f"ID usuario: {id_usuario}",
                font=("Segoe UI", 30, "bold"),
                bg="black",
                fg="white",
                relief="flat", bd=3, padx=15
            )
            self.id_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

            
    
            # Configurar opacidad simulada y desaparecer después de 3 segundos
            self.id_label.after(5000, self.id_label.destroy)


    def cambiar_pestana_usuario(self, event):
                pestaña_actual = self.notebook.index(self.notebook.select())
                if pestaña_actual == 0:  # Pestaña de Buscar Datos
                    self.mostrar_buscar_datos()
                elif pestaña_actual == 1:  # Pestaña de Administración
                    self.mostrar_administracion()

    def cambiar_pestana_administrador(self, event):
                pestaña_actual = self.notebook.index(self.notebook.select())
                if pestaña_actual == 0 and hasattr(self, 'datos'):
                    self.mostrar_datos()
                elif pestaña_actual == 0 or pestaña_actual == 1:  # Asegurar que Buscar Datos funciona
                    self.mostrar_buscar_datos()
                elif pestaña_actual == 1 or pestaña_actual == 2:  # Asegurar que Administración funciona
                    self.mostrar_administracion()

    def mostrar_datos(self):
        self.datos.mostrar()

    def mostrar_buscar_datos(self):
        self.buscar_datos.mostrar()

    def mostrar_administracion(self):
        self.administracion.mostrar()


# Crear la ventana principal
root = tk.Tk()
app = Minimarket(root, "mariano", True)
root.mainloop()