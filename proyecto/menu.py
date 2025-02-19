
class Menu:
    def __init__(self):
        """
        Constructor de la clase Menu
        """
        # self.library= Library() #Libreria
        
    def mostrar_menu(self):
        print("=== BIBLIOTECA ===")
        print("1. Añadir Libro")
        print("2. Reservar")
        print("3. Devolver")
        print("4. Listar Libro")
        print("5. Salir")
        
    def seleccionar_opcion(self):
        opcion = input("\nElige una opción (1-5):")  # Solicita una opción entre 1 y 5
        return opcion