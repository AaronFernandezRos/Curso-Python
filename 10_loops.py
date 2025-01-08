### LOOPS ###

# while

# my_condition = 0

# while my_condition < 10:
#     print(my_condition)
#     my_condition +=2
# else: #es opcional
#     print("Mi condición es mayor o igual a 10")

#
#
# Tabla del 8
# print("------------------------------")
# print("------------------------------")
# print("TABLA DEL 8 ")
# print("------------------------------")
# print("------------------------------")


# my_condition=0
# numero= 8
# while my_condition < 10:
#     my_condition+=1
#     if my_condition ==11:
#         print(my_condition)
#         break
#     resultado= numero * my_condition
#     print(f"{my_condition}x{numero} = {resultado}")
# print("Fin de Programa")

# print("------------------------------")
# print("------------------------------")
# print("TABLA INDICAANDO EL NÚMERO ")
# print("------------------------------")
# print("------------------------------")

# my_condition=0
# numero= int(input("Escribe un numero : "))
# while my_condition < 10:
#     my_condition+=1
#     if my_condition ==11:
#         break
#     resultado= numero * my_condition
#     print(f"{numero}x{my_condition} = {resultado}")
# print("Fin de Programa")

# FOR

my_list = [12, 34, 45, 67, 80, 23, 6]
my_tupla = (12, 34, 45, 67, 80, 23, 6)
my_set = {12, 34, 45, 67, 80, 23, 6}
my_dict = {"Nombre": "Pepe", 34: "Hola"}

# for item in my_dict.items():
#     print(item[1])

# for item in my_dict:
#     print(f"Dentro de iten hay: {item}")
#     print(f"El valor para la clave {item} es {my_dict[item]} ")


# my_dict = {"Nombre": "Pepe", 34: "Hola"}
# print(my_dict["Nombre"])

for item in my_dict:
    if item == "Nombre":
        print("Encontrado la clave Nombre en diccionario")
