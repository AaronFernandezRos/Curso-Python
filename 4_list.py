### LISTS ###

#Definicion de listas vacias

my_list=list() #Crear una lista vacia usando el constructor list()
my_other_list=[] #Imprime una lista vacia usando []

print(len(my_list)) #Imprime la longitud de la lista, es este caso es 0

print(len(my_other_list)) #Imprime la longitud de la lista, es este caso es 0

#Definir una lista de valores 

my_list=[35,20,40,35,14]

print(my_list)
print(len(my_list))

#Lista de tipos diferentes
my_type_list=["Hola", 3, "Mundo", 1.88, 3]

print(my_type_list)
print(len(my_type_list))

#Acceso a elementos de una lista

print(my_type_list[0]) #Accede al primer elemento
print(my_type_list[-1]) #Accede al ultimo elemento
print(my_type_list[-4]) #Accede al primer elemento
print(my_type_list.count(3)) #Cuenta el numero de elementos que se repiten del numero 3

#Como buscar el indice 

print(my_type_list.index("Hola")) #Cuenta el numero de palabras que hay en la lista contando desde 0
print(my_type_list.index("Mundo")) #Cuenta el numero de palabras que hay en la lista

#Desempaquetar una lista

#caja, hola, var6, var4, var5, var3= my_type_list

#print(caja, hola, var3)

var1, var2 =my_type_list[1], my_type_list[2]
print(var1, var2)

#Concatenar dos listas

list1=["Hola", 3]
list2=["Mundo", 1.88, 3, "Hola"]

print(list1+list2)

list3=list1+list2

print(list3)

#CURL de elementos (Creacion, Insercion, Actualizacion, Eliminacion)

list3.append("Jorge")

print(list3)

list3.append(85)
print(list3)

list3.insert(3, "Jose")
print(list3)

list3.remove("Hola")
print(list3)

list3[0]="Javier"
print(list3)

resultado=list3.pop()
print(list3)
print(resultado)

resultado=list3.pop(0)
print(list3)
print(resultado)

del list3[1]
print(list3)

list4=list3.copy()
print(list4)

list3.clear()
print(list3)
print(list4)

list4.reverse()
print(list4)

list_int=[45, 34, 12, 1, 56]

list_int.sort(reverse=True)
print(list_int)

print(list_int[1:3])

list_string="Hola vamos a tomar por ..."
print(list_string)
print(type(list_string))