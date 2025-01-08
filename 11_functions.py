
pi= 3.14

# FUNCIONES QUE NO DEVUELVEN

# def my_funcion():
#     print("Hola Mundo")


# def imprimir_hola_mundo():
#     print("Hola Mundo")

# imprimir_hola_mundo()

def suma(var1,var2):
    print(var1+var2)
    
def sumar():
    var1= int(input("Dame el primer número: "))
    var2= int(input("Dame el segundo número: "))
    suma(var1,var2)

def multiplicar_por_pi_por_un_valor_dado(valor):
    print(valor * pi)
    
# suma(2,5)
# suma(4,3)
# suma(9,20)
# suma(1,3)

# sumar()

# multiplicar_por_pi_por_un_valor_dado(34)

#FUNCION QUE DEVUELVE (GRACIAS A RETURN)
def resta(var1, var2):
    resultado = var1 - var2
    return resultado

# var3 =resta(4,2)
# print(var3)
print(resta(4,2))

def encriptar(texto):
    #hacer escriptacion
    return texto
