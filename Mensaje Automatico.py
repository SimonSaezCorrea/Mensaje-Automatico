"""
Mensaje Automático WhatsApp
==========================

Script principal para automatización de mensajes WhatsApp desde datos de Excel.

Este módulo lee datos de un archivo Excel configurado a través de variables de entorno,
procesa la información de contactos y pagos, y permite enviar mensajes personalizados
a través de WhatsApp Web.

Uso:
    python "Mensaje Automatico.py"

Configuración:
    Crea un archivo .env con la variable ARCHIVO_EXCEL apuntando a tu archivo Excel.

Ejemplo:
    ARCHIVO_EXCEL=Mensualidad.xlsx

Advertencias:
    - Abre WhatsApp Web antes de ejecutar
    - NO uses la computadora durante el envío de mensajes
    - Realiza pruebas con tu propio número primero
"""

import json
import logging
from typing import Dict, Any, List

from dotenv import load_dotenv

from utils.formateo import ensure_utf8_stdout
from utils.manejo_archivo import getData
from utils.wsp_message import enviarMensajeWhatsApp


def setup_logging() -> None:
    """Configura el sistema de logging para el script."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def display_data_preview(data: List[Dict[str, Any]]) -> None:
    """Muestra una vista previa de los datos leídos en formato JSON."""
    try:
        print("=== DATOS LEÍDOS ===")
        print(json.dumps(data, ensure_ascii=False, indent=2))
        print("=== FIN DATOS ===\n")
    except Exception as e:
        logging.warning("No se pudo mostrar datos como JSON: %s", e)
        print("Datos leídos:", data)


def generate_payment_message(item: Dict[str, Any]) -> str:
    """
    Genera un mensaje personalizado basado en los datos de pago del contacto.
    
    Args:
        item: Diccionario con datos del contacto incluyendo nombre, teléfono y dataPagos
        
    Returns:
        Mensaje personalizado formateado para WhatsApp
    """
    nombre = item.get('nombre', 'Usuario')
    data_pagos = item.get('dataPagos', {})
    
    cantidad_pagado = data_pagos.get('cantidadPagado', 0)
    faltantes = data_pagos.get('faltantes', 0)
    dia_a_pagar = data_pagos.get('diaAPagar', 'N/A')
    mes_a_pagar = data_pagos.get('mesAPagar', 'N/A')
    
    mensaje = (
        f"Hola {nombre},\n\n"
        f"Según nuestros registros, has realizado {cantidad_pagado} pagos. "
        f"Te quedan {faltantes} pagos pendientes. "
        f"El próximo pago vence el día {dia_a_pagar} del mes {mes_a_pagar}.\n\n"
        f"Por favor, asegúrate de completar tus pagos a tiempo para evitar inconvenientes.\n\n"
        f"¡Gracias por tu atención!"
    )
    
    return mensaje


def process_contacts(data: List[Dict[str, Any]], send_messages: bool = False) -> None:
    """
    Procesa la lista de contactos y opcionalmente envía mensajes.
    
    Args:
        data: Lista de diccionarios con información de contactos
        send_messages: Si True, envía mensajes reales por WhatsApp
    """
    logger = logging.getLogger(__name__)
    
    for i, item in enumerate(data, 1):
        nombre = item.get('nombre')
        telefono = item.get('telefono')
        
        if not telefono:
            logger.warning("Contacto %d sin teléfono válido, omitiendo", i)
            continue
            
        mensaje = generate_payment_message(item)
        
        print(f"\n=== CONTACTO {i}/{len(data)} ===")
        print(f"Destinatario: {nombre} ({telefono})")
        print(f"Mensaje:\n{mensaje}")
        print("=" * 50)
        
        if send_messages:
            try:
                logger.info("Enviando mensaje a %s (%s)", nombre, telefono)
                #enviarMensajeWhatsApp(telefono, mensaje)
            except Exception as e:
                logger.error("Error enviando mensaje a %s: %s", nombre, e)
        else:
            logger.info("Modo preview - no se envió mensaje a %s", nombre)


def main() -> None:
    """Función principal del script."""
    # Configuración inicial
    load_dotenv()
    ensure_utf8_stdout()
    setup_logging()
    
    logger = logging.getLogger(__name__)
    logger.info("Iniciando Mensaje Automático WhatsApp")
    
    # Cargar datos
    try:
        data = getData()
    except Exception as e:
        logger.error("Error cargando datos: %s", e)
        return
    
    if not data:
        logger.warning("No se encontraron datos para procesar")
        return
        
    logger.info("Se cargaron %d contactos", len(data))
    
    # Mostrar vista previa
    display_data_preview(data)
    
    # Procesar contactos (por defecto solo preview, no envía mensajes)
    # Para enviar mensajes reales, cambiar send_messages=True
    process_contacts(data, send_messages=False)
    
    logger.info("Procesamiento completado")


if __name__ == "__main__":
    main()
