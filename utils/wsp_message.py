"""
Módulo de envío de mensajes WhatsApp.

Este módulo contiene funciones para automatizar el envío de mensajes
a través de WhatsApp Web utilizando pyautogui y pyperclip.
"""

import logging
import time
import webbrowser
from typing import Optional

import pyautogui
import pyperclip

logger = logging.getLogger(__name__)

# Configuraciones por defecto
DEFAULT_WAIT_TIME = 9  # Tiempo de espera para cargar WhatsApp Web
DEFAULT_ACTION_DELAY = 1  # Delay entre acciones


def enviarMensajeWhatsApp(
    celular: str, 
    mensaje: str,
    wait_time: int = DEFAULT_WAIT_TIME,
    action_delay: int = DEFAULT_ACTION_DELAY,
    close_tab: bool = True
) -> bool:
    """
    Envía un mensaje a través de WhatsApp Web.
    
    Este método abre WhatsApp Web en el navegador predeterminado,
    navega al chat del contacto especificado y envía el mensaje.
    
    Args:
        celular: Número de teléfono con formato internacional (ej: +56912345678)
        mensaje: Texto del mensaje a enviar
        wait_time: Tiempo de espera en segundos para que cargue WhatsApp Web
        action_delay: Tiempo de espera entre acciones automatizadas
        close_tab: Si True, cierra la pestaña después del envío
        
    Returns:
        True si el envío fue exitoso, False en caso contrario
        
    Raises:
        Registra errores en el logger pero no lanza excepciones
        
    Advertencias:
        - WhatsApp Web debe estar configurado y activo
        - No usar la computadora durante el envío
        - Puede fallar si WhatsApp Web cambia su interfaz
        
    Example:
        >>> enviarMensajeWhatsApp("+56912345678", "Hola, este es un mensaje de prueba")
        True
    """
    try:
        logger.info("Iniciando envío de mensaje a %s", celular)
        
        # Validar inputs
        if not celular or not mensaje:
            logger.error("Número de teléfono o mensaje vacío")
            return False
        
        # Construir URL de WhatsApp Web
        url = f"https://web.whatsapp.com/send?phone={celular}"
        logger.debug("Abriendo URL: %s", url)
        
        # Abrir WhatsApp Web con el número de teléfono
        webbrowser.open(url)
        
        # Esperar a que cargue WhatsApp Web
        logger.debug("Esperando %d segundos para que cargue WhatsApp Web", wait_time)
        time.sleep(wait_time)
        
        # Copiar mensaje al portapapeles y pegarlo
        logger.debug("Copiando mensaje al portapapeles y pegando")
        pyperclip.copy(mensaje)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(action_delay)
        
        # Enviar mensaje (presionar Enter)
        logger.debug("Enviando mensaje")
        pyautogui.press("enter")
        time.sleep(action_delay)
        
        # Cerrar pestaña si está configurado
        if close_tab:
            logger.debug("Cerrando pestaña de WhatsApp Web")
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(action_delay)
        
        logger.info("Mensaje enviado exitosamente a %s", celular)
        return True
        
    except Exception as e:
        logger.error("Error enviando mensaje a %s: %s", celular, e)
        return False


def configurar_pyautogui(
    pause: float = 0.1,
    fail_safe: bool = True,
    fail_safe_corner: Optional[tuple] = None
) -> None:
    """
    Configura pyautogui con opciones de seguridad.
    
    Args:
        pause: Pausa entre acciones de pyautogui (en segundos)
        fail_safe: Si True, mover el mouse a la esquina superior izquierda cancela la automatización
        fail_safe_corner: Coordenadas específicas de la esquina de fail-safe
        
    Example:
        >>> configurar_pyautogui(pause=0.5, fail_safe=True)
    """
    pyautogui.PAUSE = pause
    pyautogui.FAILSAFE = fail_safe
    
    if fail_safe_corner:
        pyautogui.FAILSAFE_POINTS = [fail_safe_corner]
    
    logger.info("pyautogui configurado: pause=%.2f, failsafe=%s", pause, fail_safe)


# Configurar pyautogui con valores seguros por defecto
configurar_pyautogui()