import os
import sys
import subprocess

def crear_estructura_directorios():
    directorios = [
        'templates',
        'static',
        'static/css',
        'static/js',
        'static/img'
    ]
    
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f"✅ Directorio creado: {directorio}")

def instalar_dependencias():
    """Instala las dependencias de Python"""
    print("📦 Instalando dependencias...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
    except subprocess.CalledProcessError:
        print("❌ Error al instalar dependencias")
        return False
    return True

def crear_archivo_env():
    """Crea un archivo de configuración .env"""
    config_template = """# Configuración de la Tienda Web
FLASK_SECRET_KEY=tu_clave_secreta_super_segura_2024
TIENDA_NOMBRE=Mi Tienda Online
WHATSAPP_NUMBER=+521234567890
MONEDA=MXN
FLASK_ENV=development
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(config_template)
        print("✅ Archivo .env creado")
    else:
        print("ℹ️  Archivo .env ya existe")

def mostrar_instrucciones():
    """Muestra las instrucciones finales"""
    print("\n" + "="*50)
    print("🎉 ¡INSTALACIÓN COMPLETADA!")
    print("="*50)
    print("\n📋 PRÓXIMOS PASOS:")
    print("1. Edita app.py y configura tu número de WhatsApp")
    print("2. Personaliza los productos en la variable PRODUCTOS")
    print("3. Ejecuta: python app.py")
    print("4. Abre tu navegador en: http://localhost:5000")
    print("\n⚙️  CONFIGURACIÓN IMPORTANTE:")
    print("- Cambia el número de WhatsApp en TIENDA_CONFIG")
    print("- Personaliza el nombre de tu tienda")
    print("- Agrega tus propios productos")
    print("\n🚀 Para ejecutar la tienda:")
    print("   python app.py")
    print("\n📱 La integración con WhatsApp funcionará automáticamente")
    print("="*50)

def main():
    print("🛒 CONFIGURADOR DE TIENDA WEB")
    print("="*40)
    
    # Verificar Python
    if sys.version_info < (3, 8):
        print("❌ Se requiere Python 3.8 o superior")
        return
    
    print(f"✅ Python {sys.version.split()[0]} detectado")
    
    # Crear estructura
    print("\n📁 Creando estructura de directorios...")
    crear_estructura_directorios()
    
    # Instalar dependencias
    print("\n📦 Verificando dependencias...")
    if os.path.exists('requirements.txt'):
        if instalar_dependencias():
            print("✅ Todas las dependencias están instaladas")
        else:
            print("❌ Error en la instalación de dependencias")
            return
    else:
        print("⚠️  Archivo requirements.txt no encontrado")
    
    # Crear archivo de configuración
    print("\n⚙️  Configurando entorno...")
    crear_archivo_env()
    
    # Mostrar instrucciones finales
    mostrar_instrucciones()

if __name__ == "__main__":
    main()