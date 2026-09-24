# 🍽️ Restaurante App
# Jonnathan Paul Deleg Condo

Aplicación de escritorio desarrollada en **Python** utilizando **Programación Orientada a Objetos (POO)** y la biblioteca gráfica **Tkinter/ttk**.

El proyecto corresponde a la evolución de la aplicación `restaurante_app` desarrollada durante las semanas anteriores de la asignatura. En esta **Semana 15** se incorpora el concepto fundamental de **manejo de eventos**, utilizando el registro de ventas como ejemplo práctico.

La aplicación permite gestionar usuarios y productos, registrar ventas y almacenar la información de manera persistente mediante archivos **JSON**.

---

## 📚 Semana 15

### Tema

**Conceptos fundamentales de manejo de eventos**

### Objetivo

Implementar una operación de venta que permita comprender cómo una acción realizada por el usuario en una interfaz gráfica genera un evento que es atendido mediante un `callback`, el cual coordina la operación con la capa de servicios.

El flujo principal implementado es:

```text
Usuario
   ↓
Acción en la interfaz
   ↓
Botón
   ↓
command=
   ↓
Callback
   ↓
RestauranteServicio
   ↓
Persistencia en JSON
   ↓
Actualización de la interfaz
   ↓
Respuesta visual
```

---

# 🎯 Objetivos del proyecto

## Objetivo general

Continuar el desarrollo de `restaurante_app`, incorporando el registro de ventas y aplicando los fundamentos básicos del manejo de eventos en una aplicación gráfica desarrollada con Tkinter.

## Objetivos específicos

* Mantener la arquitectura modular desarrollada en las semanas anteriores.
* Conservar el inicio de sesión de la aplicación.
* Mantener la gestión y consulta de productos.
* Mantener la consulta de usuarios.
* Incorporar una nueva sección de ventas.
* Crear el modelo `Venta`.
* Relacionar usuarios con productos mediante una venta.
* Utilizar `command=` en los botones de la interfaz.
* Implementar callbacks para responder a las acciones del usuario.
* Delegar las reglas de negocio a `RestauranteServicio`.
* Guardar las ventas en `ventas.json`.
* Mostrar las ventas registradas mediante un `Treeview`.
* Actualizar la información de la interfaz después de una venta.
* Utilizar la carpeta `assets/` para recursos visuales.
* Mantener una separación clara entre interfaz, modelos, servicios y datos.

---

# 🏗️ Arquitectura del proyecto


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
│
│
├── main.py
└── README.md
```

---

# 📂 Descripción de las carpetas y archivos

## 📁 datos/

Contiene los archivos JSON utilizados para almacenar la información de la aplicación.

### `productos.json`

Almacena los productos registrados.

Cada producto contiene información como:

* Código
* Nombre
* Categoría
* Precio

Ejemplo:

```json
[
    {
        "codigo": "P001",
        "nombre": "Hamburguesa",
        "categoria": "Comida",
        "precio": 4.5,
    }
]
```

### `usuarios.json`

Almacena los usuarios que pueden utilizar la aplicación.

Ejemplo:

```json
[
    {
        "identificacion": "001",
        "nombre": "Administrador",
        "usuario": "admin",
        "password": "1234"
    }
]
```

### `ventas.json`

Es el nuevo archivo incorporado en la Semana 15.

Permite conservar las ventas realizadas.

Ejemplo:

```json
[
    {
        "usuario_id": "001",
        "producto_codigo": "P001",
        "fecha": "2026-09-24 09:35:20"
    }
]
```

---

# 📁 modelos/

Contiene las clases que representan las entidades principales de la aplicación.

## `producto.py`

Contiene la clase `Producto`.

La clase utiliza propiedades y setters para controlar los datos del producto.

Entre sus atributos se encuentran:

* `codigo`
* `nombre`
* `categoria`
* `precio`

También contiene métodos para convertir los objetos a diccionarios y reconstruirlos desde los datos almacenados en JSON.

---

## `usuario.py`

Contiene la clase `Usuario`.

Representa a las personas registradas en el sistema.

Sus principales atributos son:

* `identificacion`
* `nombre`
* `usuario`
* `password`

La clase también utiliza `@property` y setters para controlar los valores.

---

## `venta.py`

Es el nuevo modelo agregado en la Semana 15.

Representa una operación de venta y relaciona:

```text
Usuario + Producto + Fecha
```

Sus principales atributos son:

* `usuario_id`
* `producto_codigo`
* `fecha`

La clase también permite convertir una venta en un diccionario mediante `to_dict()` para almacenarla en `ventas.json`.

---

# 📁 servicios/

Contiene la lógica de funcionamiento de la aplicación.

## `archivo_servicio.py`

Se encarga de la lectura y escritura de archivos JSON.

Sus principales responsabilidades son:

* Leer archivos JSON.
* Guardar información en archivos JSON.
* Crear carpetas necesarias.
* Manejar errores relacionados con los archivos.

La interfaz gráfica no manipula directamente los archivos JSON.

---

## `restaurante_servicio.py`

Contiene las reglas de negocio de la aplicación.

Entre sus responsabilidades se encuentran:

* Validar el inicio de sesión.
* Consultar usuarios.
* Buscar productos.
* Registrar productos.
* Actualizar productos.
* Eliminar productos.
* Registrar ventas.
* Verificar que el usuario exista.
* Verificar que el producto exista.
* Verificar que exista stock.
* Disminuir el stock después de una venta.
* Guardar productos.
* Guardar ventas.

La operación de venta sigue el siguiente proceso:

```text
Buscar usuario
      ↓
