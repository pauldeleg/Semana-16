import tkinter as tk
from pathlib import Path
from tkinter import ttk



class LoginView(tk.Frame):

    def __init__(self, master, restaurante_servicio, mostrar_main):
        super().__init__(master)
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main = mostrar_main
        
        self.usuario_entry = None
        self.contraseña_entry = None
        self.mensaje_error = None
        self.logo = None
        
        self.crear_interfaz()
        self.definir_estilos()
        
    def definir_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "login.TButton",
            background="#2563eb",
            foreground= "#ffffff",
            font=("Ariel", 11, "bold"),
            padding=(14, 8),
            borderwidth=0,
        )
        estilo.map("login.TButton", background=[("active", "#1d4ed8")]) 
        
    def cargar_logo(self):
        ruta_base = Path(__file__).resolve().parent.parent
        ruta_logo = ruta_base / "assets" / "logo" / "logo.png"
        
        if not ruta_logo.exists():
            return None
        
        logo_original = tk.PhotoImage(file=str(ruta_logo))
        self.logo = logo_original.subsample(3, 3)
        return self.logo       
        
    def crear_interfaz(self):
        # Construye los componentes visuales del login.
        contenedor = tk.Frame(self, bg="#ffffff", padx=32, pady=28)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")
        
        logo = self.cargar_logo()
        if logo is not None:
            tk.Label(
                contenedor,
                image=logo,
                bg="#ffffff",
            ).pack(pady=(0, 12))
            

        titulo = tk.Label(
            contenedor,
            text="Restaurante",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 22, "bold"),
        )
        titulo.pack(pady=(0, 6))

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesion",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11),
        )
        subtitulo.pack(pady=(0, 22))

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(contenedor, width=30, font=("Arial", 11))
        self.usuario_entry.pack(pady=(4, 14), ipady=4)
        self.usuario_entry.focus()

        tk.Label(
            contenedor,
            text="Contrasena",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.contraseña_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*"
        )
        
        self.contraseña_entry.pack(pady=(4, 14), ipady=4)
        

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#ffffff",
            fg="#b42318",
            font=("Arial", 10),
        )
        self.mensaje_error.pack(pady=(0, 14))

        boton = tk.Button(
            contenedor,
            text="Iniciar sesion",
            command=self.procesar_login,
            bg="#1565c0",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            pady=6
        )
        boton.pack(fill="x", pady=(15, 0))

    def procesar_login(self,):
        
        assert self.usuario_entry is not None
        assert self.contraseña_entry is not None
        assert self.mensaje_error is not None
        
        usuario = self.usuario_entry.get().strip()
        contraseña = self.contraseña_entry.get().strip()

        if not usuario or not contraseña:
            self.mensaje_error.config(text="Ingrese usuario y contraseña.")
            return

        usuario_validado = self.restaurante_servicio.validar_acceso(usuario, contraseña)

        if usuario_validado is None:
            self.mensaje_error.config(text="Credenciales incorrectas.")
            return

        self.mensaje_error.config(text="")
        self.mostrar_main(usuario_validado)
