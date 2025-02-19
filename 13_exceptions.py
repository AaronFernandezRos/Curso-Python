### MANEJO DE EXCEPCIONES ###

valueOne = 10
valueTwo = 0
valueTree = "abc"

# try:
#     result= valueOne / valueTwo
#     print("No se ha producido un error")
# except:
#     # Se ejecuta si se produce una excepción
#     print("Se ha producido un error durante la división")

# try:
#     result= valueOne/int("tres")
#     print("No se ha producido un error")
# except:
#     print("Se ha producido un error durante la conversión o división")
# else: #Opcional
#     # Se ejecuta si no se produce una excepción
#     print("La ejecución se completó correctamente")
# finally: #Opcional
#     print("La ejecución del bloque try ha terminado")

# try:
#     result= valueOne / "dhfdshbf"
#     print("No se ha producido un error")
# except ZeroDivisionError:
#     print("Se ha producido un ZeroDivision")
# except ValueError:
#     print("Se ha producido un ValueError")
# except TypeError:
#     print("Se ha producido un TypeError")

try:
    result= valueOne / "dhfdshbf"
    print("No se ha producido un error")
except Exception as general_error:
    print(f"Se ha producido un error inesperado: {general_error}")