¿Existe?
      ↓
Buscar producto
      ↓
¿Existe?
      ↓
¿Tiene stock?
      ↓
Disminuir stock
      ↓
Crear venta
      ↓
Guardar venta
```

---

# 📁 ui/

Contiene las ventanas y componentes gráficos desarrollados con Tkinter y ttk.

## `login_view.py`

Contiene la interfaz de inicio de sesión.

Permite ingresar:

* Usuario
* Contraseña

El botón de ingreso utiliza un evento mediante `command=`.

Ejemplo:

```python
ttk.Button(
    frame,
    text="Ingresar",
    command=self.iniciar_sesion
)
```

El callback `iniciar_sesion()` obtiene los datos introducidos y solicita al servicio la validación correspondiente.

---

## `main_view.py`

Contiene la ventana principal de la aplicación.

La interfaz está organizada en diferentes secciones:

* Usuarios
* Productos
* Ventas

La sección de productos mantiene las operaciones desarrolladas anteriormente:

* Registrar
* Consultar
* Actualizar
* Eliminar
* Limpiar

La nueva sección de ventas permite:

* Seleccionar un usuario.
* Seleccionar un producto.
* Registrar una venta.
* Consultar las ventas realizadas.
* Actualizar la información después de una operación.

---

# 🖼️ Carpeta assets/

La carpeta `assets/` contiene los recursos visuales utilizados por la aplicación.

Ejemplo:

```text
assets/

Estos recursos permiten mejorar la presentación visual de la aplicación y cumplir con el requisito de utilizar un logotipo e íconos dentro de la interfaz.

---

# ⚡ Manejo de eventos

Uno de los principales objetivos de la Semana 15 es comprender el funcionamiento de los eventos.

En Tkinter, un botón puede ejecutar una función mediante el parámetro:

```python
command=
```

Por ejemplo:

```python
self.btn_registrar_venta = ttk.Button(
    frame_venta,
    text="Registrar venta",
    command=self.registrar_venta
)
```

Cuando el usuario presiona el botón, Tkinter ejecuta:

```python
self.registrar_venta()
```

Este método funciona como **callback**.

---

# 🔄 Flujo del evento de una venta

El registro de una venta sigue el siguiente flujo:

```text
1. El usuario selecciona un usuario
                ↓
2. El usuario selecciona un producto
                ↓
3. Presiona "Registrar venta"
                ↓
4. Tkinter detecta el evento
                ↓
5. command= ejecuta el callback
                ↓
6. El callback obtiene las selecciones
                ↓
7. Se llama a RestauranteServicio
                ↓
8. El servicio valida la operación
                ↓
9. Se disminuye el stock
                ↓
10. Se crea la venta
                ↓
11. Se guarda en ventas.json
                ↓
12. Se actualiza el Treeview
                ↓
13. Se muestra un mensaje al usuario
```

Este proceso permite observar cómo una acción realizada en la interfaz puede generar una respuesta en toda la aplicación.

---

# 🛒 Registro de una venta

Para registrar una venta se deben cumplir las siguientes condiciones:

1. El usuario debe existir.
2. El producto debe existir.

Cuando todas las condiciones se cumplen:

```text
Usuario seleccionado
        +
Producto seleccionado
        ↓
Registro de venta
        ↓
Guardado en ventas.json
```

La venta queda registrada en `ventas.json`.

---

# 📊 Visualización de las ventas

Las ventas registradas se muestran mediante un componente `Treeview`.

La tabla presenta información como:

| Usuario       | Producto    | Fecha               |
| ------------- | ----------- | ------------------- |
| Administrador | Hamburguesa | 2026-09-24 09:35:20 |

Después de registrar una venta, la tabla se actualiza automáticamente.

Esto permite que el usuario observe inmediatamente el resultado de la acción realizada.

---

# 💾 Persistencia

La información de la aplicación se mantiene mediante archivos JSON.

Los principales archivos son:

```text
productos.json
usuarios.json
ventas.json
```

La información de las ventas se guarda mediante:

```python
self.guardar_ventas()
```

El archivo se actualiza después de registrar correctamente una venta.

