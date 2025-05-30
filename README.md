# 🛒 Tienda Web Completa con Integración WhatsApp

Una tienda web moderna y funcional desarrollada con Flask (Python) que integra WhatsApp para finalizar las compras.

## ✨ Características Principales

- **Backend robusto**: Desarrollado en Python Flask con sesiones seguras
- **Diseño responsive**: Interfaz moderna con Tailwind CSS
- **Carrito de compras**: Funcionalidad completa con persistencia de sesión
- **Integración WhatsApp**: Envío automático de pedidos al WhatsApp del vendedor
- **Gestión de productos**: Catálogo dinámico con imágenes y descripciones
- **Experiencia de usuario**: Animaciones suaves y notificaciones en tiempo real

## 🚀 Funcionalidades

### Para el Cliente:
- Navegar por el catálogo de productos
- Ver detalles de cada producto
- Agregar productos al carrito
- Modificar cantidades en el carrito
- Eliminar productos del carrito
- Envío automático del pedido por WhatsApp

### Para el Administrador:
- Gestión de productos desde el código
- Configuración de número de WhatsApp
- Personalización de información de la tienda

## 📁 Estructura del Proyecto

```
tienda-web/
├── app.py                 # Aplicación principal de Flask
├── requirements.txt       # Dependencias de Python
├── templates/
│   ├── index.html        # Página principal
│   ├── carrito.html      # Página del carrito
│   └── producto.html     # Página de producto individual
├── static/
│   ├── css/
│   ├── js/
│   └── img/
└── README.md
```

## 🛠️ Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
```bash
mkdir tienda-web
cd tienda-web
```

2. **Crear entorno virtual**
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar la aplicación**
   - Edita `app.py` y modifica la variable `TIENDA_CONFIG`:
   ```python
   TIENDA_CONFIG = {
       'nombre': 'Tu Tienda Online',
       'whatsapp': '+521234567890',  # Tu número de WhatsApp
       'moneda': 'MXN'
   }
   ```

5. **Ejecutar la aplicación**
```bash
python app.py
```

6. **Acceder a la tienda**
   - Abre tu navegador en: `http://localhost:5000`

## ⚙️ Configuración Personalizada

### Cambiar Productos

Edita la lista `PRODUCTOS` en `app.py`:

```python
PRODUCTOS = [
    {
        'id': 1,
        'nombre': 'Nombre del Producto',
        'precio': 999.99,
        'imagen': 'URL_de_la_imagen',
        'descripcion': 'Descripción del producto',
        'categoria': 'Categoría'
    },
    # Agregar más productos...
]
```

### Personalizar Configuración

```python
TIENDA_CONFIG = {
    'nombre': 'Nombre de tu tienda',
    'whatsapp': '+52XXXXXXXXXX',  # Número con código de país
    'moneda': 'MXN'  # o 'USD', 'EUR', etc.
}
```

## 📱 Integración WhatsApp

La aplicación genera automáticamente un mensaje con:
- Lista detallada de productos
- Cantidades y precios
- Total de la compra
- Formato profesional para el vendedor

El mensaje se envía al número configurado en `TIENDA_CONFIG['whatsapp']`.

## 🎨 Personalización Visual

### Colores y Estilos
- Modifica las clases CSS en los archivos HTML
- Cambia los gradientes en las variables CSS
- Personaliza los colores del tema

### Imágenes
- Usa URLs de imágenes públicas (Unsplash, etc.)
- O sube tus propias imágenes a la carpeta `static/img/`

## 🔧 Características Técnicas

### Backend (Flask)
- Gestión de sesiones para el carrito
- API RESTful para operaciones CRUD
- Manejo de errores y validaciones
- Estructura modular y escalable

### Frontend
- Diseño responsive con Tailwind CSS
- JavaScript vanilla para interactividad
- Animaciones CSS suaves
- Optimizado para móviles

### Seguridad
- Claves secretas para sesiones
- Validación de datos del lado del servidor
- Protección CORS configurada

## 🚀 Despliegue en Producción

### Opciones de Hosting
1. **Heroku** (Recomendado para principiantes)
2. **DigitalOcean App Platform**
3. **AWS Elastic Beanstalk**
4. **Google Cloud Run**

### Configuración para Producción
```python
# En app.py, cambiar para producción:
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

## 📞 Soporte y Contacto

Para soporte técnico o personalizaciones adicionales, puedes:
- Modificar el código según tus necesidades
- Agregar más productos editando la lista `PRODUCTOS`
- Personalizar el diseño modificando los archivos HTML

## 🔄 Actualizaciones Futuras

Funcionalidades planificadas:
- Panel de administración web
- Base de datos PostgreSQL/MySQL
- Sistema de usuarios y autenticación
- Múltiples métodos de pago
- Gestión de inventario
- Analytics y reportes

## 📋 Notas Importantes

- Asegúrate de tener el número de WhatsApp correcto
- Las imágenes deben ser URLs públicas accesibles
- La aplicación guarda el carrito en la sesión del navegador
- Para producción, considera usar una base de datos real

---

¡Tu tienda web está lista para recibir clientes! 🎉
