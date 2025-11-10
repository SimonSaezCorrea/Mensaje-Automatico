from utils.manejo_archivo import getData
from utils.wsp_message import enviarMensajeWhatsApp
from utils.formateo import _ensure_utf8_stdout
from dotenv import load_dotenv
'''
Recomendaciones:
    - Antes de iniciar el codigo, recuerda abrir WhatsApp Web en tu navegador predeterminado.
    - Asegúrate de que el archivo Excel esté en la misma carpeta que el script o proporciona la ruta completa.
    - Asegúrate de que el archivo Excel tenga los datos en las columnas correctas.
    - Asegúrate de que el nombre y el teléfono estén en las columnas correctas.
    - Haz pruebas de validación antes de enviar los mensajes a los numeros, haciendo test por consola o enviandolos a tu mismo número con el mensaje y su numero respectivo.
    - Haz test de tiempos de espera para que el script funcione correctamente en tu computadora.
    ----------------------------
    - NO SE DEBE UTILIZAR LA COMPUTADORA MIENTRAS SE EJECUTRA EL SCRIPT, YA QUE PUEDE INTERFERIR EN EL ENVIO DE MENSAJES Y ESTROPEARLO.
    - En caso de que estén sucediendo problemas durante el envío, puedes apretar ESQ para cerrar el chat o CTRL + W para cerrar la pestaña de WhatsApp Web, luego ir a la consola y apretar CTRL + C para detener el script.
'''


# Cargar .env usando el módulo separado env_loader.py
load_dotenv()
_ensure_utf8_stdout()

# Función principal
data = getData()

# Abre WhatsApp Web en el navegador predeterminado
# y espera a que se cargue
# Asegúrate de que WhatsApp Web esté configurado y abierto en el navegador
for celular, nombre in data:

    # Si el número de teléfono está vacío, se omite
    # y se continúa con el siguiente número
    if celular == "":
        continue

    print(f"Enviando mensaje a {nombre} ({celular})")

    #enviarMensajeWhatsApp(celular, f"")
