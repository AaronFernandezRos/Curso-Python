# Clase Book

class Book:
    def __init__(self, title, author):
        """"
        Constructor de la clase Book
        :param title: title 
        :param author: Autor del libro. 
        """

        self.title = title  # Propiedad publica: titulo del libro
        self.author = author  # Propiedad publica: autor del libro
        self.__is_borrowed = False  # Propiedad privada: indica si el libro está prestado
        
    def borrow(self):
        """"
        Metodo para prestar un libro
        Retorna True si se prestó exitosamente, False si ya está prestado. 
        """
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True
    
    def is_borrowed(self):
        """"
        Metodo para para verificar si el libro está prestado. 
        """
        return self.__is_borrowed
    
    def return_book(self):
        """
        Método para devolver el libro.
        """
        self.__is_borrowed = False
        
    def __str__(self):
        """
        Representación en string del libro.
        """
        status = "Prestado" if self.__is_borrowed else "Disponible"
        return f"'{self.title}' por {self.author} ({status})"


# Clase Biblioteca
class Library:
    def __init__(self):
        """
        Constructor de la clase Library.
        Inicializa una lista vacía de libros.
        """
        self.books = []  # Lista pública para almacenar los libros
    
    def add_book(self, book):
        """
        Método para agregar un libro a la biblioteca.
        :param book: Instancia de la clase Book.
        """
        self.books.append(book)
        print(f"Libro '{book.title}' agregado a la biblioteca.")
        
    def show_books(self):
        """
        Método para mostrar los libros disponibles en la biblioteca.
        """
        if not self.books:
            print("La biblioteca está vacía.")
            return
        print("\nLibros en la biblioteca:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")
            
    def borrow_book(self, title):
        """
        Método para prestar un libro.
        :param title: Título del libro a prestar.
        """
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Has prestado el libro: '{title}'.")
                    return
                else:
                    print(f"El libro '{title}' ya está prestado.")
                    return
        print(f"No se encontró el libro con título: '{title}'.")
        
    def return_book(self, title):
        """
        Método para devolver un libro.
        :param title: Título del libro a devolver.
        """
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"Has devuelto el libro: '{title}'.")
                return
        print(f"No se encontró el libro con título: '{title}'.")



# my_book = Book("Titulo 1", "Yo mismo")

# #Estado previo del libro
# print("Estado previo del libro")
# status = "Prestado" if my_book.is_borrowed() else "Disponible"

# print(f"El libro está {status}")

# #Actualizar variable status
# status = "Prestado" if my_book.is_borrowed() else "Disponible"

# #Imprimir por pantalla el status actual
# print(f"El libro está {status}")

# my_book.return_book()
# #Actualizar variable status
# status = "Prestado" if my_book.is_borrowed() else "Disponible"

# #Imprimir por pantalla el status actual
# print(f"El libro está {status}")

# print(f"El titulo es {my_book.title} y el autor es {my_book.author}")


# #Prestar libro
# my_book.borrow()
# print(my_book)
# #Devolver libro
# my_book.return_book()
# print(my_book)

#Ejecucion del proyecto
if __name__ == "__main__":
    #Crear una instancia de la biblioteca
    my_library= Library()
    
    #print/my_library.show_books()
    my_library.show_books()
    

#Agregar libros a la biblioteca

    book1 = Book("Libro 1", "Autor 1")
    book2 = Book("Libro 2", "Autor 2")
    book3 = Book("Libro 3", "Autor 3")
    
    
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    
#Mostrar libros de la biblioteca
    my_library.show_books()
    
    my_library.borrow_book("Libro 2")
    
    
    