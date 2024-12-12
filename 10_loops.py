### LOOPS ###

#while

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

print("------------------------------")
print("------------------------------")
print("TABLA INDICAANDO EL NÚMERO ")
print("------------------------------")
print("------------------------------")

my_condition=0
numero= int(input("Escribe un numero : "))
while my_condition < 10:
    my_condition+=1
    if my_condition ==11:
        break
    resultado= numero * my_condition
    print(f"{numero}x{my_condition} = {resultado}")
print("Fin de Programa")