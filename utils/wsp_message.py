import webbrowser
import pyautogui
import time
import pyperclip

def enviarMensajeWhatsApp(celular, mensaje):
# Abre WhatsApp Web con el número de teléfono formateado
    webbrowser.open(f"https://web.whatsapp.com/send?phone={celular}")
    # Espera, en segundos, para que cargue WhatsApp Web 
    # Cambia el tiempo de espera según la velocidad de tu conexión a Internet
    time.sleep(9)
    
    # Copia el mensaje al portapapeles
    # y lo pega en el campo de texto de WhatsApp Web
    # Cambia el tiempo de espera según la velocidad de tu conexión a Internet
    pyperclip.copy(mensaje)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    
    # Presiona Enter para enviar el mensaje
    # Cambia el tiempo de espera según la velocidad de tu conexión a Internet
    pyautogui.press("enter")
    time.sleep(1)

    # Presiona Ctrl + W para cerrar la pestaña de WhatsApp Web
    # Cambia el tiempo de espera según la velocidad de tu conexión a Internet
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)