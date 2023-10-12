import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import inversion_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Treeview',  font="TkDefaultFont")
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        top.geometry("1000x600+183+56")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Inversiones")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.LabelTitle = tk.Label(self.top)
        self.LabelTitle.place(relx=0.38, rely=0.017, height=28, width=307)
        self.LabelTitle.configure(activebackground="#f9f9f9")
        self.LabelTitle.configure(background="#d9d9d9")
        self.LabelTitle.configure(compound='center')
        self.LabelTitle.configure(disabledforeground="#a3a3a3")
        self.LabelTitle.configure(foreground="#000000")
        self.LabelTitle.configure(highlightbackground="#d9d9d9")
        self.LabelTitle.configure(highlightcolor="black")
        self.LabelTitle.configure(relief="solid")
        self.LabelTitle.configure(text='''Control de Inversion''')
        # Configura el tamaño de la fuente
        font = ('Arial', 16)  # Puedes ajustar el tamaño (16) según tus preferencias
        self.LabelTitle.configure(font=font)
        self.LabelCI = tk.Label(self.top)
        self.LabelCI.place(relx=0.037, rely=0.162, height=38, width=87)
        self.LabelCI.configure(activebackground="#f9f9f9")
        self.LabelCI.configure(anchor='w')
        self.LabelCI.configure(background="#d9d9d9")
        self.LabelCI.configure(compound='left')
        self.LabelCI.configure(disabledforeground="#a3a3a3")
        self.LabelCI.configure(foreground="#000000")
        self.LabelCI.configure(highlightbackground="#d9d9d9")
        self.LabelCI.configure(highlightcolor="black")
        self.LabelCI.configure(text='''Capital Inicial:''')
        self.LabelSaldo = tk.Label(self.top)
        self.LabelSaldo.place(relx=0.067, rely=0.288, height=39, width=57)
        self.LabelSaldo.configure(activebackground="#f9f9f9")
        self.LabelSaldo.configure(anchor='w')
        self.LabelSaldo.configure(background="#d9d9d9")
        self.LabelSaldo.configure(compound='left')
        self.LabelSaldo.configure(disabledforeground="#a3a3a3")
        self.LabelSaldo.configure(foreground="#000000")
        self.LabelSaldo.configure(highlightbackground="#d9d9d9")
        self.LabelSaldo.configure(highlightcolor="black")
        self.LabelSaldo.configure(text='''Saldo:''')
        self.LabelFechaCI = tk.Label(self.top)
        self.LabelFechaCI.place(relx=0.36, rely=0.167, height=38, width=57)
        self.LabelFechaCI.configure(activebackground="#f9f9f9")
        self.LabelFechaCI.configure(anchor='w')
        self.LabelFechaCI.configure(background="#d9d9d9")
        self.LabelFechaCI.configure(compound='left')
        self.LabelFechaCI.configure(disabledforeground="#a3a3a3")
        self.LabelFechaCI.configure(foreground="#000000")
        self.LabelFechaCI.configure(highlightbackground="#d9d9d9")
        self.LabelFechaCI.configure(highlightcolor="black")
        self.LabelFechaCI.configure(text='''Fecha:''')
        self.LabelFechaSaldo = tk.Label(self.top)
        self.LabelFechaSaldo.place(relx=0.36, rely=0.3, height=38, width=57)
        self.LabelFechaSaldo.configure(activebackground="#f9f9f9")
        self.LabelFechaSaldo.configure(anchor='w')
        self.LabelFechaSaldo.configure(background="#d9d9d9")
        self.LabelFechaSaldo.configure(compound='left')
        self.LabelFechaSaldo.configure(disabledforeground="#a3a3a3")
        self.LabelFechaSaldo.configure(foreground="#000000")
        self.LabelFechaSaldo.configure(highlightbackground="#d9d9d9")
        self.LabelFechaSaldo.configure(highlightcolor="black")
        self.LabelFechaSaldo.configure(text='''Fecha:''')
        self.ButtonEgreso = tk.Button(self.top)
        self.ButtonEgreso.place(relx=0.21, rely=0.4, height=24, width=47)
        self.ButtonEgreso.configure(activebackground="beige")
        self.ButtonEgreso.configure(activeforeground="black")
        self.ButtonEgreso.configure(background="#d9d9d9")
        self.ButtonEgreso.configure(compound='left')
        self.ButtonEgreso.configure(disabledforeground="#a3a3a3")
        self.ButtonEgreso.configure(foreground="#000000")
        self.ButtonEgreso.configure(highlightbackground="#d9d9d9")
        self.ButtonEgreso.configure(highlightcolor="black")
        self.ButtonEgreso.configure(pady="0")
        self.ButtonEgreso.configure(text='''Egreso''')
        self.ButtonIngreso = tk.Button(self.top)
        self.ButtonIngreso.place(relx=0.74, rely=0.4, height=24, width=47)
        self.ButtonIngreso.configure(activebackground="beige")
        self.ButtonIngreso.configure(activeforeground="black")
        self.ButtonIngreso.configure(background="#d9d9d9")
        self.ButtonIngreso.configure(compound='left')
        self.ButtonIngreso.configure(disabledforeground="#a3a3a3")
        self.ButtonIngreso.configure(foreground="#000000")
        self.ButtonIngreso.configure(highlightbackground="#d9d9d9")
        self.ButtonIngreso.configure(highlightcolor="black")
        self.ButtonIngreso.configure(pady="0")
        self.ButtonIngreso.configure(text='''Ingreso''')
        _style_code()
        self.treeviewEgreso = ScrolledTreeView(self.top)
        self.treeviewEgreso.place(relx=0.01, rely=0.467, relheight=0.452, relwidth=0.485)
        self.treeviewEgreso.configure(columns=("Fecha", "Detalle", "Monto"), show="headings")
