
# Imprimir por pantalla un menu para poder
# Seleccionar una de las siguientes operaciones:
# suma, resta, multiplicacion y division
# El programa pedira dos numeros por pantalla
# y mostrará el resultado final de la operacion

# my_condition=0
# numero= int(input("Indica que operacion quieres realizar : "))
# while my_condition < 10:
#     my_condition+=1
#     if my_condition ==11:
#         break
#     resultado= numero * my_condition
#     print(f"{numero}x{my_condition} = {resultado}")


# num1= int(input("Dame el primer número: "))
# num2= int(input("Dame el segundo número: "))

def mostrar_menu():
    print("-----------------------")
    print("===CALCULADORA BÁSICA===")
    print("-----------------------")
    print("Indica '1' para SUMAR")
    print("Indica '2' para RESTAR")
    print("Indica '3' para MULTIPLICAR")
    print("Indica '4' para DIVIDIR")
    print("-----------------------")


def seleccion_operaciones():
    operaciones = int(input("Selecciona la operación que quieres realizar: "))
    while operaciones< 5:
        if operaciones > 5:
            break
        elif operaciones == 1:
            if suma:
                break
        elif operaciones == 2:
            if resta: 
                break       

def suma(num1, num2):
    return num1 + num2
    


def resta(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 / num2


mostrar_menu()
seleccion_operaciones()
