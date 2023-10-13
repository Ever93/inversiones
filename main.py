import sqlite3
import tkinter as tk
import db
import datetime
from tkinter import *
from tkinter import messagebox, ttk, filedialog

def obtener_capital_inicial():
    conn, c = conectar()
    c.execute("SELECT fecha, monto FROM capitalinicial")
    datos = c.fetchall()
    conn.close()
    return datos

class InversionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600+183+56")
        self.root.title('Inversión')
        self.create_widgets()
        self.render_monto_capital()
        self.render_monto_saldo()
        self.render_egreso()
        self.render_ingreso()
        self.top = None
        
    def create_widgets(self):
        #Etiquetas
        self.LabelTitle = tk.Label(self.root, text='''Control de Inversión''', background='#d9d9d9', compound='center',relief='solid', font=('Arial', 16))
        self.LabelTitle.place(relx=0.38, rely=0.017, height=28, width=307)
        
        self.LabelCI = tk.Label(self.root, text='''Capital:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelCI.place(relx=0.037, rely=0.162, height=38, width=87)
        
        self.LabelSaldo = tk.Label(self.root, text='''Saldo:''', background='#d9d9d9', compound='left', anchor='w', font=('Arial', 12))
        self.LabelSaldo.place(relx=0.067, rely=0.288, height=39, width=57)
        
        self.LabelFechaCI = tk.Label(self.root, text='''Fecha:''', background='#d9d9d9', compound='left', anchor='w', font=('Arial', 12))
        self.LabelFechaCI.place(relx=0.36, rely=0.167, height=38, width=57)
        
        self.LabelFechaSaldo = tk.Label(self.root, text='''Fecha:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelFechaSaldo.place(relx=0.36, rely=0.3, height=38, width=57)
        
        ####Botones
        self.ButtonEgreso = tk.Button(self.root, text='''Egreso''', background='#d9d9d9', compound='left', pady=0)
        self.ButtonEgreso.place(relx=0.21, rely=0.4, height=24, width=47)
        
        self.ButtonIngreso = tk.Button(self.root, text='''Ingreso''', background='#d9d9d9', compound='left', pady=0)
        self.ButtonIngreso.place(relx=0.74, rely=0.4, height=24, width=47)

        self.ButtonDeleteEgreso = tk.Button(self.root, background="#d9d9d9", compound='left', pady="0", text='''Eliminar''')
        self.ButtonDeleteEgreso.place(relx=0.44, rely=0.933, height=24, width=47)

        self.ButtonCI = tk.Button(self.root, text='Cargar', background="#d9d9d9", compound='left', pady=0, command=self.capital_clicked)
        self.ButtonCI.place(relx=0.13, rely=0.233, height=24, width=47)
        
        self.ButtonDeleteIngreso = tk.Button(self.root, background="#d9d9d9", compound='left', pady="0", text='''Eliminar''')
        self.ButtonDeleteIngreso.place(relx=0.94, rely=0.933, height=24, width=47)
        
        self.ButtonExport = tk.Button(self.root, background="#d9d9d9", compound='left', pady="0", text='''Exportar''')
        self.ButtonExport.place(relx=0.01, rely=0.933, height=24, width=47)
        
        #Label de contenido de solo lectura
        self.LabelMonto = tk.Label(self.root, text='15.000.000', background="white", font="TkTextFont", relief="solid")
        self.LabelMonto.place(relx=0.13, rely=0.167, relheight=0.057, relwidth=0.144)
        
        self.LabelSaldo = tk.Label(self.root, text='15.000.000', background="white", font="TkTextFont", relief="solid")
        self.LabelSaldo.place(relx=0.13, rely=0.3, relheight=0.057, relwidth=0.144)
        
        self.LabelFechaCapital = tk.Label(self.root, text='13-10-2023', background="white", font="TkTextFont", relief="solid")
        self.LabelFechaCapital.place(relx=0.41, rely=0.167, relheight=0.057, relwidth=0.194)

        self.LabelFechaSaldo = tk.Label(self.root, text='13-10-2023', background="white", font="TkTextFont", relief="solid")
        self.LabelFechaSaldo.place(relx=0.41, rely=0.3, relheight=0.057, relwidth=0.194)
        
        # Crear el Treeview
        #Treeview Egreso
        self.treeviewEgreso = ttk.Treeview(self.root, columns=("Fecha", "Detalle", "Monto"), show="headings")
        self.treeviewEgreso.place(relx=0.01, rely=0.467, relheight=0.452, relwidth=0.485)

        column_configs = [("Fecha", "Fecha", 100), ("Detalle", "Detalle", 200), ("Monto", "Monto", 100)]
        for col_name, col_text, col_width in column_configs:
            self.treeviewEgreso.heading(col_name, text=col_text)
            self.treeviewEgreso.column(col_name, width=col_width, stretch=True)
        self.render_egreso()
        #Treview Ingreso
        self.treeviewIngreso = ttk.Treeview(self.root, columns=("Fecha", "Detalle", "Monto"), show="headings")
        self.treeviewIngreso.place(relx=0.51, rely=0.467, relheight=0.452, relwidth=0.480)

        column_configs = [("Fecha", "Fecha", 100), ("Detalle", "Detalle", 200), ("Monto", "Monto", 100)]
        for col_name, col_text, col_width in column_configs:
            self.treeviewIngreso.heading(col_name, text=col_text)
            self.treeviewIngreso.column(col_name, width=col_width, stretch=True)
        self.render_ingreso()
        
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
        entry_monto = tk.Entry(top)
        entry_monto.pack()
        entry_monto.focus_set()  # Establecer el foco en el campo de entrada
        def on_ok():
            self.guardar_capital(entry_monto.get())
            top.destroy()  # Cerrar la ventana modal

        btn_ok = tk.Button(top, text='Ok', command=on_ok)
        btn_ok.pack()
        top.mainloop()
        
    def guardar_capital(self, monto):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn, c = db.conectar()
        
        try:
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
        
        
    def render_monto_capital(self):
    # Obtener el monto directamente del registro con id=1
        conn, c = db.conectar()
        c.execute("SELECT fecha, monto FROM capitalinicial WHERE id = 1")
        data= c.fetchone()
        conn.close()
    
        if data:
            fecha, monto = data
            formatted_date = datetime.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")
            self.LabelMonto.config(text=str(monto))
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
            self.LabelSaldo.config(text=str(monto))
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
            self.treeviewEgreso.insert('', END, row[0], values=(row[1], row[2], row[3]))

    def render_ingreso(self):
        conn, c = db.conectar()
        rows = c.execute("SELECT * FROM ingreso").fetchall()
        conn.close()
        self.treeviewIngreso.delete(*self.treeviewIngreso.get_children())
        for row in rows:
            self.treeviewIngreso.insert('', END, row[0], values=(row[1], row[2], row[3]))

    
root = Tk()
app = InversionApp(root)
root.mainloop()