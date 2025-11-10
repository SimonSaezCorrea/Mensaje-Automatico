from .env_loader import get_excel_path
from .formateo import formato, mayuscula
import openpyxl 

def getDataRow(hoja, row):
    debePagar = hoja.cell(row=row, column=4).value
    if debePagar == "Inactiva":
        return []

    nombre = hoja.cell(row=row, column=2).value
    telefono = hoja.cell(row=row, column=3).value

    if nombre is None:
        return []
    
    telefono = formato(telefono)
    nombre = mayuscula(nombre)

    if telefono == "":
        return []
    
    return [telefono, nombre]

def getData():

    # Obtener la ruta del Excel desde el módulo env_loader (usa .env o fallback)
    ruta = get_excel_path()
    print(f"Usando archivo de Excel: {ruta}")

    if ruta == "":
        print("No se ha especificado la ruta del archivo Excel.")
        return []

    # Abre el archivo Excel y carga la hoja activa
    try:
        excel = openpyxl.load_workbook(ruta)
        hoja = excel.active
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return []
    except Exception as e:
        print(f"Error al abrir el archivo Excel '{ruta}': {e}")
        return []

    lista = []

    # Si no hay suficientes filas, devolvemos lista vacía
    if hoja.max_row < 3:
        return []

    for i in range(3, hoja.max_row + 1):
        datos = getDataRow(hoja, i)
        if datos != []:
            lista.append(datos)

    return lista
