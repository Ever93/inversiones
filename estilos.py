import tkinter.ttk as ttk
import sys

# Definir los valores de estilo
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana2color = 'beige' # X11 color: #f5f5dc
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
    style.map('.',background = [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
        style.map('.',foreground = [('selected', 'white'), ('active','white')])
    else:
        style.map('.',foreground = [('selected', 'black'), ('active','black')])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Treeview',  font="TkDefaultFont")
    _style_code_ran = 1
