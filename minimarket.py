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
        ancho_ventana = 1200
        alto_ventana = 350
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
        validacion = root.register(solo_numeros)          
        


        Label(frame, text="Precio de Venta", bg="white", font=("Segoe UI", 12)).grid(row=1, column=1, padx=10, pady=5)
        input_precio = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(validacion, "%S"))
        input_precio.grid(row=2, column=1, padx=10, pady=5)

        Label(frame, text="Cantidad", bg="white", font=("Segoe UI", 12)).grid(row=1, column=2, padx=10, pady=5)
        input_cantidad = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(validacion, "%S"))
        input_cantidad.grid(row=2, column=2, padx=10, pady=5)
        
        # Combobox para categorias

        ##########

        # Obtener las categorías
        categorias_tuplas = traer_categorias()

        # Convertir la lista de tuplas en una lista de cadenas de texto
        categorias = [categoria[0] for categoria in categorias_tuplas]

        # Crear el Combobox
        Label(frame, text="Categoria", bg="white", font=("Segoe UI", 12)).grid(row=1, column=3, padx=10, pady=5)
        combobox_busqueda1 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda1['values'] = categorias
        combobox_busqueda1.grid(row=2, column=3, padx=10, pady=5)

        # Configurar el tamaño de la fuente de las opciones del Combobox
        combobox_busqueda1.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        ########

        # Combobox para proveedores

        ########

        # Obtener las categorías
        proveedores_tuplas = traer_proveedores()

        # Convertir la lista de tuplas en una lista de cadenas de texto
        proveedores = [proveedor[0] for proveedor in proveedores_tuplas]

        # Crear el Combobox
        Label(frame, text="Proveedores", bg="white", font=("Segoe UI", 12)).grid(row=1, column=4, padx=10, pady=5)
        combobox_busqueda2 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda2['values'] = proveedores
        combobox_busqueda2.grid(row=2, column=4, padx=10, pady=5)

        # Configurar el tamaño de la fuente de las opciones del Combobox
        combobox_busqueda2.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))



        ######

        # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)


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
        btn_aceptar = Button(frame, command=on_yes, text="Aceptar", bg="#e0e0e0", activebackground="#c0c0c0", activeforeground="white", fg="black", font=("Segoe UI", 15, "bold"),height=1, relief="groove", bd=2, width=12)
        btn_aceptar.grid(row=3, column=2, padx=10, pady=(30, 10))

        btn_cancelar = Button(frame, text="Cancelar", command=on_no, bg="#e74c3c", fg="white", activebackground="#c0c0c0", activeforeground="white", font=("Segoe UI", 12, "bold"), relief="groove", bd=2, width=9)
        btn_cancelar.grid(row=4, column=2, padx=10, pady=10)

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

        # Hacer la ventana modal
        ventana.grab_set()

        # Configurar el color de fondo de la ventana a blanco
        ventana.configure(bg="white")
        

        # Obtener el tamaño de la pantalla
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
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


        confirm_window = tk.Toplevel()
        confirm_window.title("Actualizar Precio")
        confirm_window.geometry("600x400")
        confirm_window.config(bg="white")

        # Centrando la ventana  
        screen_width = confirm_window.winfo_screenwidth()
        screen_height = confirm_window.winfo_screenheight()
        window_width = 1300
        window_height = 320
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        confirm_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        global filtro_timer
        # Inicializar filtro_timer
        filtro_timer = None

        # Hacer la ventana modal
        confirm_window.grab_set()

        label = tk.Label(confirm_window, text="Actualizar el precio de el producto:", font=("Segoe UI", 16, "bold"), bg="white")
        label.pack(pady=10)


        entry_frame = tk.Frame(confirm_window, bg="white")
        entry_frame.pack(pady=20)



        # Selección de producto con Combobox
        lbl_nombre = tk.Label(entry_frame, text="Nombre del producto", font=("Segoe UI", 14), bg="white")
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10)

        productos = traer_todos_los_productos()  # Obtener los productos

        producto_list = [producto[0] for producto in productos]  # Lista con los nombres de los productos

        combobox_nombre = ttk.Combobox(entry_frame, values=producto_list, width=20, font=("Segoe UI", 16), height=5)
        combobox_nombre.grid(row=1, column=0, padx=10, pady=10)
        combobox_nombre.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))

        # Vincular la función de autocompletar al evento de escritura
        combobox_nombre.bind('<KeyRelease>', on_key_release)    

        # Campo de precio editable
        lbl_precio = tk.Label(entry_frame, text="Precio actual a editar", font=("Segoe UI", 14), bg="white")
        lbl_precio.grid(row=0, column=1, padx=10, pady=10)
        entry_precio = tk.Entry(entry_frame, width=20, bg="#d7d7d7", font=("Segoe UI", 16))
        entry_precio.grid(row=1, column=1, padx=10, pady=10)

        # Campo de cantidad no editable
        lbl_cantidad = tk.Label(entry_frame, text="Stock", font=("Segoe UI", 14), bg="white")
        lbl_cantidad.grid(row=0, column=2, padx=10, pady=10)
        entry_cantidad = tk.Entry(entry_frame, width=20, bg="#d7d7d7", font=("Segoe UI", 16), state='readonly')
        entry_cantidad.grid(row=1, column=2, padx=10, pady=10)

        # Campo de categoria no editable
        lbl_categoria = tk.Label(entry_frame, text="Categoria", font=("Segoe UI", 14), bg="white")
        lbl_categoria.grid(row=0, column=3, padx=10, pady=10)
        entry_categoria= tk.Entry(entry_frame, width=20, bg="#d7d7d7", font=("Segoe UI", 16), state='readonly')
        entry_categoria.grid(row=1, column=3, padx=10, pady=10)


        # Campo de proveedor no editable
        lbl_proveedor = tk.Label(entry_frame, text="Proveedor", font=("Segoe UI", 14), bg="white")
        lbl_proveedor.grid(row=0, column=4, padx=10, pady=10)
        entry_proveedor = tk.Entry(entry_frame, width=20, bg="#d7d7d7", font=("Segoe UI", 16), state='readonly')
        entry_proveedor.grid(row=1, column=4, padx=10, pady=10)

        # Crear el Label de advertencia
        advertencia_label = tk.Label(confirm_window, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack()

        # Cargar los datos del producto seleccionado
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
                    entry_categoria.insert(0, producto[3])  # Ctegoria
                    entry_categoria.config(state='readonly')

                    entry_proveedor.config(state='normal')
                    entry_proveedor.delete(0, tk.END)
                    entry_proveedor.insert(0, producto[4])  # Proveedor
                    entry_proveedor.config(state='readonly')

        combobox_nombre.bind("<<ComboboxSelected>>", cargar_datos_producto)


    # Función para actualizar los datos
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
                    advertencia_label.config(text="Actualice el precio porfavor")

                else:
                    actualizar_producto(nombre_producto, precio_producto)
                    
                    on_no()
                return

            else:
                advertencia_label.config(text="Debe ingresar solo números")
                return

        def on_no():
            confirm_window.destroy()  # Cerrar la ventana
          

        button_frame = tk.Frame(confirm_window, bg="white")
        button_frame.pack(pady=20)

        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

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

    def mostrar_arbol_productos(self):
        # Limpiar el área derecha si ya hay contenido
        for widget in self.master.pack_slaves():
            if isinstance(widget, tk.Frame) and widget.winfo_x() > 310:
                widget.destroy()

        # Estilo personalizado para agrandar la fuente de la tabla y aumentar la altura de las filas
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 16, "bold"))  # Agranda la fuente de los encabezados
        style.configure("Treeview", font=("Segoe UI", 14), rowheight=30)   # Agranda la fuente de las filas y ajusta la altura
        style.configure("Rojo.TLabel", foreground="red")

        # Frame derecho para mostrar la tabla
        frame_derecho = tk.Frame(self.master, padx=10, pady=10)
        frame_derecho.place(x=320, y=0, width=self.master.winfo_width() - 320, height=self.master.winfo_height())

        # Título para la tabla
        label_tabla = tk.Label(frame_derecho, text="Productos", font=("Courier New", 24, "bold"), fg="black", relief="flat")
        label_tabla.pack(pady=20)

        # Tabla (Treeview) para mostrar los productos
        tree = ttk.Treeview(frame_derecho, columns=("nombre", "cantidad", "precio", "categoria", "proveedor"), show="headings", height=10)

        # Definir las columnas con doble clic
        tree.heading("nombre", text="Nombre")
        tree.heading("cantidad", text="Cantidad")
        tree.heading("precio", text="Precio")
        tree.heading("categoria", text="Categoria")
        tree.heading("proveedor", text="Proveedor")

        # Definir el ancho de las columnas
        tree.column("nombre", width=200)
        tree.column("cantidad", width=100, anchor="center")
        tree.column("precio", width=100, anchor="center")
        tree.column("categoria", width=150, anchor="center")
        tree.column("proveedor", width=150, anchor="center")

        # Empaquetar la tabla
        tree.pack(fill=tk.BOTH, expand=True)

    def mostrar_buscar_datos(self):
        self.buscar_datos.mostrar()

    def mostrar_administracion(self):
        self.administracion.mostrar()




# Crear la ventana principal
root = tk.Tk()
app = Minimarket(root, "mariano", True)
root.mainloop()