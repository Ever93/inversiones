import sqlite3
import tkinter as tk
import db
import datetime
from tkinter import *
from tkinter import messagebox, ttk
import tkinter.messagebox
from export_excel import exportar_excel

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

def create_entry_with_validation(top, validate_function):
    vcmd = (top.register(validate_function), '%P')  # %P se refiere al nuevo valor
    entry = ttk.Entry(top, validate="key", validatecommand=vcmd)
    return entry

def format_number_with_commas(number):
    try:
        # Verificar si el número es un entero o una cadena de texto
        if isinstance(number, int):
            number = str(number)
        # Convierte el número a un entero para eliminar puntos o comas
        number = int(number.replace(',', '').replace('.', ''))
        # Formatea el número con comas como separadores de miles
        formatted_number = f'{number:,}'
        return formatted_number
    except ValueError:
        # En caso de error al formatear el número, devuelve el número original
        return number

class InversionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+183+56")
        self.root.iconbitmap('movitec.ico')
        self.root.title('Inversión')
        self.create_widgets()
        self.render_monto_capital()
        self.render_monto_saldo()
        self.render_egreso()
        self.render_ingreso()
        self.calcular_suma_egresos()
        self.calcular_suma_ingresos()
        self.calcular_balance()
        self.top = None
        
    def create_widgets(self):
        #Etiquetas (#height altura y width ancho)####################################################################
        self.LabelTitle = tk.Label(self.root, text='''Control de Inversión''', background='#d9d9d9', compound='center',relief='solid', font=('Arial', 16))
        self.LabelTitle.place(relx=0.38, rely=0.017, height=28, width=307)
        
        self.LabelCI = tk.Label(self.root, text='''Capital:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelCI.place(relx=0.065, rely=0.170, height=30, width=87)
        
        self.LabelSaldo = tk.Label(self.root, text='''Saldo:''', background='#d9d9d9', compound='left', anchor='w', font=('Arial', 12))
        self.LabelSaldo.place(relx=0.067, rely=0.305, height=30, width=87)
        
        self.LabelFechaCI = tk.Label(self.root, text='''Fecha:''', background='#d9d9d9', compound='left', anchor='w', font=('Arial', 12))
        self.LabelFechaCI.place(relx=0.35, rely=0.170, height=30, width=87)
        
        self.LabelFechaSaldo = tk.Label(self.root, text='''Fecha:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelFechaSaldo.place(relx=0.35, rely=0.305, height=30, width=87)
        
        self.LabelTotalIngreso = tk.Label(self.root, text='''Ingreso:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelTotalIngreso.place(relx=0.51, rely=0.4, height=30, width=87)
        
        self.LabelTotalEgreso = tk.Label(self.root, text='''Egreso:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelTotalEgreso.place(relx=0.01, rely=0.4, height=30, width=87)
        
        self.LabelBalance = tk.Label(self.root, text='''Balance:''', background='#d9d9d9', compound='left', anchor='w', font=('Arial', 12))
        self.LabelBalance.place(relx=0.68, rely=0.170, height=30, width=87)
        
        ####Botones#############################################################################
        self.ButtonEgreso = tk.Button(self.root, text='''Egreso''', background='#d9d9d9', compound='left', pady=0, command=self.egreso_clicked)
        self.ButtonEgreso.place(relx=0.45, rely=0.4, height=24, width=47)
        
        self.ButtonIngreso = tk.Button(self.root, text='''Ingreso''', background='#d9d9d9', compound='left', pady=0, command=self.ingreso_clicked)
        self.ButtonIngreso.place(relx=0.94, rely=0.4, height=24, width=47)

        self.ButtonDeleteEgreso = tk.Button(self.root, background="#d9d9d9", compound='left', pady="0", text='''Eliminar''', command=self.eliminar_ultimo_egreso)
        self.ButtonDeleteEgreso.place(relx=0.44, rely=0.933, height=24, width=47)

        self.ButtonCI = tk.Button(self.root, text='Cargar', background="#d9d9d9", compound='left', pady=0, command=self.capital_clicked)
        self.ButtonCI.place(relx=0.13, rely=0.233, height=24, width=47)
        
        self.ButtonDeleteIngreso = tk.Button(self.root, background="#d9d9d9", compound='left', pady="0", text='''Eliminar''', command=self.eliminar_ultimo_ingreso)
        self.ButtonDeleteIngreso.place(relx=0.94, rely=0.933, height=24, width=47)
        
        self.ButtonExport = tk.Button(self.root, background="#d9d9d9", compound='left', pady="0", text='''Exportar''', command=self.exportar_excel)
        self.ButtonExport.place(relx=0.01, rely=0.933, height=24, width=47)
        
        self.ButtonContar = tk.Button(self.root, background="#d9d9d9", compound='left', pady="0", text='''Contar''', command=self.contar_clicked)
        self.ButtonContar.place(relx=0.74, rely=0.305,
                                relheight=0.050, relwidth=0.130)

        
        #Label de contenido de solo lectura##########################################
        self.LabelMonto = tk.Label(self.root, background="white", font=("TkTextFont", 12), relief="solid", borderwidth=1)
        self.LabelMonto.place(relx=0.12, rely=0.170, relheight=0.050, relwidth=0.130)
        
        self.LabelSaldo = tk.Label(self.root, background="white", font=("TkTextFont", 12), relief="solid", borderwidth=1)
        self.LabelSaldo.place(relx=0.12, rely=0.305, relheight=0.050, relwidth=0.130)
        
        self.LabelFechaCapital = tk.Label(self.root, background="white", font=("TkTextFont", 12), relief="solid", borderwidth=1)
        self.LabelFechaCapital.place(relx=0.40, rely=0.170, relheight=0.051, relwidth=0.190)

        self.LabelFechaSaldo = tk.Label(self.root, background="white", font=("TkTextFont", 12), relief="solid", borderwidth=1)
        self.LabelFechaSaldo.place(relx=0.40, rely=0.305, relheight=0.050, relwidth=0.190)
        
        self.LabelIngreso = tk.Label(self.root, background="white", font=("TkTextFont", 12), relief="solid", borderwidth=1)
        self.LabelIngreso.place(relx=0.57, rely=0.4, relheight=0.050, relwidth=0.130)
        
        self.LabelEgreso = tk.Label(self.root, background="white", font=("TkTextFont", 12), relief="solid", borderwidth=1)
        self.LabelEgreso.place(relx=0.07, rely=0.4, relheight=0.050, relwidth=0.130)
        
        self.LabelBalance = tk.Label(self.root, background="white", font=("TkTextFont", 12), relief="solid", borderwidth=1)
        self.LabelBalance.place(relx=0.74, rely=0.170, relheight=0.050, relwidth=0.130)
        
        self.LabelResultado = tk.Label(self.root, font=("TkTextFont", 10))
        self.LabelResultado.place(relx=0.87, rely=0.170, relheight=0.050, relwidth=0.060)
        
        # Crear Treeview########################################################################
        #Treeview Egreso
        self.treeviewEgreso = ttk.Treeview(self.root, columns=("Fecha", "Detalle", "Monto"), show="headings")
        self.treeviewEgreso.place(relx=0.01, rely=0.467, relheight=0.452, relwidth=0.485)
        column_configs = [("Fecha", "Fecha", 100), ("Detalle", "Detalle", 200), ("Monto", "Monto", 100)]
        for col_name, col_text, col_width in column_configs:
            self.treeviewEgreso.heading(col_name, text=col_text)
            self.treeviewEgreso.column(col_name, width=col_width, stretch=True)
        # Crear la barra de desplazamiento vertical
        treeview_scrollbar_y = ttk.Scrollbar(self.root, orient="vertical", command=self.treeviewEgreso.yview)
        treeview_scrollbar_y.place(relx=0.495, rely=0.467, relheight=0.452)
        self.treeviewEgreso.configure(yscrollcommand=treeview_scrollbar_y.set)
        self.render_egreso()
        
        #Treview Ingreso
        self.treeviewIngreso = ttk.Treeview(self.root, columns=("Fecha", "Detalle", "Monto"), show="headings")
        self.treeviewIngreso.place(relx=0.51, rely=0.467, relheight=0.452, relwidth=0.480)
        column_configs = [("Fecha", "Fecha", 100), ("Detalle", "Detalle", 200), ("Monto", "Monto", 100)]
        for col_name, col_text, col_width in column_configs:
            self.treeviewIngreso.heading(col_name, text=col_text)
            self.treeviewIngreso.column(col_name, width=col_width, stretch=True)
        # Crear la barra de desplazamiento vertical
        treeview_scrollbar_y = ttk.Scrollbar(self.root, orient="vertical", command=self.treeviewIngreso.yview)
        treeview_scrollbar_y.place(relx=0.986, rely=0.467, relheight=0.452)
        self.treeviewIngreso.configure(yscrollcommand=treeview_scrollbar_y.set)
        self.render_ingreso()
    

    def contar_clicked(self):
        top = tk.Toplevel()
        top.title('Contar Efectivo')
        top.geometry('350x350')
        # Obtiene las dimensiones de la ventana principal
        x = self.root.winfo_x() + (self.root.winfo_width() - 350) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 350) // 2
        top.geometry(f'350x350+{x}+{y}')
        top.resizable(0, 0)  # Deshabilita maximizar y minimizar
        top.grab_set()

    # L# Lógica para contar los billetes (este es un ejemplo simple)
        self.billetes = {
            100000: tk.StringVar(value=""),
            50000: tk.StringVar(value=""),
            20000: tk.StringVar(value=""),
            10000: tk.StringVar(value=""),
            5000: tk.StringVar(value=""),
            2000: tk.StringVar(value=""),
            1000: tk.StringVar(value=""),
            500: tk.StringVar(value="")
        }

        for i, (denominacion, var) in enumerate(self.billetes.items()):
            lbl_text = f'Billete de {self.format_denomination(denominacion)}:'
            lbl_billete = ttk.Label(top, text=lbl_text)
            lbl_billete.grid(row=i, column=0, padx=10, pady=5)

            entry_billete = ttk.Entry(top, textvariable=var)
            entry_billete.grid(row=i, column=1, padx=10, pady=5)

            if i == 0:
                entry_billete.focus()

            # Configurar el rastreo ('write') directamente en el StringVar
            var.trace_add('write', lambda *args,
                          var=var: self.calcular_total())

        limpiar_button = ttk.Button(
            top, text="Limpiar", command=self.limpiar_campos)
        limpiar_button.grid(row=len(self.billetes), column=1, padx=10, pady=5)

        self.total_label = ttk.Label(top, text="Total: $0", font=("Arial", 14))
        self.total_label.grid(row=len(self.billetes)+1, columnspan=2, padx=20, pady=5)

    def calcular_total(self, *args):
        total = sum(denominacion * (int(var.get()) if var.get().isdigit() else 0)
                    for denominacion, var in self.billetes.items())
        total_formateado = "{:,.0f}".format(total).replace(",", ".")
        self.total_label.config(text=f"Total: {total_formateado} Gs.")

    def limpiar_campos(self):
        for var in self.billetes.values():
            var.set("")
        self.total_label.config(text="Total: $0")

    def format_denomination(self, value):
        if isinstance(value, int):
            return f"{value:,.0f}".replace(",", ".")
        else:
            return value  # Devuelve la cadena sin modificar si no es un número

    def capital_clicked(self):
        top = tk.Toplevel()
        top.title('Cargar Capital')
        top.geometry('250x100')
        # Obtiene las dimensiones de la ventana principal
        x = self.root.winfo_x() + (self.root.winfo_width() - 250) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 100) // 2
        top.geometry(f'250x100+{x}+{y}')
        top.resizable(0, 0)  # Deshabilita maximizar y minimizar
        top.grab_set()
        lbl_monto = tk.Label(top, text='Monto:')
        lbl_monto.pack()
        entry_monto = create_entry_with_validation(top, validate_monto)
        entry_monto.pack()
        entry_monto.focus_set()  # Establecer el foco en el campo de entrada
        # Configura un controlador de evento para detectar cambios en el campo de entrada
        entry_monto.bind("<KeyRelease>", lambda event, entry_monto=entry_monto: on_monto_change(event, entry_monto))

        def on_ok():
            self.guardar_capital(entry_monto.get())
            top.grab_release()  # Libera la ventana principal
            top.destroy()  # Cerrar la ventana modal
            
        def handle_enter(event):
            on_ok()
        # Configura la tecla Enter para llamar a handle_enter
        top.bind('<Return>', handle_enter)
        btn_ok = tk.Button(top, text='Ok', command=on_ok)
        btn_ok.pack()
        top.mainloop()
        
    def guardar_capital(self, monto):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn, c = db.conectar()
        try:
            # Convierte el monto a un número entero eliminando comas y puntos
            monto = int(monto.replace(',', '').replace('.', ''))
            c.execute("SELECT * FROM capitalinicial WHERE id = 1")
            existing_record = c.fetchone()
            if existing_record:
                c.execute("UPDATE capitalinicial SET monto = ?, fecha = ? WHERE id = 1", (monto, fecha_actual))
            else:
                c.execute("INSERT INTO capitalinicial (id, fecha, monto) VALUES (1, ?, ?)", (fecha_actual, monto))
            # Comprobar si ya existe un registro en la tabla saldo
            c.execute("SELECT * FROM saldo WHERE id = 1")
            existing_record_saldo = c.fetchone()
            if existing_record_saldo:
            # Si el registro ya existe, actualiza el monto y la fecha
                c.execute("UPDATE saldo SET monto = ?, fecha = ? WHERE id = 1", (monto, fecha_actual))
            else:
            # Si el registro no existe, crea uno nuevo
                c.execute("INSERT INTO saldo (id, fecha, monto) VALUES (1, ?, ?)", (fecha_actual, monto))
            conn.commit()
            self.render_monto_capital()
            self.render_monto_saldo()
            
        except sqlite3.Error as e:
            print("Error al guardar en la base de datos:", e)
        finally:
        # Cerrar la conexión a la base de datos
            conn.close()
        messagebox.showinfo("Éxito", "Datos agregados correctamente")

    def egreso_clicked(self):
        top = tk.Toplevel()
        top.title('Cargar Egreso')
        top.geometry('400x200')
        # Obtiene las dimensiones de la ventana principal
        x = self.root.winfo_x() + (self.root.winfo_width() - 400) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 200) // 2
        top.geometry(f'400x200+{x}+{y}')
        top.resizable(0, 0)  # Deshabilita maximizar y minimizar
        top.grab_set()
        lbl_monto = tk.Label(top, text='Monto:')
        lbl_monto.grid(row=1, column=0, padx=5, pady=5)
        entry_monto = create_entry_with_validation(top, validate_monto)
        entry_monto.grid(row=1, column=1, padx=5, pady=5)
        entry_monto.focus_set()  # Establecer el foco en el campo de entrada
        # Configura un controlador de evento para detectar cambios en el campo de entrada
        entry_monto.bind("<KeyRelease>", lambda event, entry_monto=entry_monto: on_monto_change(event, entry_monto))
        lbl_detalle = tk.Label(top, text='Detalle:')
        lbl_detalle.grid(row=2, column=0, padx=5, pady=5)
        entry_detalle = tk.Text(top, wrap=tk.WORD, width=40, height=4)
        entry_detalle.grid(row=2, column=1, padx=5, pady=5)
        
        def on_ok():
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            detalle = entry_detalle.get("1.0", "end-1c")  # Obtener el detalle del cuadro de texto
            monto = entry_monto.get()  # Obtener el monto ingresado
            self.guardar_egreso(fecha_actual, detalle, monto)
            top.grab_release()  # Libera la ventana principal
            top.destroy()  # Cierra la ventana modal
            
        def handle_enter(event):
            on_ok()
        # Configura la tecla Enter para llamar a handle_enter
        top.bind('<Return>', handle_enter)
        btn_ok = tk.Button(top, text='Ok', command=on_ok)
        btn_ok.grid(row=3, column=1, padx=5, pady=5)
        top.mainloop()
    
    def guardar_egreso(self, fecha, detalle, monto):
        conn, c = db.conectar()
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            # Convierte el monto a un número entero eliminando comas y puntos
            monto = int(monto.replace(',', '').replace('.', ''))
            c.execute("INSERT INTO egreso (fecha, detalle, monto) VALUES (?, ?, ?)", (fecha or fecha_actual, detalle, monto))
            conn.commit()
            # Restar el monto del egreso del saldo actual
            c.execute("SELECT monto FROM saldo WHERE id = 1")
            saldo_actual = c.fetchone()[0]
            nuevo_saldo = saldo_actual - monto
        # Actualizar el saldo en la base de datos
            c.execute("UPDATE saldo SET fecha = ?, monto = ? WHERE id = 1", (fecha_actual, nuevo_saldo))
            conn.commit()
            self.render_egreso()  # Actualiza la vista de Treeview con los nuevos datos
            self.render_monto_saldo()
            self.calcular_suma_egresos()
            
        except sqlite3.Error as e:
            print("Error al guardar en la base de datos:", e)
        finally:
            conn.close()
            messagebox.showinfo("Éxito", "Egreso agregado correctamente")

    def eliminar_ultimo_egreso(self):
        conn, c = db.conectar()
        try:
        # Obtener el último registro de egreso
            c.execute("SELECT id, monto FROM egreso ORDER BY id DESC LIMIT 1")
            ultimo_egreso = c.fetchone()
            if ultimo_egreso:
                egreso_id, egreso_monto = ultimo_egreso
                # Mostrar un cuadro de diálogo de confirmación
                respuesta = tkinter.messagebox.askquestion("Eliminar Egreso", f"¿Seguro que desea eliminar el último egreso de {egreso_monto}?", icon='warning')
                if respuesta == 'yes':
            # Eliminar el último registro de egreso
                    c.execute("DELETE FROM egreso WHERE id = ?", (egreso_id,))
                    conn.commit()
            # Obtener el saldo actual
                    c.execute("SELECT monto FROM saldo WHERE id = 1")
                    saldo_actual = c.fetchone()[0]
            # Actualizar el saldo sumando el monto del egreso eliminado
                    nuevo_saldo = saldo_actual + egreso_monto
                    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    c.execute("UPDATE saldo SET fecha = ?, monto = ? WHERE id = 1", (fecha_actual, nuevo_saldo))
                    conn.commit()
                    self.render_egreso()  # Actualizar la vista de Treeview con los nuevos datos
                    self.render_monto_saldo()
                    self.calcular_suma_egresos()
                    
        except sqlite3.Error as e:
            print("Error al eliminar el egreso:", e)
        finally:
            conn.close()

    def ingreso_clicked(self):
        top = tk.Toplevel()
        top.title('Cargar Ingreso')
        top.geometry('400x200')
        # Obtiene las dimensiones de la ventana principal
        x = self.root.winfo_x() + (self.root.winfo_width() - 400) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 200) // 2
        top.geometry(f'400x200+{x}+{y}')
        top.resizable(0, 0)  # Deshabilita maximizar y minimizar
        top.grab_set()
        lbl_monto = tk.Label(top, text='Monto:')
        lbl_monto.grid(row=1, column=0, padx=5, pady=5)
        entry_monto = create_entry_with_validation(top, validate_monto)
        entry_monto.grid(row=1, column=1, padx=5, pady=5)
        entry_monto.focus_set()  # Establecer el foco en el campo de entrada
        # Configura un controlador de evento para detectar cambios en el campo de entrada
        entry_monto.bind("<KeyRelease>", lambda event, entry_monto=entry_monto: on_monto_change(event, entry_monto))
        lbl_detalle = tk.Label(top, text='Detalle:')
        lbl_detalle.grid(row=2, column=0, padx=5, pady=5)
        entry_detalle = tk.Text(top, wrap=tk.WORD, width=40, height=4)
        entry_detalle.grid(row=2, column=1, padx=5, pady=5)
        
        def on_ok():
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            detalle = entry_detalle.get("1.0", "end-1c")  # Obtener el detalle del cuadro de texto
            monto = entry_monto.get()  # Obtener el monto ingresado
            self.guardar_ingreso(fecha_actual, detalle, monto)
            top.grab_release()  # Libera la ventana principal
            top.destroy()  # Cierra la ventana modal
            
        def handle_enter(event):
            on_ok()
        # Configura la tecla Enter para llamar a handle_enter
        top.bind('<Return>', handle_enter)
        btn_ok = tk.Button(top, text='Ok', command=on_ok)
        btn_ok.grid(row=3, column=1, padx=5, pady=5)
        top.mainloop()

    def guardar_ingreso(self, fecha, detalle, monto):
        conn, c = db.conectar()
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            # Convierte el monto a un número entero eliminando comas y puntos
            monto = int(monto.replace(',', '').replace('.', ''))
            c.execute("INSERT INTO ingreso (fecha, detalle, monto) VALUES (?, ?, ?)", (fecha or fecha_actual, detalle, monto))
            conn.commit()
            # sumar el monto de ingreso
            c.execute("SELECT monto FROM saldo WHERE id = 1")
            saldo_actual = c.fetchone()[0]
            nuevo_saldo = saldo_actual + monto
        # Actualizar el saldo en la base de datos
            c.execute("UPDATE saldo SET fecha = ?, monto = ? WHERE id = 1", (fecha_actual, nuevo_saldo))
            conn.commit()
            self.render_ingreso()  # Actualiza la vista de Treeview con los nuevos datos
            self.render_monto_saldo()
            self.calcular_suma_ingresos()
            
        except sqlite3.Error as e:
            print("Error al guardar en la base de datos:", e)
        finally:
            conn.close()
            messagebox.showinfo("Éxito", "Egreso agregado correctamente")
    
    def eliminar_ultimo_ingreso(self):
        conn, c = db.conectar()
        try:
        # Obtener el último registro de egreso
            c.execute("SELECT id, monto FROM ingreso ORDER BY id DESC LIMIT 1")
            ultimo_ingreso = c.fetchone()
            if ultimo_ingreso:
                ingreso_id, ingreso_monto = ultimo_ingreso
                # Mostrar un cuadro de diálogo de confirmación
                respuesta = tkinter.messagebox.askquestion("Eliminar Ingreso", f"¿Seguro que desea eliminar el último ingreso de {ingreso_monto}?", icon='warning')
                if respuesta == 'yes':
            # Eliminar el último registro de egreso
                    c.execute("DELETE FROM ingreso WHERE id = ?", (ingreso_id,))
                    conn.commit()
            # Obtener el saldo actual
                    c.execute("SELECT monto FROM saldo WHERE id = 1")
                    saldo_actual = c.fetchone()[0]
            # Actualizar el saldo sumando el monto del egreso eliminado
                    nuevo_saldo = saldo_actual - ingreso_monto
                    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    c.execute("UPDATE saldo SET fecha = ?, monto = ? WHERE id = 1", (fecha_actual, nuevo_saldo))
                    conn.commit()
                    self.render_ingreso()  # Actualizar la vista de Treeview con los nuevos datos
                    self.render_monto_saldo()
                    self.calcular_suma_ingresos()
                    self.calcular_balance()
                    
        except sqlite3.Error as e:
            print("Error al eliminar el ingreso:", e)
        finally:
            conn.close()
            
    def render_monto_capital(self):
    # Obtener el monto directamente del registro con id=1
        conn, c = db.conectar()
        c.execute("SELECT fecha, monto FROM capitalinicial WHERE id = 1")
        data= c.fetchone()
        conn.close()
        if data:
            fecha, monto = data
            formatted_date = datetime.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")
            formatted_monto = format_number_with_commas(monto)# Formatea el monto con separadores de miles
            self.LabelMonto.config(text=formatted_monto)
            self.LabelFechaCapital.config(text=formatted_date)
        else:
            self.LabelMonto.config(text='No disponible')  # En caso de que no haya datos en la tabla
            self.LabelFechaCapital.config(text='')
            
    def render_monto_saldo(self):
        conn, c = db.conectar()
        c.execute("SELECT fecha, monto FROM saldo WHERE id = 1")
        data= c.fetchone()
        conn.close()
        if data:
            fecha, monto = data
            formatted_date = datetime.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")
            formatted_monto = format_number_with_commas(monto)# Formatea el monto con separadores de miles
            self.LabelSaldo.config(text=formatted_monto)
            self.LabelFechaSaldo.config(text=formatted_date)
        else:
            self.LabelSaldo.config(text='No disponible')  # En caso de que no haya datos en la tabla
            self.LabelFechaSaldo.config(text='')
            
    def render_egreso(self):
        conn, c = db.conectar()
        rows = c.execute("SELECT * FROM egreso").fetchall()
        conn.close()
        self.treeviewEgreso.delete(*self.treeviewEgreso.get_children())
        for row in rows:
            # Formatear el monto antes de agregarlo al Treeview
            formatted_monto = format_number_with_commas(row[3])
            self.treeviewEgreso.insert('', END, row[0], values=(row[1], row[2], formatted_monto))

    def render_ingreso(self):
        conn, c = db.conectar()
        rows = c.execute("SELECT * FROM ingreso").fetchall()
        conn.close()
        self.treeviewIngreso.delete(*self.treeviewIngreso.get_children())
        for row in rows:
            # Formatear el monto antes de agregarlo al Treeview
            formatted_monto = format_number_with_commas(row[3])
            self.treeviewIngreso.insert('', END, row[0], values=(row[1], row[2], formatted_monto))

    def exportar_excel(self):
        nombre_archivo = 'datos_inversiones.xlsx'
        exportar_excel(nombre_archivo)

    def calcular_suma_egresos(self):
        conn, c = db.conectar()
        c.execute("SELECT monto FROM egreso")
        montos = c.fetchall()
        conn.close()
        total_egresos = sum(monto[0] for monto in montos)
        formatted_total_egresos = format_number_with_commas(total_egresos)
        self.LabelEgreso.config(text=formatted_total_egresos)
        self.calcular_balance()
    
    def calcular_suma_ingresos(self):
        conn, c = db.conectar()
        c.execute("SELECT monto FROM ingreso")
        montos = c.fetchall()
        conn.close()
        total_ingresos = sum(monto[0] for monto in montos)
        formatted_total_ingresos = format_number_with_commas(total_ingresos)
        self.LabelIngreso.config(text=formatted_total_ingresos)
        self.calcular_balance()

    def calcular_balance(self):
        conn, c = db.conectar()
        c.execute("SELECT monto FROM ingreso")
        ingresos = c.fetchall()
        conn.close()
        total_ingresos = sum(ingreso[0] for ingreso in ingresos)
        conn, c = db.conectar()
        c.execute("SELECT monto FROM egreso")
        egresos = c.fetchall()
        conn.close()
        total_egresos = sum(egreso[0] for egreso in egresos)
        # Calcular el balance restando los egresos de los ingresos
        balance = total_ingresos - total_egresos
        formatted_balance = format_number_with_commas(balance)
        self.LabelBalance.config(text=formatted_balance)
        # Mostrar el mensaje correspondiente
        if balance < 0:
            self.LabelResultado.config(text="Perdida")
        elif balance > 0:
            self.LabelResultado.config(text="Ganancia")
        else:
            self.LabelResultado.config(text="")
        
root = Tk()
app = InversionApp(root)
root.mainloop()