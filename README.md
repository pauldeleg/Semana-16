# Restaurante App

## Semana 16 - Manejo de eventos en Tkinter
# Jonnathan Paul Deleg Condo

## 1. Descripción del proyecto

**Restaurante App** es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos y la biblioteca Tkinter para la creación de una interfaz gráfica.

El proyecto ha evolucionado durante las semanas anteriores incorporando diferentes funcionalidades para la administración de un restaurante, como el inicio de sesión, gestión de productos, registro de ventas y persistencia de información mediante archivos JSON.

En la **Semana 16** se incorporó principalmente el manejo de eventos en Tkinter para implementar una gestión de usuarios más interactiva mediante `bind()`, eventos de teclado, eventos virtuales de `ttk`, callbacks, `command=` y el componente `Treeview`.

---

## 2. Objetivo de la Semana 16

Aplicar el manejo de eventos en Tkinter dentro de una aplicación existente, utilizando diferentes mecanismos de interacción con el usuario sin modificar la arquitectura modular del proyecto.

La implementación permite trabajar con:

* Eventos de teclado.
* Eventos virtuales de ttk.
* `bind()`.
* `command=`.
* Callbacks.
* `Treeview`.
* `Combobox`.
* Gestión de usuarios.
* Roles de usuario.
* Persistencia mediante `usuarios.json`.

---
## 3. Funcionalidades de la aplicación

La aplicación permite realizar las siguientes operaciones:

### Inicio de sesión

El sistema permite iniciar sesión utilizando un usuario y una contraseña almacenados en `usuarios.json`.

### Gestión de usuarios

El Administrador puede:

* Registrar usuarios.
* Consultar usuarios.
* Actualizar usuarios.
* Eliminar usuarios.
* Seleccionar usuarios desde un `Treeview`.
* Asignar roles.

### Gestión de productos

La aplicación permite:

* Registrar productos.
* Consultar productos.
* Actualizar productos.
* Eliminar productos.
* Controlar el precio.
* Guardar los productos en `productos.json`.

### Gestión de ventas

La aplicación permite:

* Seleccionar un usuario.
* Seleccionar un producto.
* Registrar una venta.
* Guardar las ventas en `ventas.json`.
* Consultar las ventas registradas.

---

## 4. Roles del sistema

La aplicación utiliza tres roles:

* **Administrador**
* **Empleado**
* **Cliente**

### Administrador

El Administrador tiene acceso a la gestión de usuarios.

Puede registrar, consultar, actualizar y eliminar usuarios.

### Empleado

El Empleado puede utilizar las funciones generales de la aplicación, pero no tiene acceso a la administración de usuarios.

### Cliente

El Cliente puede utilizar las funciones permitidas por la aplicación, pero no tiene acceso a la administración de usuarios.

---

## 5. Manejo de eventos

Una de las principales mejoras realizadas durante la Semana 16 fue la incorporación de diferentes mecanismos para manejar eventos en Tkinter.

---

### 6.1 `command=`

Los botones utilizan `command=` para ejecutar una función cuando el usuario los presiona.

Por ejemplo:

```python
ttk.Button(
    formulario,
    text="Registrar",
    command=self.registrar_usuario
)
```

Cuando el usuario presiona el botón **Registrar**, se ejecuta el método `registrar_usuario()`.

También se utiliza para los botones:

* Registrar.
* Actualizar.
* Eliminar.
* Limpiar.
* Registrar venta.

---

### 6.2 `bind()`

El método `bind()` permite asociar un evento de Tkinter con una función callback.

En la aplicación se utiliza para detectar diferentes acciones del usuario.

Por ejemplo:

```python
self.tree_usuarios.bind(
    "<<TreeviewSelect>>",
    self.on_usuario_selected
)
```

Esto permite ejecutar `on_usuario_selected()` cuando el usuario selecciona una fila del Treeview.

---

## 6. Evento `<<TreeviewSelect>>`

El evento virtual:

```text
<<TreeviewSelect>>
```

se utiliza para detectar la selección de un usuario en el Treeview.

