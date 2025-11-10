import os


def get_excel_path():
    ruta_excel = os.getenv("EXCEL_PATH", "").strip()
    return ruta_excel