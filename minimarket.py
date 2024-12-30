import tkinter as tk
from tkinter import ttk, messagebox
from functions import *
from tkinter import Toplevel, Label, Entry, Button, Frame, font
import re


### TODA LA VENTANA DE EL MINIMARKET 


class Datos:
    def __init__(self, master, minimarket):
        self.master = master
        self.minimarket = minimarket

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
            ("Actualizar Precio", self.actualizar_precio),
            ("Visualizar Productos", self.visualizar_productos),
            ("Agregar Proveedor", self.agregar_proveedor),
            ("Borrar Proveedor", self.borrar_proveedor),
            ("Visualizar Proveedores", self.visualizar_proveedores),
            ("Agregar Categoría", self.agregar_categoria),
            ("Borrar Categoría", self.borrar_categoria),
            ("Visualizar Categorías", self.visualizar_categorias),
            
        ]

        c = 0
        bandera = False
        for texto, comando in botones:
            c += 1  
            
    
            tk.Button(self.master,text=texto,command=comando,height=1,  width=20,  bg="#e0e0e0",  fg="black", font=("Segoe UI", 12, "bold"),  activebackground="#c0c0c0",  activeforeground="white", relief="groove",  bd=2  ).pack(pady=9)
            if c == 4:
                c = 0
                bandera = True
                # Agregar una línea sutil estilo "hr"
                tk.Frame(self.master, bg="gray", height=2, width=300).pack(pady=10, fill="x") 
              
            if bandera == True and c == 3:
                c = 0
                # Agregar una línea sutil estilo "hr"
                tk.Frame(self.master, bg="gray", height=2, width=300).pack(pady=10, fill="x") 
       
        # Botón "Borrar Datos" en la parte inferior
        boton_borrar_datos = tk.Button(self.master, text="Borrar Datos", height=1, command=self.borrar_datos,  bg="red", fg="white", width=15, font=("Segoe UI", 12, "bold"), bd=2)
        boton_borrar_datos.pack(pady=30)

    # Métodos de ejemplo para los botones


    def agregar_producto(self):
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
        screen_width = ventana.winfo_screenwidth()

        # Ajustar el ancho de la ventana según el ancho de la pantalla
        if screen_width < 1100:
            ancho_ventana = 1000
        else:
            ancho_ventana = 1100

        alto_ventana = 320
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
        Label(frame, text="Nombre del producto", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=5)
        input_nombre = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        input_nombre.grid(row=2, column=0, padx=(30,10), pady=5)


        # Función de validación
        def solo_numeros(char):
            return char.isdigit()  # Verifica si el carácter ingresado es un número

        # Registro de la validación
        validacion = self.master.register(solo_numeros)

        Label(frame, text="Precio de Venta", bg="white", font=("Segoe UI", 12)).grid(row=1, column=1, padx=10, pady=5)
        input_precio = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(validacion,    "%S"))
        input_precio.grid(row=2, column=1, padx=10, pady=5)

        Label(frame, text="Cantidad", bg="white", font=("Segoe UI", 12)).grid(row=1, column=2, padx=10, pady=5)
        input_cantidad = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(validacion,  "%S"))
        input_cantidad.grid(row=2, column=2, padx=10, pady=5)

        # Combobox para categorias
        categorias_tuplas = traer_categorias()
        categorias = [categoria[0] for categoria in categorias_tuplas]
        Label(frame, text="Categoria", bg="white", font=("Segoe UI", 12)).grid(row=1, column=3, padx=10, pady=5)
        combobox_busqueda1 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda1['values'] = categorias
        combobox_busqueda1.grid(row=2, column=3, padx=10, pady=5)
        combobox_busqueda1.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        # Combobox para proveedores
        proveedores_tuplas = traer_proveedores()
        proveedores = [proveedor[0] for proveedor in proveedores_tuplas]
        Label(frame, text="Proveedores", bg="white", font=("Segoe UI", 12)).grid(row=1, column=4, padx=10, pady=5)
        combobox_busqueda2 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda2['values'] = proveedores
        combobox_busqueda2.grid(row=2, column=4, padx=10, pady=5)
        combobox_busqueda2.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        # Crear un frame para los botones
        button_frame = tk.Frame(ventana, bg="white")
        button_frame.pack(pady=(0, 30))

        def on_yes():
            nombre_producto = input_nombre.get()
            precio_producto = input_precio.get()
            cantidad_producto = input_cantidad.get()
            categoria_producto = combobox_busqueda1.get()
            proveedor_producto = combobox_busqueda2.get()

            # Verifica si los valores de precio y cantidad son válidos (números enteros o decimales)
            if not nombre_producto or not precio_producto or cantidad_producto and not bool(re.match("^[A-Za-z0-9 ]*$", nombre_producto)):
                advertencia_label.config(text="No acepta vacios ni ',.-/()'")
                return

            cargar_producto_actualizacion(nombre_producto, precio_producto, cantidad_producto, categoria_producto, proveedor_producto)
            on_no()

        def on_no():
            ventana.destroy()

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12,    "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12,     "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

        # Configurar peso de filas y columnas para centrar
        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        ventana.protocol("WM_DELETE_WINDOW", on_no)
        
    def borrar_producto(self):
        # Crear la ventana
        ventana = tk.Toplevel()
        ventana.title("Borrar Producto")
        ventana.geometry("300x150")  # Tamaño de la ventana
        ventana.resizable(False, False)  # Evita que se redimensione

        # Hacer la ventana modal
        ventana.grab_set()

        # Configurar el color de fondo de la ventana a blanco
        ventana.configure(bg="white")
        

        # Obtener el tamaño de la pantalla
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana

        if screen_width < 1100:

            window_width = 400
            window_height = 270
        else:
            window_width = 500
            window_height = 290

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        # Ubicar la ventana en el centro de la pantalla
        ventana.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Label para el nombre del producto
        label_nombre = tk.Label(ventana, text="Nombre de el Producto:", bg="white", font=("Segoe UI", 16))
        label_nombre.pack(pady=10)

        # Entry para el nombre del producto con fondo #d7d7d7
        entry_nombre = tk.Entry(ventana, bg="#d7d7d7", font=("Segoe UI", 16), width=25)
        entry_nombre.pack(pady=5)

            # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack()
        
        # Función para confirmar y devolver el valor ingresado
        def confirmar():
            nombre_prod = entry_nombre.get()

            if not nombre_prod:  # Verificar si está vacío
                advertencia_label.config(text="¡Error! No admite nombre vacío.")
                return  # No hacer nada más si está vacío

            if bool(re.match("^[A-Za-z0-9 ]*$", nombre_prod)):  # Verificar si contiene letras y números
                v = buscar_producto(nombre_prod) # creada, y sida true lo borra al instante, si hace falta en otra instancia crear otra funcion solo para borrar
                if v:
                    
                    messagebox.showinfo("Borrar Producto", "Producto borrado con éxito.")
                    ventana.destroy()  # Cerrar la ventana
                else:
                    messagebox.showinfo("Borrar Producto", "No se encontró el producto.")

            else:
                advertencia_label.config(text="Solo admite letras y números.")

        # Botón de borrar
        boton_confirmar = tk.Button(ventana, text="Borrar", command=confirmar, bg="#ef3232", relief="groove", font=("Segoe UI", 16, "bold"), fg="black", width=12)
        boton_confirmar.pack(pady=10)

        def cerrar():
            ventana.destroy()  # Cerrar la ventana

        # Botón para cerrar la ventana
        boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar, bg="lightgrey", font=("Segoe UI", 14, "bold"), fg="black", relief="groove")
        boton_cerrar.pack(pady=5)

        ventana.protocol("WM_DELETE_WINDOW", cerrar)

        # Iniciar el bucle principal de la ventana
        ventana.mainloop()

    def actualizar_precio(self):
        
        def filtrar_productos():
            value = combobox_nombre.get().lower()
            if value == '':
                combobox_nombre['values'] = producto_list
            else:
                data = []
                for item in producto_list:
                    if value in item.lower():
                        data.append(item)
                combobox_nombre['values'] = data
            combobox_nombre.event_generate('<Down>')

        def on_key_release(event):
            global filtro_timer
            if filtro_timer:
                confirm_window.after_cancel(filtro_timer)  # Cancelar temporizador anterior
            filtro_timer = confirm_window.after(1200, filtrar_productos)  # Esperar 1500 milisegundos

        confirm_window = Toplevel()
        confirm_window.title("Actualizar Precio")
        confirm_window.geometry("1200x300")  # Ajusta el tamaño según necesites
        confirm_window.resizable(False, False)  # Evita que se redimensione
        confirm_window.configure(bg="white")

        # Inicializar filtro_timer
        global filtro_timer
        filtro_timer = None

        # Hacer la ventana modal
        confirm_window.grab_set()

        # Centrar la ventana en la pantalla
        confirm_window.update_idletasks()
        screen_width = confirm_window.winfo_screenwidth()

        # Ajustar el ancho de la ventana según el ancho de la pantalla
        if screen_width < 1100:
            ancho_ventana = 1000
        else:
            ancho_ventana = 1100

        alto_ventana = 320
        x = (confirm_window.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (confirm_window.winfo_screenheight() // 2) - (alto_ventana // 2)
        confirm_window.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un frame contenedor central en la ventana secundaria
        frame = Frame(confirm_window, bg="white")
        frame.pack(fill="both", expand=False)

        # Título central
        Label(frame, text="Actualizar el precio del producto:", bg="white", font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=5, pady=(10, 30)
        )

        # Etiquetas e Inputs
        Label(frame, text="Nombre del producto", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=5)
        combobox_nombre = ttk.Combobox(frame, font=("Segoe UI", 16), state="normal", height=5)
        combobox_nombre.grid(row=2, column=0, padx=(30,10), pady=5)

        productos = traer_todos_los_productos()  # Obtener los productos
        producto_list = [producto[0] for producto in productos]  # Lista con los nombres de los productos
        combobox_nombre['values'] = producto_list
        combobox_nombre.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))

        # Vincular la función de autocompletar al evento de escritura
        combobox_nombre.bind('<KeyRelease>', on_key_release)

        # Campo de precio editable
        Label(frame, text="Precio actual a editar", bg="white", font=("Segoe UI", 12)).grid(row=1, column=1, padx=10, pady=5)
        entry_precio = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        entry_precio.grid(row=2, column=1, padx=10, pady=5)

        # Campo de cantidad no editable
        Label(frame, text="Stock", bg="white", font=("Segoe UI", 12)).grid(row=1, column=2, padx=10, pady=5)
        entry_cantidad = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), state='readonly')
        entry_cantidad.grid(row=2, column=2, padx=10, pady=5)

        # Campo de categoria no editable
        Label(frame, text="Categoria", bg="white", font=("Segoe UI", 12)).grid(row=1, column=3, padx=10, pady=5)
        entry_categoria = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), state='readonly')
        entry_categoria.grid(row=2, column=3, padx=10, pady=5)

        # Campo de proveedor no editable
        Label(frame, text="Proveedor", bg="white", font=("Segoe UI", 12)).grid(row=1, column=4, padx=10, pady=5)
        entry_proveedor = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), state='readonly')
        entry_proveedor.grid(row=2, column=4, padx=10, pady=5)

        # Crear el Label de advertencia
        advertencia_label = tk.Label(confirm_window, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        # Crear un frame para los botones
        button_frame = tk.Frame(confirm_window, bg="white")
        button_frame.pack(pady=(0, 30))

        def cargar_datos_producto(event):
            producto_seleccionado = combobox_nombre.get()
            for producto in productos:
                if producto[0] == producto_seleccionado:
                    entry_precio.delete(0, tk.END)
                    entry_precio.insert(0, producto[1])  # Precio actual

                    entry_cantidad.config(state='normal')
                    entry_cantidad.delete(0, tk.END)
                    entry_cantidad.insert(0, producto[2])  # Cantidad
                    entry_cantidad.config(state='readonly')

                    entry_categoria.config(state='normal')
                    entry_categoria.delete(0, tk.END)
                    entry_categoria.insert(0, producto[3])  # Categoria
                    entry_categoria.config(state='readonly')

                    entry_proveedor.config(state='normal')
                    entry_proveedor.delete(0, tk.END)
                    entry_proveedor.insert(0, producto[4])  # Proveedor
                    entry_proveedor.config(state='readonly')

        combobox_nombre.bind("<<ComboboxSelected>>", cargar_datos_producto)

        def on_yes():
            nombre_producto = combobox_nombre.get()
            precio_producto = entry_precio.get()

            producto_seleccionado = combobox_nombre.get()
            for producto in productos:
                if producto[0] == producto_seleccionado:
                    precio_anterior = producto[1]

            def es_numero_decimal(valor):
                try:
                    float(valor)  # Intenta convertir a número flotante
                    return True
                except ValueError:
                    return False

            if es_numero_decimal(precio_producto):
                if (float(precio_anterior) == float(precio_producto)):
                    advertencia_label.config(text="Actualice el precio por favor")
                else:
                    actualizar_producto(nombre_producto, precio_producto)
                    on_no()
                return
            else:
                advertencia_label.config(text="Debe ingresar solo números")
                return

        def on_no():
            confirm_window.destroy()  # Cerrar la ventana

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

        # Configurar peso de filas y columnas para centrar
        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        confirm_window.protocol("WM_DELETE_WINDOW", on_no)
        confirm_window.mainloop()

    def visualizar_productos(self):
       self.minimarket.mostrar_arbol_productos()


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
        screen_width = 1024 #self.master.winfo_screenwidth() #minimo = 1152 
        screen_height = 768#self.master.winfo_screenheight() # minimo = 864 
        self.master.geometry(f"{screen_width}x{screen_height}")
        self.master.minsize(800, 600)  # Tamaño mínimo de la ventana


        # Mostrar ID del usuario de forma transparente y bienvenida
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
            self.datos = Datos(self.contenido, self)
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

        # Vincular el evento de cambio de tamaño de la ventana
        self.master.bind("<Configure>", self.ajustar_tamano)

    def ajustar_tamano(self, event):
        # Ajustar el tamaño del notebook y el frame derecho
        self.notebook.place(x=0, y=0, width=310, height=self.master.winfo_height())
        if hasattr(self, 'frame_derecho'):
            self.frame_derecho.place(x=320, y=0, width=max(self.master.winfo_width() - 320, 480), height=max(self.master.winfo_height(), 600))

    

    def mostrar_arbol_productos(self, bandera=False):
        # Limpiar el área derecha si ya hay contenido
        self.ocultar_arbol_productos()

        # Estilo personalizado para agrandar la fuente de la tabla y aumentar la altura de las filas
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 16, "bold"))  # Agranda la fuente de los encabezados
        style.configure("Treeview", font=("Segoe UI", 14), rowheight=30)   # Agranda la fuente de las filas y ajusta la altura
        style.configure("Rojo.TLabel", foreground="red")

        # Frame derecho para mostrar la tabla
        self.frame_derecho = tk.Frame(self.master, padx=10, pady=10)
        self.frame_derecho.place(x=320, y=0, width=max(self.master.winfo_width() - 320, 480), height=max(self.master.winfo_height(), 600))

        # Título para la tabla
        label_tabla = tk.Label(self.frame_derecho, text="Productos", font=("Segoe UI", 24, "bold"), fg="black", relief="flat")
        label_tabla.pack(pady=20)
            


        # Tabla (Treeview) para mostrar los productos
        tree = ttk.Treeview(self.frame_derecho, columns=("nombre", "cantidad", "precio", "categoria", "proveedor"), show="headings", height=10)

        # Definir las columnas con doble clic
        tree.heading("nombre", text="Nombre", command=lambda: contador_clic("nombre"))
        tree.heading("cantidad", text="Cantidad", command=lambda: contador_clic("cantidad"))
        tree.heading("precio", text="Precio", command=lambda: contador_clic("precio"))
        tree.heading("categoria", text="Categoria", command=lambda: contador_clic("categoria"))
        tree.heading("proveedor", text="Proveedor", command=lambda: contador_clic("proveedor"))

        # Definir el ancho de las columnas
        tree.column("nombre", width=100, anchor="center")
        tree.column("cantidad", width=100, anchor="center")
        tree.column("precio", width=100, anchor="center")
        tree.column("categoria", width=100, anchor="center")
        tree.column("proveedor", width=100, anchor="center")

        # Empaquetar la tabla
        tree.pack(fill=tk.BOTH, expand=True)

        # funciones para copiar columna:

        # Inicializar un diccionario para contar los clics en cada columna
        click_counter = {"nombre": 0, "cantidad": 0, "precio": 0, "categoria": 0, "proveedor": 0}
    

        # Función para contar clics y copiar la columna si hay dos clics consecutivos
        def contador_clic(columna):
            # Incrementar el contador para la columna seleccionada
            click_counter[columna] += 1

            # Si se hace clic dos veces, copiar la columna y resetear el contador
            if click_counter[columna] == 2:
                copiar_columna(columna)
                click_counter[columna] = 0
            else:
                # Resetear los contadores de las demás columnas
                for col in click_counter:
                    if col != columna:
                        click_counter[col] = 0


        # Función para copiar la columna seleccionada al portapapeles
        def copiar_columna(columna):
            # Obtener los índices de las filas y el índice de la columna
            valores_columna = []
            columna_index = tree["columns"].index(columna)

            # Extraer todos los valores de la columna seleccionada
            for item in tree.get_children():
                valor = tree.item(item)['values'][columna_index]
                valores_columna.append(str(valor))

            # Unir los valores con saltos de línea y copiarlos al portapapeles
            self.master.clipboard_clear()  # Limpiar el portapapeles
            self.master.clipboard_append("\n".join(valores_columna))  # Copiar al portapapeles
            self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

            # Mostrar mensaje emergente
            mostrar_mensaje_copiado()

        # Variable para realizar seguimiento de los clics
        global primer_click
        primer_click = None

        # Función para copiar una fila completa al portapapeles
        def copiar_fila(event):
            global primer_click

            # Identificar la fila sobre la que se ha hecho clic
            item = tree.identify_row(event.y)

            # Si no se ha hecho clic sobre ninguna fila (fuera del área de filas)
            if not item:
                return

            # Si ya se ha hecho un primer clic en esta fila
            if primer_click == item:
                # Obtener los valores de la fila
                valores_fila = tree.item(item)['values']

                # Unir los valores con tabuladores o saltos de línea, y copiarlos al portapapeles
                fila_copiada = "\t".join(str(valor) for valor in valores_fila)  # Usa tabuladores para separar los valores
                self.master.clipboard_clear()  # Limpiar el portapapeles
                self.master.clipboard_append(fila_copiada)  # Copiar al portapapeles
                self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

                # Mostrar mensaje emergente
                mostrar_mensaje_copiado()

                # Reiniciar el contador de clics
                primer_click = None
            else:
                # Si es el primer clic en la fila, guardamos esa fila
                primer_click = item

        # Función para mostrar el mensaje "Copiado al portapapeles"
        def mostrar_mensaje_copiado():
            # Crear la ventana del mensaje
            mensaje = tk.Toplevel(self.master)
            mensaje.title("Mensaje Copiado")

            # Obtener las dimensiones de la ventana principal
            ventana_width = self.master.winfo_width()
            ventana_height = self.master.winfo_height()

            # Obtener las dimensiones del mensaje
            mensaje_width = 300
            mensaje_height = 50

            # Calcular la posición para centrar el mensaje
            position_top = self.master.winfo_rooty() + (ventana_height // 2) - (mensaje_height // 2)
            position_left = self.master.winfo_rootx() + (ventana_width // 2) - (mensaje_width // 2)

            # Hacer la ventana pequeña, sin bordes y transparente
            mensaje.geometry(f"{mensaje_width}x{mensaje_height}+{position_left}+{position_top}")
            mensaje.overrideredirect(True)  # Eliminar los bordes de la ventana
            mensaje.config(bg="black")  # Fondo negro semitransparente
            mensaje.attributes("-alpha", 0.7)  # Hacerla semi-transparente

            # Etiqueta con el mensaje
            label = tk.Label(mensaje, text="Copiado al portapapeles", fg="white", font=("Arial", 16, "bold"), bg="black")
            label.pack(expand=True)

            # Cerrar el mensaje después de 2 segundos
            mensaje.after(2000, mensaje.destroy)  # 2000 ms = 2 segundos

        # Asociar el evento de clic en la fila
        tree.bind("<ButtonRelease-1>", copiar_fila)

        

        def mostrar_productos():
            all_data = traer_todos_los_productos()
            return all_data


        def actualizar_filtro(event=None):
            all_data2 = traer_todos_los_productos()
                # Obtener el texto ingresado en el Entry
            texto_busqueda = mostrar_productos.entry_busqueda.get().lower()
            # Limpiar la tabla para mostrar los nuevos resultados
            for item in tree.get_children():
                tree.delete(item)
            # Filtrar productos que contengan el texto ingresado
            if texto_busqueda == "":
                productos_a_mostrar = all_data2  # Mostrar todos los productos si no se ha ingresado texto
            else:
                productos_a_mostrar = [p for p in all_data2 if texto_busqueda in p[0].lower()]
            # Insertar los productos filtrados en la tabla
            if productos_a_mostrar:
                # Aplicar estilo a las filas con el tag "rojo"
                tree.tag_configure("rojo", foreground="red", font=("Segoe UI", 14, "bold"))
                for i in productos_a_mostrar:
                    # Determina el color según el valor de i[2]
                    tag = ("rojo",) if i[2] < 5 else ()
                    # Insertar una fila vacía para crear espacio
                    tree.insert("", "end", values=("", "", "", "", ""))
                    tree.insert("", "end", values=(f"{i[0]}", i[2], f"${i[1]:.2f}", f"{i[3]}", i[4]), tags=tag)
            else:
                tree.insert("", "end", values=("No se encontraron productos", "", "", "", ""))

        def mostrar_todos_los_productos(s = mostrar_productos()): # cambiar por funcion que traiga todos los datos
            # Limpiar la tabla para mostrar los productos
            for item in tree.get_children():
                tree.delete(item)
            # Configurar el tag para texto en rojo
            tree.tag_configure("rojo", foreground="red", font=("Segoe UI", 14, "bold"))
            # Insertar todos los productos en la tabla
            for i in s:
                tree.insert("", "end", values=("", "", "", "", ""))
                # Verificar si el valor en la posición 2 es menor a -5
                # Determina el color según el valor de i[2]
                tag = ("rojo",) if i[2] < 5 else ()
                # Insertar el producto con el tag "rojo"
                tree.insert("", "end", values=(f"{i[0]}", i[2], f"${i[1]:.2f}", f"{i[3]}", i[4]), tags=tag)
            

     
        mostrar_productos.entry_busqueda = ttk.Entry(self.master, font=("Segoe UI", 14))
        mostrar_productos.entry_busqueda.place(x=390, y=50)  # Ajustar la posición
        mostrar_productos.entry_busqueda.bind("<KeyRelease>", actualizar_filtro)  # Detectar cada tecla que el usuario presiona

        
        # Mostrar todos los productos   inmediatamente cuando se abre el Entry    
        mostrar_todos_los_productos()
        
            
         

        

    def ocultar_arbol_productos(self):
        if hasattr(self, 'frame_derecho'):
            self.frame_derecho.destroy()
    


    def mostrar_id_inicio(self, username):
        # Simular la obtención del ID del usuario
        id_usuario = obtener_id_usuario(username)  # Método que debes implementar

         # Mostrar mensaje de bienvenida como un título en la parte superior
        self.bienvenida = tk.Label(self.master, text="Bienvenido!", font=("Segoe UI", 50))
        self.bienvenida.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

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
        self.bienvenida.after(10000, self.bienvenida.destroy)
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