El funcionamiento es:

```text
Usuario selecciona una fila
        ↓
<<TreeviewSelect>>
        ↓
on_usuario_selected()
        ↓
Obtiene la identificación
        ↓
RestauranteServicio.buscar_usuario()
        ↓
Obtiene el objeto Usuario
        ↓
Carga los datos en el formulario
```

La identificación de la fila se utiliza para consultar el objeto correspondiente mediante `RestauranteServicio`.

El Treeview muestra solamente:

* Identificación.
* Nombre.
* Usuario.
* Rol.

La contraseña no se muestra en la tabla.

---

## 7. Evento `<Return>`

El evento:

```text
<Return>
```

permite utilizar la tecla **Enter** como atajo para registrar un usuario.

Se implementa mediante:

```python
self.root.bind(
    "<Return>",
    self.on_enter
)
```

El callback reutiliza el método de registro:

```python
def on_enter(self, event):
    self.registrar_usuario()
```

De esta manera no se duplica la lógica de registro dentro del evento.

---

## 8. Evento `<Escape>`

El evento:

```text
<Escape>
```

permite limpiar el formulario.

Se implementa mediante:

```python
self.root.bind(
    "<Escape>",
    self.on_escape
)
```

El callback ejecuta:

```python
def on_escape(self, event):
    self.limpiar_usuario()
```

También se elimina la selección actual del Treeview.

---

## 9. Evento `<<ComboboxSelected>>`

El formulario de usuarios utiliza un `Combobox` para seleccionar el rol.

Las opciones disponibles son:

```text
Administrador
Empleado
Cliente
```

El evento:

```text
<<ComboboxSelected>>
```

detecta cuando cambia el rol seleccionado.

Se implementa mediante:

```python
self.combo_rol.bind(
    "<<ComboboxSelected>>",
    self.on_rol_selected
)
```

El callback responde al cambio realizado por el usuario.

---

## 10. Callbacks

Los callbacks son métodos que se ejecutan como respuesta a determinadas acciones o eventos.

Además, los botones utilizan métodos como:

```text
registrar_usuario()
actualizar_usuario()
eliminar_usuario()
limpiar_usuario()
```

Los callbacks de la interfaz no contienen directamente las reglas principales del negocio.

La interfaz solicita las operaciones a `RestauranteServicio`.

---

## 11. Arquitectura del proyecto

El proyecto mantiene una arquitectura modular para separar las responsabilidades.

```text
Modelos
   ↓
Servicios
   ↓
Interfaz gráfica
   ↓
main.py
```

### Modelos

Los modelos representan las entidades principales del restaurante:

```text
Producto
Usuario
Venta
```

Los archivos correspondientes son:

```text
modelos/
├── producto.py
├── usuario.py
└── venta.py
```

---

### Servicios

La capa de servicios contiene las reglas y operaciones del sistema.

```text
servicios/
├── archivo_servicio.py
└── restaurante_servicio.py
```

`RestauranteServicio` se encarga de:

* Validar usuarios.
* Registrar usuarios.
* Actualizar usuarios.
* Eliminar usuarios.
* Buscar usuarios.
* Registrar productos.
* Actualizar productos.
* Eliminar productos.
* Registrar ventas.
* Coordinar la persistencia.

`ArchivoServicio` se encarga de leer y guardar los archivos JSON.

---

### Interfaz gráfica

La interfaz utiliza Tkinter y ttk.

```text
ui/
├── login_view.py
└── main_view.py
```

### `LoginView`

Se encarga del inicio de sesión.

### `MainView`

Se encarga de mostrar y coordinar:

* Usuarios.
* Productos.
* Ventas.
* Formularios.
* Botones.
* Treeview.
* Combobox.
* Eventos.

---

## 12. Persistencia de datos

La aplicación utiliza archivos JSON para conservar la información.

La carpeta `datos` contiene:

```text
datos/
├── productos.json
├── usuarios.json
└── ventas.json
```

### usuarios.json

Almacena información de los usuarios:

```json
[
    {
        "identificacion": "001",
        "nombre": "Administrador",
        "usuario": "admin",
        "password": "1234",
        "rol": "Administrador"
    }
]
```

### productos.json

Almacena los productos registrados.

### ventas.json

Almacena las ventas realizadas.

La interfaz gráfica no realiza directamente operaciones de lectura o escritura sobre los archivos JSON.

El flujo de persistencia es:

```text
MainView
    ↓
RestauranteServicio
    ↓
ArchivoServicio
    ↓
Archivo JSON
```

---

## 13. Gestión de usuarios mediante Treeview

El Treeview utilizado para los usuarios contiene las siguientes columnas:

```text
Identificación | Nombre | Usuario | Rol
```

Ejemplo:

```text
001 | Administrador | admin     | Administrador
002 | Carlos        | empleado  | Empleado
003 | Paul          | cliente   | Cliente
```

La contraseña no se muestra en el Treeview.

Cuando se selecciona una fila, se obtiene la identificación del usuario y se realiza una búsqueda mediante `RestauranteServicio`.

---

## 14. Validaciones

Las validaciones se encuentran principalmente en la capa de servicios y en los modelos.

Entre las validaciones implementadas se encuentran:

* La identificación del usuario es obligatoria.
* El nombre es obligatorio.
* El nombre de usuario es obligatorio.
* La contraseña es obligatoria.
* El rol debe ser válido.
* No se permiten identificaciones de usuario duplicadas.
* No se permiten nombres de usuario duplicados.
* No se puede eliminar el usuario actualmente conectado.
* El código del producto es obligatorio.
* No se permiten códigos de productos duplicados.
* El precio no puede ser negativo.
* No se puede registrar una venta si no existe stock.

---

## 15. Recursos visuales

El proyecto utiliza la carpeta:

```text
assets/
```

para almacenar los recursos visuales.

La estructura es:

```text
assets/
├── logo.png
├── usuario.png
├── producto.png
└── venta.png
```

El archivo `logo.png` se utiliza como logotipo de la aplicación.

Los demás recursos pueden utilizarse como íconos relacionados con las diferentes secciones del sistema.

---

## 16. Estructura completa del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
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
├── assets/
│   ├── logo.png
│   ├── usuario.png
│   ├── producto.png
│   └── venta.png
│
└── main.py
|__README.md
```



---


## 17. Evolución del proyecto

El proyecto mantiene la continuidad con las semanas anteriores.

La evolución se puede resumir de la siguiente manera:

```text
Semanas anteriores
        ↓
Programación Orientada a Objetos
        ↓
Productos
        ↓
Usuarios
        ↓
Persistencia JSON
        ↓
Ventas
        ↓
Interfaz Tkinter
        ↓
Componentes y contenedores
        ↓
Eventos y callbacks
        ↓
Semana 16
Gestión de usuarios mediante eventos
```

La Semana 16 no reemplaza las funcionalidades anteriores, sino que las amplía mediante el manejo de eventos.

---

## 18. Conclusión

La implementación de la Semana 16 permitió incorporar el manejo de eventos a la aplicación Restaurante App.

Mediante `bind()` se asociaron eventos de teclado y eventos virtuales de ttk con diferentes callbacks. El evento `<<TreeviewSelect>>` permite seleccionar usuarios y cargar sus datos en el formulario, mientras que `<Return>` y `<Escape>` facilitan la interacción mediante el teclado.

También se utilizó `<<ComboboxSelected>>` para responder a la selección de roles y `command=` para ejecutar las operaciones de los botones.

La lógica de negocio y la persistencia se mantienen separadas de la interfaz gráfica mediante `RestauranteServicio` y `ArchivoServicio`. Los usuarios se almacenan en `usuarios.json`, permitiendo conservar la información después de cerrar y volver a ejecutar la aplicación.

De esta manera, Restaurante App conserva las funcionalidades desarrolladas anteriormente y evoluciona incorporando una gestión de usuarios basada en eventos, manteniendo una arquitectura modular y coherente con el dominio de un restaurante.
