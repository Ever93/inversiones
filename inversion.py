import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import estilos  # Importa el módulo de estilos que has creado
from autoscroll import AutoScroll, ScrolledTreeView, _bound_to_mousewheel, _unbound_to_mousewheel, _on_mousewheel, _on_shiftmouse
root = tk.Tk()
estilos._style_code()

class Toplevel1:
    def __init__(self, top=None):
        top.geometry("1000x600+183+56")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Inversiones")
        top.configure(background="#d9d9d9")
        self.top = top
        global _top1  # Permite el acceso a la variable global _top1
        _top1 = self 

        #####Etiquetas
        self.LabelTitle = tk.Label(self.top, text='''Control de Inversión''', background='#d9d9d9', compound='center',relief='solid', font=('Arial', 16))
        self.LabelTitle.place(relx=0.38, rely=0.017, height=28, width=307)
        #Label Capital
        self.LabelCI = tk.Label(self.top, text='''Capital:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelCI.place(relx=0.037, rely=0.162, height=38, width=87)
        #Label saldo
        self.LabelSaldo = tk.Label(self.top, text='''Saldo:''', background='#d9d9d9', compound='left', anchor='w', font=('Arial', 12))
        self.LabelSaldo.place(relx=0.067, rely=0.288, height=39, width=57)
        #Label Fecha de capital
        self.LabelFechaCI = tk.Label(self.top, text='''Fecha:''', background='#d9d9d9', compound='left', anchor='w', font=('Arial', 12))
        self.LabelFechaCI.place(relx=0.36, rely=0.167, height=38, width=57)
        #Label de fecha saldo
        self.LabelFechaSaldo = tk.Label(self.top, text='''Fecha:''', background='#d9d9d9', compound='left', anchor='w',font=('Arial', 12))
        self.LabelFechaSaldo.place(relx=0.36, rely=0.3, height=38, width=57)

        ####Botones
        self.ButtonEgreso = tk.Button(self.top, text='''Egreso''', background='#d9d9d9', compound='left', pady=0)
        self.ButtonEgreso.place(relx=0.21, rely=0.4, height=24, width=47)
        
        self.ButtonIngreso = tk.Button(self.top, text='''Ingreso''', background='#d9d9d9', compound='left', pady=0)
        self.ButtonIngreso.place(relx=0.74, rely=0.4, height=24, width=47)

        self.ButtonDeleteEgreso = tk.Button(self.top, background="#d9d9d9", compound='left', pady="0", text='''Eliminar''')
        self.ButtonDeleteEgreso.place(relx=0.44, rely=0.933, height=24, width=47)

        self.ButtonCI = tk.Button(self.top, text='Cargar', background="#d9d9d9", compound='left', pady=0)
        self.ButtonCI.place(relx=0.13, rely=0.233, height=24, width=47)
        
        self.ButtonDeleteIngreso = tk.Button(self.top, background="#d9d9d9", compound='left', pady="0", text='''Eliminar''')
        self.ButtonDeleteIngreso.place(relx=0.94, rely=0.933, height=24, width=47)
        
        self.ButtonExport = tk.Button(self.top, background="#d9d9d9", compound='left', pady="0", text='''Exportar''')
        self.ButtonExport.place(relx=0.01, rely=0.933, height=24, width=47)

        ####Cuadro de texto
        self.TextCI = tk.Text(self.top, background="white", font="TkTextFont", wrap="word")
        self.TextCI.place(relx=0.13, rely=0.167, relheight=0.057, relwidth=0.144)

        self.TextSaldo = tk.Text(self.top, background="white", font="TkTextFont", wrap="word")
        self.TextSaldo.place(relx=0.13, rely=0.3, relheight=0.057, relwidth=0.144)
        
        self.TextFechaCI = tk.Text(self.top, background="white", font="TkTextFont", wrap="word")
        self.TextFechaCI.place(relx=0.41, rely=0.167, relheight=0.057, relwidth=0.194)

        self.TextFecha = tk.Text(self.top, background="white", font="TkTextFont", wrap="word")
        self.TextFecha.place(relx=0.41, rely=0.3, relheight=0.057, relwidth=0.194)
        
        ###Treview
        # Llama a la función para configurar los estilos
        estilos._style_code()
        self.treeviewEgreso = ScrolledTreeView(self.top, columns=("Fecha", "Detalle", "Monto"), show="headings")
        self.treeviewEgreso.place(relx=0.01, rely=0.467, relheight=0.452, relwidth=0.485)
        column_configs = [("Fecha", "Fecha", 100, 50), ("Detalle", "Detalle", 200, 100), ("Monto", "Monto", 100, 50)]
        for col_name, col_text, col_width, col_minwidth in column_configs:
            self.treeviewEgreso.heading(col_name, text=col_text)
            self.treeviewEgreso.column(col_name, width=col_width, minwidth=col_minwidth, stretch=True)
        vsb = ttk.Scrollbar(self.top, orient="vertical", command=self.treeviewEgreso.yview)
        self.treeviewEgreso.configure(yscrollcommand=vsb.set)
        vsb.place(relx=0.985, rely=0.467, relheight=0.452)

        #Treview Ingreso
        self.treeviewIngreso = ScrolledTreeView(self.top, columns=("Fecha", "Detalle", "Monto"), show="headings")
        self.treeviewIngreso.place(relx=0.51, rely=0.467, relheight=0.452, relwidth=0.480)
        column_configs = [("Fecha", "Fecha", 100, 50), ("Detalle", "Detalle", 200, 100), ("Monto", "Monto", 100, 50)]
        for col_name, col_text, col_width, col_minwidth in column_configs:
            self.treeviewIngreso.heading(col_name, text=col_text)
            self.treeviewIngreso.column(col_name, width=col_width, minwidth=col_minwidth, stretch=True)        
        self.treeviewIngreso.configure(yscrollcommand=vsb.set)
        vsb.place(relx=0.945, rely=0.467, relheight=0.452)

if __name__ == '__main__':
    _top1 = Toplevel1(root)
    root.mainloop()