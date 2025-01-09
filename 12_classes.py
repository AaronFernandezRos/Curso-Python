
class Animal:
    def __init__(self, species, sound, color="rojo", age: int=0):
        self.species=species # Propiedad pública (todos pueden ver)
        self.__sound=sound #Propiedad privado (solo la clase puede ver)
        self.age= age #Propiedades público con valor inicial
        self._color= color #Propiedades protegidas
        
    def make_sound(self):
        #Metodo público, que puede usarse por cualquier persona
        print(f"El {self.species} hace {self.__sound}")
        
    def get_sound(self):
        #Metodo que utiliza el objeto para acceder a la propiedad sound
        return self.__sound
    
    def grow_older(self):
        #Incrementa la edad en un año al objeto animal
        # self.age=self.age +1 
        self.age +=1
        if self.age >15:
            print(f"El {self.species} la ha palmado")
        else:
            print(f"El {self.species} ahora tiene la edad de {self.age}")

my_animal= Animal("Perro", "Guau", "azul", 15)
my_animal_2= Animal("Gato", "Meow")


# print(type(my_animal))
# print(type(my_animal_2))

# print(type(my_animal.age))
# print(type(my_animal_2.age))

# print (f"La especie del animal es: {my_animal._color} y su edad es  {my_animal.age}.")
# print (f"La especie del animal es: {my_animal_2.species} y su edad es {my_animal_2.age}.")

# my_animal.age=12

# print(my_animal._color)

# my_animal.make_sound()

# print(my_animal.get_sound())
print(my_animal.grow_older())
