import os
import csv

#Trabajando con .txt Files
# with open("ficheros/example.txt", "w+", encoding="utf-8") as txt_file:
with open(r"C:\GitHub\Curso Python\ficheros\example.txt", "w+", encoding="utf-8") as txt_file:

    
    #Escribir contenido en el archivo
    txt_file.write("Hola, este es un archivo de texto.\n")
    txt_file.write("Python es genial para manejar archivos.\n")