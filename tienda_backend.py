from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_super_segura_2024'
CORS(app)

# Configuración de la tienda
TIENDA_CONFIG = {
    'nombre': 'Mi samuel Online',
    'whatsapp': '+527721099217',  # Cambia por tu número de WhatsApp
    'moneda': 'MXN'
}

# Base de datos simulada de productos
PRODUCTOS = [
    {
        'id': 1,
        'nombre': 'iPhone 15 Pro',
        'precio': 25999.00,
        'imagen': 'https://images.unsplash.com/photo-1696446702294-9462c463ab0e?w=400',
        'descripcion': 'El iPhone más avanzado con chip A17 Pro y cámara de 48MP',
        'categoria': 'Tecnología'
    },
    {
        'id': 2,
        'nombre': 'MacBook Air M3',
        'precio': 32999.00,
        'imagen': 'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400',
        'descripcion': 'Laptop ultradelgada con chip M3 y batería de larga duración',
        'categoria': 'Tecnología'
    },
    {
        'id': 3,
        'nombre': 'Nike Air Max 270',
        'precio': 2899.00,
        'imagen': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400',
        'descripcion': 'Tenis deportivos con máximo confort y diseño moderno',
        'categoria': 'Deportes'
    },
    {
        'id': 4,
        'nombre': 'Sony WH-1000XM5',
        'precio': 7999.00,
        'imagen': 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=400',
        'descripcion': 'Audífonos inalámbricos con cancelación de ruido líder en la industria',
        'categoria': 'Audio'
    },
    {
        'id': 5,
        'nombre': 'Samsung Galaxy S24 Ultra',
        'precio': 29999.00,
        'imagen': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400',
        'descripcion': 'Smartphone premium con S Pen y cámara de 200MP',
        'categoria': 'Tecnología'
    },
    {
        'id': 6,
        'nombre': 'Adidas Ultraboost 23',
        'precio': 3299.00,
        'imagen': 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400',
        'descripcion': 'Tenis para running con tecnología Boost para máximo retorno de energía',
        'categoria': 'Deportes'
    },
    {
        'id': 7,
        'nombre': 'iPad Pro 12.9"',
        'precio': 23999.00,
        'imagen': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400',
        'descripcion': 'Tablet profesional con chip M2 y pantalla Liquid Retina XDR',
        'categoria': 'Tecnología'
    },
    {
        'id': 8,
        'nombre': 'Canon EOS R6 Mark II',
        'precio': 45999.00,
        'imagen': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400',
        'descripcion': 'Cámara mirrorless profesional con sensor full-frame de 24.2MP',
        'categoria': 'Fotografía'
    }
]

@app.route('/')
def index():
    return render_template('tienda_index.html', productos=PRODUCTOS, config=TIENDA_CONFIG)

@app.route('/api/productos')
def api_productos():
    return jsonify(PRODUCTOS)

@app.route('/api/producto/<int:producto_id>')
def api_producto(producto_id):
    producto = next((p for p in PRODUCTOS if p['id'] == producto_id), None)
    if producto:
        return jsonify(producto)
    return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/api/agregar-carrito', methods=['POST'])
def agregar_carrito():
    data = request.get_json()
    producto_id = data.get('producto_id')
    cantidad = data.get('cantidad', 1)
    
    # Buscar el producto
    producto = next((p for p in PRODUCTOS if p['id'] == producto_id), None)
    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    # Inicializar carrito si no existe
    if 'carrito' not in session:
        session['carrito'] = []
    
    # Verificar si el producto ya está en el carrito
    producto_en_carrito = next((item for item in session['carrito'] if item['id'] == producto_id), None)
    
    if producto_en_carrito:
        producto_en_carrito['cantidad'] += cantidad
    else:
        session['carrito'].append({
            'id': producto['id'],
            'nombre': producto['nombre'],
            'precio': producto['precio'],
            'imagen': producto['imagen'],
            'cantidad': cantidad
        })
    
    session.modified = True
    return jsonify({'mensaje': 'Producto agregado al carrito', 'carrito_items': len(session['carrito'])})

@app.route('/api/carrito')
def api_carrito():
    carrito = session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return jsonify({
        'items': carrito,
        'total': total,
        'count': len(carrito)
    })

@app.route('/api/actualizar-carrito', methods=['POST'])
def actualizar_carrito():
    data = request.get_json()
    producto_id = data.get('producto_id')
    nueva_cantidad = data.get('cantidad')
    
    if 'carrito' not in session:
        return jsonify({'error': 'Carrito vacío'}), 400
    
    # Encontrar y actualizar el producto
    for item in session['carrito']:
        if item['id'] == producto_id:
            if nueva_cantidad <= 0:
                session['carrito'].remove(item)
            else:
                item['cantidad'] = nueva_cantidad
            break
    
    session.modified = True
    return jsonify({'mensaje': 'Carrito actualizado'})

@app.route('/api/eliminar-carrito/<int:producto_id>', methods=['DELETE'])
def eliminar_del_carrito(producto_id):
    if 'carrito' not in session:
        return jsonify({'error': 'Carrito vacío'}), 400
    
    session['carrito'] = [item for item in session['carrito'] if item['id'] != producto_id]
    session.modified = True
    return jsonify({'mensaje': 'Producto eliminado del carrito'})

@app.route('/api/limpiar-carrito', methods=['POST'])
def limpiar_carrito():
    session.pop('carrito', None)
    return jsonify({'mensaje': 'Carrito limpiado'})

@app.route('/carrito')
def carrito():
    return render_template('tienda_carrito.html', config=TIENDA_CONFIG)

@app.route('/producto/<int:producto_id>')
def producto_detalle(producto_id):
    producto = next((p for p in PRODUCTOS if p['id'] == producto_id), None)
    if not producto:
        return "Producto no encontrado", 404
    return render_template('producto.html', producto=producto, config=TIENDA_CONFIG)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)