"""
Módulo de carga de configuración desde variables de entorno.

Este módulo maneja la carga de archivos .env y la resolución
de rutas para archivos Excel basándose en variables de entorno.
"""

import os
import pathlib
from typing import Sequence


def get_excel_path(
    preferred_keys: Sequence[str] = (
        "ARCHIVO_EXCEL", 
        "NOMBRE_ARCHIVO", 
        "FILE_NAME", 
        "EXCEL_PATH"
    ),
    defaults: Sequence[str] = (
        "Mensualidad.xlsx", 
        "formulario postulacion (Respuestas).xlsx"
    )
) -> str:
    """
    Obtiene la ruta al archivo Excel desde variables de entorno o valores por defecto.

    Busca en orden las claves especificadas en las variables de entorno.
    Si encuentra una, resuelve la ruta respecto al directorio raíz del proyecto.
    Si no encuentra ninguna, busca archivos por defecto existentes.

    Args:
        preferred_keys: Secuencia de nombres de variables de entorno a buscar en orden
        defaults: Secuencia de nombres de archivo por defecto a buscar en el proyecto

    Returns:
        Ruta absoluta al archivo Excel a utilizar

    Example:
        # Con variable de entorno ARCHIVO_EXCEL=datos.xlsx
        >>> get_excel_path()
        '/path/to/proyecto/datos.xlsx'
        
        # Sin variables de entorno, pero con Mensualidad.xlsx existente
        >>> get_excel_path()
        '/path/to/proyecto/Mensualidad.xlsx'

    Note:
        - Las rutas relativas se resuelven respecto al directorio padre de utils/
        - Las rutas absolutas se mantienen tal como están
        - Si ningún archivo existe, devuelve la ruta al primer archivo por defecto
    """
    # Directorio raíz del proyecto (parent de utils/)
    project_root = pathlib.Path(__file__).parent.parent

    # Buscar en variables de entorno
    for key in preferred_keys:
        value = os.getenv(key)
        if value and value.strip():
            ruta_env = value.strip()
            ruta_path = pathlib.Path(ruta_env)
            
            # Resolver rutas relativas respecto al proyecto
            if not ruta_path.is_absolute():
                return str((project_root / ruta_path).resolve())
            
            return str(ruta_path)

    # Si no hay variable de entorno, buscar archivos por defecto existentes
    for default_file in defaults:
        candidate = project_root / default_file
        if candidate.exists():
            return str(candidate.resolve())

    # Ningún archivo existe: devolver el primer default como ruta absoluta
    return str((project_root / defaults[0]).resolve())