# Configura los encabezados de columna
        self.treeviewEgreso.heading("Fecha", text="Fecha")
        self.treeviewEgreso.heading("Detalle", text="Detalle")
        self.treeviewEgreso.heading("Monto", text="Monto")
# Configura las columnas y su ancho
        self.treeviewEgreso.column("Fecha", width=100)  # Ancho de la columna "Fecha"
        self.treeviewEgreso.column("Detalle", width=200)  # Ancho de la columna "Detalle"
        self.treeviewEgreso.column("Monto", width=100)  # Ancho de la columna "Monto"
# Ajusta el ancho mínimo y estiramiento de las columnas según sea necesario
        self.treeviewEgreso.column("Fecha", minwidth=50)
        self.treeviewEgreso.column("Fecha", stretch=True)
        self.treeviewEgreso.column("Detalle", minwidth=100)
        self.treeviewEgreso.column("Detalle", stretch=True)
        self.treeviewEgreso.column("Monto", minwidth=50)
        self.treeviewEgreso.column("Monto", stretch=True)
        # Configura la barra de desplazamiento vertical en el lado derecho
        vsb = ttk.Scrollbar(self.top, orient="vertical", command=self.treeviewEgreso.yview)
        self.treeviewEgreso.configure(yscrollcommand=vsb.set)
        vsb.place(relx=0.985, rely=0.467, relheight=0.452)
        
        self.treeviewIngreso = ScrolledTreeView(self.top)
        self.treeviewIngreso.place(relx=0.51, rely=0.467, relheight=0.452, relwidth=0.480)
        self.treeviewIngreso.configure(columns=("Fecha", "Detalle", "Monto"), show="headings")

# Configura los encabezados de columna
        self.treeviewIngreso.heading("Fecha", text="Fecha")
        self.treeviewIngreso.heading("Detalle", text="Detalle")
        self.treeviewIngreso.heading("Monto", text="Monto")

# Configura las columnas y su ancho
        self.treeviewIngreso.column("Fecha", width=100)  # Ancho de la columna "Fecha"
        self.treeviewIngreso.column("Detalle", width=200)  # Ancho de la columna "Detalle"
        self.treeviewIngreso.column("Monto", width=100)  # Ancho de la columna "Monto"

