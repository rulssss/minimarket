import tkinter as tk

class Datos:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.label = tk.Label(self.frame, text="Contenido de Datos", font=("Arial", 20))
        self.label.pack(pady=20)

    def mostrar(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def ocultar(self):
        self.frame.pack_forget()


class BuscarDatos:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.label = tk.Label(self.frame, text="Contenido de Buscar Datos", font=("Arial", 20))
        self.label.pack(pady=20)

    def mostrar(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def ocultar(self):
        self.frame.pack_forget()


class Administracion:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="white")
        self.label = tk.Label(self.frame, text="Contenido de Administración", font=("Arial", 20))
        self.label.pack(pady=20)

    def mostrar(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def ocultar(self):
        self.frame.pack_forget()


class MinimarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimarket Software")

        # Configurar la ventana para que tome el tamaño de la pantalla sin ser pantalla completa
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

        ######### Crear la barra de navegación #############
        
        self.nav_bar = tk.Frame(self.root, bg="#d7d7d7")
        self.nav_bar.place(x=0, y=0, width=screen_width, height=60)

        # Crear los botones de la barra de navegación
        self.btn_datos = tk.Button(self.nav_bar, text="Datos", width=20, height=2, command=self.mostrar_datos)
        self.btn_datos.pack(side=tk.LEFT, padx=10)

        self.btn_buscar_datos = tk.Button(self.nav_bar, text="Buscar Datos", width=20, height=2, command=self.mostrar_buscar_datos)
        self.btn_buscar_datos.pack(side=tk.LEFT, padx=10)

        self.btn_administracion = tk.Button(self.nav_bar, text="Administración", width=20, height=2, command=self.mostrar_administracion)
        self.btn_administracion.pack(side=tk.LEFT, padx=10)

        ######### Crear el área blanca que cambia de acuerdo con el botón #########
        self.contenido = tk.Frame(self.root, bg="white")
        self.contenido.place(x=0, y=60, width=screen_width, height=screen_height - 60)

        # Crear instancias de las clases de contenido
        self.datos = Datos(self.contenido)
        self.buscar_datos = BuscarDatos(self.contenido)
        self.administracion = Administracion(self.contenido)

    def mostrar_datos(self):
        self.ocultar_secciones()
        self.datos.mostrar()

    def mostrar_buscar_datos(self):
        self.ocultar_secciones()
        self.buscar_datos.mostrar()

    def mostrar_administracion(self):
        self.ocultar_secciones()
        self.administracion.mostrar()

    def ocultar_secciones(self):
        self.datos.ocultar()
        self.buscar_datos.ocultar()
        self.administracion.ocultar()


if __name__ == "__main__":
    root = tk.Tk()
    app = MinimarketApp(root)
    root.mainloop()