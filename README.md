# Restaurante App — Semana 14

## Jonnathan paul deleg condo

## Componentes y Contenedores

Aplicación desarrollada en Python para la asignatura **Programación Orientada a Objetos**, correspondiente a la Semana 14.

En esta etapa se continúa la evolución de `restaurante_app`, mejorando la interfaz gráfica mediante el uso de componentes, contenedores y gestores de geometría de Tkinter. Se incorporan operaciones de registro, consulta, actualización y eliminación de productos, manteniendo la separación de responsabilidades y la persistencia de información en archivos JSON.

## Objetivo

Aplicar los fundamentos de componentes y contenedores en Tkinter para construir una interfaz gráfica organizada, clara y funcional, que permita gestionar los productos de un restaurante mediante formularios y botones.

El proyecto conserva la estructura modular desarrollada en la Semana 13 y mantiene el uso de modelos, servicios, archivos JSON y vistas gráficas.

## Tecnologías utilizadas

* Python.
* Tkinter y ttk.
* Programación Orientada a Objetos (POO).
* Archivos JSON.
* Git y GitHub.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/ (opcional)
├── main.py
└── README.md
```

## Descripción de los componentes

### Carpeta `datos/`

Contiene los archivos JSON utilizados para almacenar información local.

* **productos.json:** almacena los productos registrados del restaurante.
* **usuarios.json:** almacena los usuarios y las credenciales utilizadas para el acceso.

### Carpeta `modelos/`

Contiene las clases que representan las entidades del sistema.

#### Producto

Representa los productos del restaurante, incluyendo código, nombre, categoría, precio y stock, según los atributos definidos en el proyecto.

El modelo mantiene el uso de `@property`, setters y validaciones para controlar la información de los productos.

#### Usuario

Representa los usuarios del sistema y sus datos de acceso.

Mantiene las propiedades, setters y validaciones implementadas previamente.

### Carpeta `servicios/`

Contiene la lógica de acceso a los datos y las operaciones del restaurante.

#### ArchivoServicio

Se encarga de leer y guardar la información en archivos JSON, manteniendo la responsabilidad de la persistencia.

#### RestauranteServicio

Centraliza las operaciones relacionadas con los productos y usuarios.

Sus responsabilidades incluyen:

* Registrar productos.
* Consultar y listar productos.
* Actualizar productos.
* Eliminar productos.
* Validar los datos de las operaciones.
* Validar el acceso de los usuarios.
* Proporcionar información a las vistas gráficas.

Las validaciones y operaciones de negocio se mantienen fuera de los botones y formularios de la interfaz.

### Carpeta `ui/`

Contiene las vistas de la interfaz gráfica desarrolladas con Tkinter.

#### LoginView

Presenta la pantalla de inicio de sesión y permite validar el acceso mediante usuario y contraseña.

#### MainView

Presenta el panel principal de la aplicación y organiza las secciones de usuarios y productos mediante componentes y contenedores.

La sección de productos incluye un formulario, botones de acción y un área para visualizar la información registrada.

## Componentes y contenedores utilizados

Durante esta semana se incorporan componentes de Tkinter y ttk para mejorar la organización de la interfaz.

Entre los componentes utilizados se encuentran:

* `Frame`: permite agrupar y organizar componentes.
* `Label`: muestra textos y títulos.
* `Entry`: permite ingresar datos de los productos.
* `Button`: ejecuta acciones mediante `command=`.
* `Treeview`: permite visualizar los productos en forma de tabla.
* `messagebox`: muestra mensajes de información, advertencia y error.

### Gestores de geometría

Se utilizan gestores de geometría de Tkinter para organizar los componentes de la interfaz:

* `pack()`: organiza los componentes dentro de un contenedor.
* `grid()`: organiza los componentes mediante filas y columnas.

Cada contenedor organiza sus elementos de forma clara, evitando mezclar innecesariamente los gestores de geometría en el mismo contenedor.

## Funcionalidades de productos

La sección de productos permite realizar las siguientes operaciones:

### Registrar producto

El usuario ingresa la información del producto mediante un formulario y presiona el botón de registro.

El servicio valida los datos, crea el producto y guarda la información en `productos.json`.

### Consultar productos

Permite cargar y visualizar los productos registrados en el archivo JSON mediante los servicios de la aplicación.

### Actualizar producto

Permite seleccionar o identificar un producto mediante el código definido en el proyecto y modificar sus datos.

Los cambios se validan y se guardan en `productos.json`.

### Eliminar producto

Permite eliminar un producto registrado mediante su identificador.

La operación se realiza a través de `RestauranteServicio` y se actualiza la información almacenada.

## Flujo de funcionamiento

```text
Inicio de la aplicación
          ↓
      LoginView
          ↓
Validación de credenciales
          ↓
      MainView
          ↓
Navegación por secciones
          ↓
       Productos
          ↓
Formulario y botones
          ↓
Registrar | Consultar | Actualizar | Eliminar
          ↓
RestauranteServicio
          ↓
ArchivoServicio
          ↓
productos.json
          ↓
Actualización de la interfaz
```

## Separación de responsabilidades

La aplicación mantiene una arquitectura modular:

* **UI:** coordina la interacción con el usuario.
* **RestauranteServicio:** ejecuta las operaciones y validaciones del dominio.
* **ArchivoServicio:** administra la lectura y escritura de archivos JSON.
* **Modelos:** representan las entidades `Producto` y `Usuario`.
* **Datos:** almacenan la información local de la aplicación.

Las vistas no manipulan directamente los archivos JSON. Las operaciones se solicitan a través de los servicios correspondientes.

## Persistencia de datos

La información de los productos se conserva mediante el archivo:

```text
datos/productos.json
```

Después de registrar, actualizar o eliminar un producto, los cambios se guardan mediante `ArchivoServicio`.

Esto permite que la información permanezca disponible después de cerrar y volver a ejecutar la aplicación.

## Ejecución

Para ejecutar el proyecto, se debe abrir una terminal en la carpeta principal de `restaurante_app` y utilizar:

```bash
python main.py
```


## Comprobaciones realizadas

La aplicación permite comprobar:

* Inicio correcto de la aplicación.
* Funcionamiento del inicio de sesión.
* Visualización de la interfaz principal.
* Consulta de usuarios registrados.
* Presentación organizada del formulario de productos.
* Registro de un nuevo producto.
* Consulta de productos existentes.
* Actualización de productos.
* Eliminación de productos.
* Persistencia de los cambios en `productos.json`.
* Actualización de la información mostrada en la interfaz.
* Uso de `RestauranteServicio` para las operaciones.
* Organización de componentes mediante contenedores y gestores de geometría.


## Conclusión

La Semana 14 permitió evolucionar la interfaz gráfica de `restaurante_app` mediante el uso de componentes, contenedores y gestores de geometría de Tkinter.

La incorporación de formularios y botones facilita la gestión de productos a través de las operaciones de registro, consulta, actualización y eliminación. Además, se conserva la arquitectura modular, la persistencia mediante archivos JSON y la separación de responsabilidades entre la interfaz, los servicios y los modelos.

Esta evolución establece una base organizada para continuar ampliando las funcionalidades del restaurante en las siguientes semanas.
