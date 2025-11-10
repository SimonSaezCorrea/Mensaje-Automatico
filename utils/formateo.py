import sys
import io
import os

# Función para convertir la primera letra de cada palabra a mayúscula
# y el resto a minúscula
def mayuscula(palabra):
    palabras = palabra.split(" ")
    palabra = " ".join([i.capitalize() for i in palabras])
    return palabra.strip()

# Función para formatear el número de teléfono
# Asegurando que tenga el formato correcto para WhatsApp
def formato(telefono):
    telefono = str(telefono).replace(" ", "")
    if len(telefono) < 8:
        return ""
    elif len(telefono) == 9:
        telefono = "+56" + telefono
    elif len(telefono) == 8:
        telefono = "+569" + telefono
    elif len(telefono) == 11:
        telefono = "+" + telefono
    return telefono

# Asegurar que la salida por consola use UTF-8 para que los prints muestren tildes y caracteres especiales
def _ensure_utf8_stdout():
    try:
        # Forzar modo UTF-8 en la sesión de Python si es posible
        os.environ.setdefault('PYTHONUTF8', '1')
        enc = getattr(sys.stdout, 'encoding', None)
        if not enc or enc.lower() != 'utf-8':
            try:
                sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
            except Exception:
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
            try:
                sys.stderr.reconfigure(encoding='utf-8', errors='backslashreplace')
            except Exception:
                sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='backslashreplace')
    except Exception:
        # Falla silenciosa: si no se puede reconfigurar, seguimos sin romper la ejecución
        pass