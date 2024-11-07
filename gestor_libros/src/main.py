import sqlite3
from gui.app import BibliotecaApp
import tkinter as tk

def base_datos():
    conn = sqlite3.connect('../data/biblioteca.db')  # Ajusta la ruta
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        año_publicacion INTEGER,
        genero TEXT
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    base_datos()
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
