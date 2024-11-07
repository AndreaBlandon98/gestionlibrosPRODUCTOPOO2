import tkinter as tk
from tkinter import messagebox, simpledialog
from src.libro import Libro


class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestión de Libros")
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.lista_libros = tk.Listbox(self.frame, width=50)
        self.lista_libros.pack()

        self.boton_agregar = tk.Button(self.frame, text="Agregar Libro", command=self.agregar_libro)
        self.boton_agregar.pack()

        self.boton_editar = tk.Button(self.frame, text="Editar Libro", command=self.editar_libro)
        self.boton_editar.pack()

        self.boton_eliminar = tk.Button(self.frame, text="Eliminar Libro", command=self.eliminar_libro)
        self.boton_eliminar.pack()

        self.cargar_libros()

    def cargar_libros(self):
        self.lista_libros.delete(0, tk.END)
        libros = Libro.obtener_todos()
        for libro in libros:
            self.lista_libros.insert(tk.END, f"{libro[0]} - {libro[1]} por {libro[2]} ({libro[3]}), Género: {libro[4]}")

    def agregar_libro(self):
        titulo = simpledialog.askstring("Título", "Ingrese el título del libro:")
        autor = simpledialog.askstring("Autor", "Ingrese el autor del libro:")
        año_publicacion = simpledialog.askinteger("Año de Publicación", "Ingrese el año de publicación:")
        genero = simpledialog.askstring("Género", "Ingrese el género del libro:")

        if titulo and autor and año_publicacion and genero:
            nuevo_libro = Libro(titulo, autor, año_publicacion, genero)
            nuevo_libro.guardar()
            self.cargar_libros()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def editar_libro(self):
        seleccionado = self.lista_libros.curselection()
        if seleccionado:
            index = seleccionado[0]
            id_libro = int(self.lista_libros.get(index).split(" - ")[0])
            titulo = simpledialog.askstring("Título", "Ingrese el nuevo título del libro:")
            autor = simpledialog.askstring("Autor", "Ingrese el nuevo autor del libro:")
            año_publicacion = simpledialog.askinteger("Año de Publicación", "Ingrese el nuevo año de publicación:")
            genero = simpledialog.askstring("Género", "Ingrese el nuevo género del libro:")

            if titulo and autor and año_publicacion and genero:
                Libro.actualizar(id_libro, titulo, autor, año_publicacion, genero)
                self.cargar_libros()
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un libro para editar.")

    def eliminar_libro(self):
        seleccionado = self.lista_libros.curselection()
        if seleccionado:
            index = seleccionado[0]
            id_libro = int(self.lista_libros.get(index).split(" - ")[0])
            Libro.eliminar(id_libro)
            self.cargar_libros()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un libro para eliminar.")
