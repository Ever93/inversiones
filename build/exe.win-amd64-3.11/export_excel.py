import sqlite3
import xlsxwriter
from tkinter import filedialog
import tkinter.messagebox as messagebox
import datetime

def exportar_excel(nombre_archivo):
    try:
        # Conectarse a la base de datos
        conn = sqlite3.connect('inversiones.db')
        cursor = conn.cursor()

        # Crear un archivo Excel
        fecha_actual = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        nombre_archivo = f'inversion_{fecha_actual}.xlsx'
        ruta_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")], initialfile=nombre_archivo)
        if ruta_guardar:
            workbook = xlsxwriter.Workbook(ruta_guardar)
            worksheet_egreso = workbook.add_worksheet("Egreso")
            worksheet_ingreso = workbook.add_worksheet("Ingreso")
            worksheet_saldo = workbook.add_worksheet("Saldo")
            worksheet_capitalinicial = workbook.add_worksheet("Capital Inicial")

            # Exportar datos de la tabla egreso
            cursor.execute("SELECT fecha, detalle, monto FROM egreso")
            egreso_data = cursor.fetchall()
            worksheet_egreso.write('A1', 'Fecha')
            worksheet_egreso.write('B1', 'Detalle')
            worksheet_egreso.write('C1', 'Monto')
            for i, (fecha, detalle, monto) in enumerate(egreso_data, start=2):
                worksheet_egreso.write(f'A{i}', fecha)
                worksheet_egreso.write(f'B{i}', detalle)
                worksheet_egreso.write(f'C{i}', monto)

            # Exportar datos de la tabla ingreso
            cursor.execute("SELECT fecha, detalle, monto FROM ingreso")
            ingreso_data = cursor.fetchall()
            worksheet_ingreso.write('A1', 'Fecha')
            worksheet_ingreso.write('B1', 'Detalle')
            worksheet_ingreso.write('C1', 'Monto')
            for i, (fecha, detalle, monto) in enumerate(ingreso_data, start=2):
                worksheet_ingreso.write(f'A{i}', fecha)
                worksheet_ingreso.write(f'B{i}', detalle)
                worksheet_ingreso.write(f'C{i}', monto)

            # Exportar datos de la tabla saldo
            cursor.execute("SELECT fecha, monto FROM saldo")
            saldo_data = cursor.fetchall()
            worksheet_saldo.write('A1', 'Fecha')
            worksheet_saldo.write('B1', 'Monto')
            for i, (fecha, monto) in enumerate(saldo_data, start=2):
                worksheet_saldo.write(f'A{i}', fecha)
                worksheet_saldo.write(f'B{i}', monto)

            # Exportar datos de la tabla capitalinicial
            cursor.execute("SELECT fecha, monto FROM capitalinicial")
            capital_data = cursor.fetchall()
            worksheet_capitalinicial.write('A1', 'Fecha')
            worksheet_capitalinicial.write('B1', 'Monto')
            for i, (fecha, monto) in enumerate(capital_data, start=2):
                worksheet_capitalinicial.write(f'A{i}', fecha)
                worksheet_capitalinicial.write(f'B{i}', monto)

            # Cerrar el archivo Excel
            workbook.close()

            messagebox.showinfo("Exportación Exitosa", f'Todos los datos se han exportado correctamente en {ruta_guardar}')
    except Exception as e:
        print(f'Ocurrió un error al exportar los datos a Excel: {e}')
    finally:
        conn.close()
