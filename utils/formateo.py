"""
Módulo de formateo para texto y configuración de encoding.

Este módulo contiene funciones para formatear nombres y números de teléfono,
así como funcionalidades para asegurar la correcta visualización de caracteres
UTF-8 en consolas Windows.
"""

import io
import os
import sys
from typing import Optional


def mayuscula(palabra: str) -> str:
    """
    Convierte la primera letra de cada palabra a mayúscula y el resto a minúscula.
    
    Args:
        palabra: Texto a formatear
        
    Returns:
        Texto con formato título (primera letra de cada palabra en mayúscula)
        
    Example:
        >>> mayuscula("juan pérez garcía")
        'Juan Pérez García'
    """
    if not isinstance(palabra, str):
        return str(palabra)
    
    palabras = palabra.split(" ")
    palabra_formateada = " ".join([i.capitalize() for i in palabras])
    return palabra_formateada.strip()


def formato(telefono: Optional[str]) -> str:
    """
    Formatea un número de teléfono para WhatsApp (formato chileno +56).
    
    Asegura que el número tenga el formato correcto para WhatsApp Web.
    Maneja números de 8, 9 y 11 dígitos según estándares chilenos.
    
    Args:
        telefono: Número de teléfono a formatear (puede ser None, str o número)
        
    Returns:
        Número formateado con código de país (+56) o cadena vacía si es inválido
        
    Examples:
        >>> formato("912345678")  # 9 dígitos
        '+56912345678'
        >>> formato("12345678")   # 8 dígitos
        '+56912345678'
        >>> formato("56912345678")  # 11 dígitos
        '+56912345678'
        >>> formato("123")        # Muy corto
        ''
    """
    if telefono is None:
        return ""
    
    telefono_str = str(telefono).replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    # Verificar longitud mínima
    if len(telefono_str) < 8:
        return ""
    
    # Formatear según longitud
    if len(telefono_str) == 9:
        # Número móvil chileno sin código de país
        telefono_str = "+56" + telefono_str
    elif len(telefono_str) == 8:
        # Número fijo chileno sin código de país
        telefono_str = "+569" + telefono_str
    elif len(telefono_str) == 11:
        # Número con código de país sin el símbolo +
        telefono_str = "+" + telefono_str
    elif len(telefono_str) == 12 and telefono_str.startswith("+56"):
        # Ya está formateado correctamente
        pass
    else:
        # Longitud no reconocida
        return ""
    
    return telefono_str


def ensure_utf8_stdout() -> None:
    """
    Asegura que la salida por consola use UTF-8 para mostrar tildes y caracteres especiales.
    
    Esta función es especialmente útil en Windows donde la consola por defecto
    puede usar una codificación que no soporta caracteres Unicode.
    
    La función falla silenciosamente si no puede reconfigurar la salida,
    para no interrumpir la ejecución del programa principal.
    """
    try:
        # Forzar modo UTF-8 en la sesión de Python si es posible
        os.environ.setdefault('PYTHONUTF8', '1')
        
        # Verificar codificación actual
        enc = getattr(sys.stdout, 'encoding', None)
        
        if not enc or enc.lower() != 'utf-8':
            # Intentar reconfigurar stdout
            try:
                sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
            except Exception:
                # Si reconfigure no está disponible, usar TextIOWrapper
                sys.stdout = io.TextIOWrapper(
                    sys.stdout.buffer, 
                    encoding='utf-8', 
                    errors='backslashreplace'
                )
            
            # Intentar reconfigurar stderr
            try:
                sys.stderr.reconfigure(encoding='utf-8', errors='backslashreplace')
            except Exception:
                # Si reconfigure no está disponible, usar TextIOWrapper
                sys.stderr = io.TextIOWrapper(
                    sys.stderr.buffer, 
                    encoding='utf-8', 
                    errors='backslashreplace'
                )
                
    except Exception:
        # Falla silenciosa: si no se puede reconfigurar, continuamos sin UTF-8
        pass