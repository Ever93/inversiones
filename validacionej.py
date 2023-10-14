import sqlite3
import tkinter as tk
import db
import datetime
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import tkinter.messagebox
import sys
import decimal
from export_excel import exportar_excel
import locale

# Funciones de validación y formato de números
def format_number(number):
    try:
        # Convierte el número a un entero para eliminar puntos o comas
        number = int(number.replace(',', '').replace('.', ''))
        # Formatea el número con comas como separadores de miles
        formatted_number = f'{number:,}'
        return formatted_number
    except ValueError:
        # En caso de error al formatear el número, devuelve el número original
        return number

def validate_monto(new_value):
    # Verificar si la entrada es un número o está vacía
    if new_value == "":
        return True
    # Elimina comas y puntos antes de verificar si la cadena consiste en dígitos
    cleaned_value = new_value.replace(',', '').replace('.', '', 1)
    if cleaned_value.isdigit():
        return True
    return False


def on_monto_change(event, entry_monto):
    # Obtiene el valor actual del campo de entrada
    current_value = entry_monto.get()
    # Eliminar cualquier separador de miles
    current_value = current_value.replace(',', '').replace('.', '')
    # Verificar si el valor actual es numérico
    if current_value.isdigit():
        # Aplicar el formato al valor actual
        formatted_value = f'{int(current_value):,}'
        # Actualiza el campo de entrada con el valor formateado
        entry_monto.delete(0, tk.END)
        entry_monto.insert(0, formatted_value)


# Función para crear un campo de entrada con validación
def create_entry_with_validation(top, validate_function):
    vcmd = (top.register(validate_function), '%P')  # %P se refiere al nuevo valor
    entry = ttk.Entry(top, validate="key", validatecommand=vcmd)
    return entry

def capital_clicked(self):
        top = tk.Toplevel()
        top.title('Cargar Capital')
        top.geometry('250x100')
        # Obtiene las dimensiones de la ventana principal
        x = self.root.winfo_x() + (self.root.winfo_width() - 250) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 100) // 2
        top.geometry(f'250x100+{x}+{y}')

        lbl_monto = tk.Label(top, text='Monto:')
        lbl_monto.pack()
        
        entry_monto = create_entry_with_validation(top, validate_monto)
        entry_monto.pack()
        entry_monto.focus_set()  # Establecer el foco en el campo de entrada
        # Configura un controlador de evento para detectar cambios en el campo de entrada
        entry_monto.bind("<KeyRelease>", lambda event, entry_monto=entry_monto: on_monto_change(event, entry_monto))