Al cerrar y volver a ejecutar la aplicación, las ventas almacenadas pueden recuperarse nuevamente.

---

# 🧩 Separación de responsabilidades

El proyecto mantiene una separación de responsabilidades.

### Interfaz gráfica

Se encarga de:

* Mostrar información.
* Recibir datos del usuario.
* Detectar eventos.
* Ejecutar callbacks.
* Mostrar mensajes.

### Callback

Se encarga de:

* Obtener los datos seleccionados.
* Coordinar la operación.
* Llamar al servicio.
* Actualizar la interfaz.

### RestauranteServicio

Se encarga de:

* Validar reglas de negocio.
* Buscar usuarios.
* Buscar productos.
* Verificar stock.
* Crear ventas.
* Solicitar la persistencia.

### ArchivoServicio

Se encarga de:

* Leer JSON.
* Guardar JSON.

### Modelos

Representan las entidades:

```text
Usuario
Producto
Venta
```

# ⚠️ Validaciones implementadas

El sistema controla diferentes situaciones.

### Usuario vacío

Si no se selecciona un usuario:

```text
Seleccione un usuario.
```

### Producto vacío

Si no se selecciona un producto:

```text
Seleccione un producto.
```

### Usuario inexistente

El servicio informa:

```text
El usuario seleccionado no existe.
```

### Producto inexistente

El servicio informa:

```text
El producto seleccionado no existe.
```



---

# 📦 Requisitos

Para ejecutar el proyecto se necesita:

* Python instalado.
* Tkinter disponible.
* Los archivos JSON dentro de la carpeta `datos`.
* La estructura de carpetas del proyecto correctamente organizada.



El inicio de sesión tiene finalidad académica y utiliza los datos almacenados en `usuarios.json`.

---

# ▶️ Ejecución

Desde la carpeta principal del proyecto ejecutar:

```bash
python main.py
```

---

# 📌 Evolución del proyecto

El proyecto representa una evolución progresiva:

```text
Semanas anteriores
       ↓
Modelos y POO
       ↓
Persistencia JSON
       ↓
Interfaz gráfica Tkinter
       ↓
Gestión de productos y usuarios
       ↓
Semana 15
       ↓
Manejo de eventos
       ↓
Registro de ventas
```

De esta manera, la Semana 15 no reconstruye el proyecto desde cero, sino que agrega una nueva funcionalidad sobre la aplicación existente.

---

# 🧠 Conceptos de POO aplicados

El proyecto utiliza diferentes conceptos de Programación Orientada a Objetos.

### Encapsulamiento

Se utilizan atributos privados mediante variables como:

```python
self._nombre
self._precio

```

y se accede a ellos mediante propiedades.

### Propiedades

Se utilizan:

```python
@property
```

y setters para controlar los datos de los objetos.

### Clases

El sistema cuenta con clases como:

```text
Producto
Usuario
Venta
ArchivoServicio
RestauranteServicio
LoginView
MainView
```

### Separación de responsabilidades

Cada componente realiza una función específica para evitar concentrar toda la lógica en un solo archivo.

---

# 📈 Resultado esperado

Al finalizar la Semana 15, `restaurante_app` debe permitir:

* Iniciar sesión.
* Consultar usuarios.
* Registrar productos.
* Consultar productos.
* Actualizar productos.
* Eliminar productos.
* Seleccionar usuarios.
* Seleccionar productos.
* Registrar ventas.
* Disminuir automáticamente el stock.
* Guardar las ventas en `ventas.json`.
* Recuperar las ventas al reiniciar.
* Mostrar las ventas en una tabla.
* Responder a las acciones mediante eventos y callbacks.
* Utilizar recursos gráficos desde `assets/`.

---

# 📝 Conclusiones

1. La incorporación de la sección de ventas permitió comprender de manera práctica cómo funcionan los eventos en una aplicación gráfica, ya que una acción realizada por el usuario puede activar un botón mediante `command=` y ejecutar un callback.

2. El uso de callbacks permite conectar las acciones realizadas en la interfaz con los métodos del sistema, manteniendo una comunicación organizada entre la interfaz gráfica y la capa de servicios.

3. La utilización de `RestauranteServicio` permite mantener las reglas de la venta fuera de la interfaz, facilitando la separación de responsabilidades y evitando que la lógica del negocio se concentre directamente en Tkinter.

4. La incorporación de `ventas.json` permitió conservar las operaciones realizadas y comprobar la importancia de la persistencia de información en una aplicación que trabaja con archivos.

5. El registro de ventas también permitió relacionar los conceptos de usuarios, productos y stock, demostrando cómo diferentes objetos pueden interactuar dentro de una aplicación orientada a objetos.

6. Finalmente, la evolución de `restaurante_app` permitió integrar los conocimientos adquiridos durante las semanas anteriores, manteniendo una arquitectura modular y agregando nuevas funcionalidades sin reconstruir completamente el proyecto.
