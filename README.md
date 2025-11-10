# Mensaje Automático WhatsApp

Automatización para el envío de mensajes personalizados de WhatsApp basados en datos de Excel.

## 🚀 Características

- Lectura automática de datos desde archivos Excel
- Formateo automático de números telefónicos (formato chileno +56)
- Carga de configuración desde archivos `.env`
- Generación de mensajes personalizados por usuario
- Soporte para datos de pagos y fechas
- Salida en formato JSON para debugging

## 📋 Prerrequisitos

- Python 3.9 o superior
- WhatsApp Web configurado en tu navegador
- Archivo Excel con los datos de contactos

## 🔧 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/SimonSaezCorrea/Mensaje-Automatico.git
cd Mensaje-Automatico
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura tu archivo `.env` (copia desde `.env.example`):
```bash
cp .env.example .env
```

4. Edita `.env` con la ruta a tu archivo Excel:
```
ARCHIVO_EXCEL=Mensualidad.xlsx
```

## 📊 Formato del Excel

El archivo Excel debe tener las siguientes columnas:
- **Columna B (2)**: Nombre del contacto
- **Columna C (3)**: Número de teléfono
- **Columna D (4)**: Estado (si contiene "Inactiva" se omite)
- **Columnas E en adelante**: Datos de pagos y fechas

## 🖥️ Uso

### Ejecución básica
```bash
python "Mensaje Automatico.py"
```

### Durante la ejecución

⚠️ **IMPORTANTE**: 
- Abre WhatsApp Web en tu navegador antes de ejecutar
- **NO uses la computadora** mientras el script esté enviando mensajes
- Si necesitas detener: presiona `Ctrl+C` en la consola

### Controles de emergencia
- `ESC`: Cerrar chat actual
- `Ctrl+W`: Cerrar pestaña de WhatsApp Web
- `Ctrl+C`: Detener completamente el script

## 🛠️ Configuración

### Variables de entorno soportadas
- `ARCHIVO_EXCEL`: Ruta al archivo Excel principal
- `NOMBRE_ARCHIVO`: Ruta alternativa al archivo
- `FILE_NAME`: Otra alternativa de ruta
- `EXCEL_PATH`: Otra alternativa de ruta

### Estructura del proyecto
```
Mensaje-Automatico/
├── Mensaje Automatico.py    # Script principal
├── utils/
│   ├── __init__.py
│   ├── env_loader.py        # Carga de configuración
│   ├── formateo.py          # Formateo de texto y números
│   ├── manejo_archivo.py    # Lectura del Excel
│   └── wsp_message.py       # Envío de mensajes
├── .env.example             # Ejemplo de configuración
├── requirements.txt         # Dependencias
└── README.md               # Este archivo
```

## 🔍 Debugging

El script imprime la información leída en formato JSON para verificar que los datos se lean correctamente:

```json
[
  {
    "nombre": "Juan Pérez",
    "telefono": "+56912345678",
    "dataPagos": {
      "cantidadPagado": 3,
      "faltantes": 2,
      "diaAPagar": "15",
      "mesAPagar": "Noviembre"
    }
  }
]
```

## ⚠️ Consideraciones de seguridad

- El archivo `.env` contiene configuración sensible y **no debe** subirse a repositorios públicos
- Realiza pruebas enviando mensajes a tu propio número antes de enviar en masa
- Ten cuidado con los tiempos de espera para evitar bloqueos de WhatsApp

## 🤝 Contribuir

1. Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🐛 Problemas conocidos

- En Windows PowerShell antiguo pueden aparecer caracteres mal codificados (el script incluye configuración UTF-8)
- WhatsApp Web puede cambiar su interfaz y afectar la automatización
- Archivos Excel muy grandes pueden tardar en procesarse

## 📞 Soporte

Si encuentras problemas:
1. Revisa que tu archivo Excel tenga el formato correcto
2. Verifica que las variables de entorno estén configuradas
3. Asegúrate de que WhatsApp Web esté funcionando manualmente
4. Abre un issue en GitHub con detalles del error
