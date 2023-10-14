import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter"],  # Asegura que las bibliotecas GUI estén incluidas
    "include_files": [
        ("movitec.ico", "movitec.ico"),  # Añade tu icono
        ("inversiones.db", "inversiones.db"),  # Añade tu base de datos u otros archivos
        ("export_excel.py", "export_excel.py"),  # Añade export_excel.py
        ("db.py", "db.py"),  # Añade db.py
    ],
    "include_msvcr": True,  # Incluye las bibliotecas de tiempo de ejecución de Microsoft
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Indica que es una aplicación GUI de Windows

executables = [Executable("main.py", base=base, icon="movitec.ico")]

setup(
    name="InversionesApp",
    version="1.0",
    description="Tu descripción",
    options={"build_exe": build_exe_options},
    executables=executables,
)
