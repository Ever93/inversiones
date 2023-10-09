import sqlite3

def conectar():
    conn = sqlite3.connect('comveta.db')
    c = conn.cursor()
    return conn, c

conn, c = conectar()
conn.commit()
conn.close()