# Ajusta el ancho mínimo y estiramiento de las columnas según sea necesario
        self.treeviewIngreso.column("Fecha", minwidth=50)
        self.treeviewIngreso.column("Fecha", stretch=True)
        self.treeviewIngreso.column("Detalle", minwidth=100)
        self.treeviewIngreso.column("Detalle", stretch=True)
        self.treeviewIngreso.column("Monto", minwidth=50)
        self.treeviewIngreso.column("Monto", stretch=True)
        
        self.treeviewIngreso.configure(yscrollcommand=vsb.set)
        vsb.place(relx=0.945, rely=0.467, relheight=0.452)
        self.ButtonCI = tk.Button(self.top)
        self.ButtonCI.place(relx=0.13, rely=0.233, height=24, width=47)
        self.ButtonCI.configure(activebackground="beige")
        self.ButtonCI.configure(activeforeground="black")
        self.ButtonCI.configure(background="#d9d9d9")
        self.ButtonCI.configure(command=inversion_support.CargarCI)
        self.ButtonCI.configure(compound='left')
        self.ButtonCI.configure(disabledforeground="#a3a3a3")
        self.ButtonCI.configure(foreground="#000000")
        self.ButtonCI.configure(highlightbackground="#d9d9d9")
        self.ButtonCI.configure(highlightcolor="black")
        self.ButtonCI.configure(pady="0")
        self.ButtonCI.configure(text='''Cargar''')
        self.TextCI = tk.Text(self.top)
        self.TextCI.place(relx=0.13, rely=0.167, relheight=0.057, relwidth=0.144)

        self.TextCI.configure(background="white")
        self.TextCI.configure(font="TkTextFont")
        self.TextCI.configure(foreground="black")
        self.TextCI.configure(highlightbackground="#d9d9d9")
        self.TextCI.configure(highlightcolor="black")
        self.TextCI.configure(insertbackground="black")
        self.TextCI.configure(selectbackground="#c4c4c4")
        self.TextCI.configure(selectforeground="black")
        self.TextCI.configure(wrap="word")
        self.TextSaldo = tk.Text(self.top)
        self.TextSaldo.place(relx=0.13, rely=0.3, relheight=0.057
                , relwidth=0.144)
        self.TextSaldo.configure(background="white")
        self.TextSaldo.configure(font="TkTextFont")
        self.TextSaldo.configure(foreground="black")
        self.TextSaldo.configure(highlightbackground="#d9d9d9")
        self.TextSaldo.configure(highlightcolor="black")
        self.TextSaldo.configure(insertbackground="black")
        self.TextSaldo.configure(selectbackground="#c4c4c4")
        self.TextSaldo.configure(selectforeground="black")
        self.TextSaldo.configure(wrap="word")
        self.TextFechaCI = tk.Text(self.top)
        self.TextFechaCI.place(relx=0.41, rely=0.167, relheight=0.057
                , relwidth=0.194)
        self.TextFechaCI.configure(background="white")
        self.TextFechaCI.configure(font="TkTextFont")
        self.TextFechaCI.configure(foreground="black")
        self.TextFechaCI.configure(highlightbackground="#d9d9d9")
        self.TextFechaCI.configure(highlightcolor="black")
        self.TextFechaCI.configure(insertbackground="black")
        self.TextFechaCI.configure(selectbackground="#c4c4c4")
        self.TextFechaCI.configure(selectforeground="black")
        self.TextFechaCI.configure(wrap="word")
        self.TextFecha = tk.Text(self.top)
        self.TextFecha.place(relx=0.41, rely=0.3, relheight=0.057
                , relwidth=0.194)
        self.TextFecha.configure(background="white")
        self.TextFecha.configure(font="TkTextFont")
        self.TextFecha.configure(foreground="black")
        self.TextFecha.configure(highlightbackground="#d9d9d9")
        self.TextFecha.configure(highlightcolor="black")
        self.TextFecha.configure(insertbackground="black")
        self.TextFecha.configure(selectbackground="#c4c4c4")
        self.TextFecha.configure(selectforeground="black")
        self.TextFecha.configure(wrap="word")
        self.ButtonDeleteEgreso = tk.Button(self.top)
        self.ButtonDeleteEgreso.place(relx=0.44, rely=0.933, height=24, width=47)

        self.ButtonDeleteEgreso.configure(activebackground="beige")
        self.ButtonDeleteEgreso.configure(activeforeground="black")
        self.ButtonDeleteEgreso.configure(background="#d9d9d9")
        self.ButtonDeleteEgreso.configure(compound='left')
        self.ButtonDeleteEgreso.configure(disabledforeground="#a3a3a3")
        self.ButtonDeleteEgreso.configure(foreground="#000000")
        self.ButtonDeleteEgreso.configure(highlightbackground="#d9d9d9")
        self.ButtonDeleteEgreso.configure(highlightcolor="black")
        self.ButtonDeleteEgreso.configure(pady="0")
        self.ButtonDeleteEgreso.configure(text='''Eliminar''')
        self.ButtonDeleteIngreso = tk.Button(self.top)
        self.ButtonDeleteIngreso.place(relx=0.94, rely=0.933, height=24
                , width=47)
        self.ButtonDeleteIngreso.configure(activebackground="beige")
        self.ButtonDeleteIngreso.configure(activeforeground="black")
        self.ButtonDeleteIngreso.configure(background="#d9d9d9")
        self.ButtonDeleteIngreso.configure(compound='left')
        self.ButtonDeleteIngreso.configure(disabledforeground="#a3a3a3")
        self.ButtonDeleteIngreso.configure(foreground="#000000")
        self.ButtonDeleteIngreso.configure(highlightbackground="#d9d9d9")
        self.ButtonDeleteIngreso.configure(highlightcolor="black")
        self.ButtonDeleteIngreso.configure(pady="0")
        self.ButtonDeleteIngreso.configure(text='''Eliminar''')
        self.ButtonExport = tk.Button(self.top)
        self.ButtonExport.place(relx=0.01, rely=0.933, height=24, width=47)
        self.ButtonExport.configure(activebackground="beige")
        self.ButtonExport.configure(activeforeground="black")
        self.ButtonExport.configure(background="#d9d9d9")
        self.ButtonExport.configure(compound='left')
        self.ButtonExport.configure(disabledforeground="#a3a3a3")
        self.ButtonExport.configure(foreground="#000000")
        self.ButtonExport.configure(highlightbackground="#d9d9d9")
        self.ButtonExport.configure(highlightcolor="black")
        self.ButtonExport.configure(pady="0")
        self.ButtonExport.configure(text='''Exportar''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    inversion_support.main()

if __name__ == '__main__':
    inversion_support.main()




