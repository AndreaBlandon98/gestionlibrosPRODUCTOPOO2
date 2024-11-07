import sqlite3

class Libro:
    def __init__(self, titulo, autor, año_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero

    def guardar(self):
        conn = sqlite3.connect('../data/biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO libros (titulo, autor, año_publicacion, genero) VALUES (?, ?, ?, ?)',
                       (self.titulo, self.autor, self.año_publicacion, self.genero))
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():
        conn = sqlite3.connect('../data/biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM libros')
        libros = cursor.fetchall()
        conn.close()
        return libros


    def actualizar(id, titulo, autor, año_publicacion, genero):
        conn = sqlite3.connect('../data/biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE libros SET titulo = ?, autor = ?, año_publicacion = ?, genero = ? WHERE id = ?',
                       (titulo, autor, año_publicacion, genero, id))
        conn.commit()
        conn.close()


    def eliminar(id):
        conn = sqlite3.connect('../data/biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
        conn.commit()
        conn.close()
