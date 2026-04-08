#Clase Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
    
    def leer(self, paginas):
        self.pagina_actual += paginas
        if self.pagina_actual > self.paginas:
            self.pagina_actual = self.paginas
        return f"Leíste {paginas} páginas. Vas en la página {self.pagina_actual}"
    
    def info(self):
        return f"'{self.titulo}' por {self.autor}, {self.paginas} páginas"

# Usar la clase
mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez", 500)
print(mi_libro.info())           # 'Cien años de soledad' por Gabriel García Márquez, 500 páginas
print(mi_libro.leer(50))         # Leíste 50 páginas. Vas en la página 50
print(mi_libro.leer(100))        # Leíste 100 páginas. Vas en la página 150