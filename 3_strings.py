### Strings ###

#Declaración de strings usando comillas simples y dobles
my_string="Hola uno"
my_others_string='Hola dos'

print(my_string)
print(my_others_string)


#Declaración de strings usando comillas simples y dobles
variable1="Hola uno"
variable2='Hola dos'

print(variable1)
print(variable2)

#Concatenar string con un espacio en blanco

print(variable1+", "+variable2)

#Crear un salto de línea
variable3="Esto es un string\ncon salto de línea"
print(variable3)

#Insertar tabulación

variable4="Esto es un string\tcon salto de línea"
print(variable4)

#Escapar(Mostrar) caracteres especiales
variable5="\\tEsto es un string \ncon salto de línea"
print(variable5)

#Formateo de strings

name, surname, age="Aaron", "Fernandez", 22
print(name, surname, age)

#Formateo usando .format()

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))

#Formateo antiguo usando %

print("Mi nombre es %s %s y mi edad es %d"%(name,surname,age))

#Concatenar varios string

print("Mi nombre es "+ name +" "+ surname + " y mi edad es " + str(age))

#Formateo usando f-strings (moderno)

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetamos caracteres

language="Python"

a,b,c,d,e,f=language

print(a)
print(b)

#Dividir strings (Slice)

language_slice= language[1:3]
print(language_slice)

language_slice= language[1:]
print(language_slice)

language_slice=language[-2] #Toma el segundo caracter empezando por la derecha
print(language_slice)

language_slice=language[0:6:2] #Toma caracteres de indice 0 al 6, saltando de 2 en 2
print(language_slice)

#Revertir la cadena de texto
language_slice=language[::-1]
print(language_slice)

### Funciones de string ###

#Remplazar caracteres de un string

fruit="Strawberry"
fruit_replace=fruit.replace('r', 'R')
print(fruit_replace)

#Convertir el primer caracter del texto en mayuscula
print(fruit.capitalize())

#Convertir todo el texto en mayuscula
print(fruit.upper())

#Convertir todo el texto en miniscula
print(fruit.lower())

#Verificar si todo el texto esta en minuscula
print(fruit.islower())

#Contar cuantos caracteres hay del mismo tipo
print(fruit.count("r"))

#Contar todos los caracteres de una palabara
print(len(fruit))
print(f"La variable {fruit} tiene: "+ str(len(fruit)))

numero_de_letras =len(fruit)
print(numero_de_letras)
print(str(numero_de_letras).isnumeric())

#Verificar si comienza la cadena con unos caracteres
print(language.startswith("Py"))