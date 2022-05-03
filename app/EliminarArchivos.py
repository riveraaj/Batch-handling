import math
from os import remove
import pathlib
from random import randint
import datetime
import logging
import time

menu = """
        Menú Eliminar Archivos
        -----------------------

1. Continuar en Eliminar Archivos
0. Salir al Menú Principal
________________________________

"""

bienvenida = """
        Se encuentra en la opción Eliminar Archivos
        -----------------------------------------
"""


class Eliminar:

    def __init__(self):

        try:
            id = randint(10000, 19999)
            aux = id
            if (aux == id):
                id = randint(1000, 19999)
            else:
                id = id
            opcion = 0
            while (True):
                print(bienvenida)
                pathCarpeta = input(
                    "Digite la ruta de la carpeta del archivo: ")
                archivo = input(
                    "Digite el nombre y la extensión del archivo: ")
                pathArchivo = pathCarpeta + "/" + archivo
                if (pathlib.Path(pathArchivo).is_file()):
                    inicioTiempo = time.perf_counter()
                    eliminarArchivo = remove(pathArchivo)
                    finalTiempo = time.perf_counter()
                    print("\nEl tiempo de ejecución del proceso de Eliminar Archivos es de " +
                          str(finalTiempo - inicioTiempo)+" segundos")
                    print("\nArchivo eliminado correctamente")
                    bitacora = input(
                        "Desea registrar este cambio en la bitácora? (Y/N) > ").upper()
                    while (bitacora != "N" and bitacora != "Y"):
                        print("No ha ingresado una opción correcta")
                        bitacora = input(
                            "Desea registrar este cambio en la bitácora? (Y/N) > ").upper()
                    fecha_hora = datetime.datetime.now()
                    fecha_y_hora_en_texto = fecha_hora.strftime(
                        '%d/%m/%Y %H:%M:%S')
                    if bitacora == "Y":
                        logging.basicConfig(
                            filename='Bitacora', level=logging.INFO)
                        logging.info("\n\n--- Eliminar Archivos ---" + "\n" + "Identificación de Batch: " + str(id) + "\n" + "Ruta de carpeta del archivo: " +
                                     pathArchivo + "\n" + "Archivo elminado: " + archivo + "\n" + "Fecha y hora: "+fecha_y_hora_en_texto+"\n")
                        print("Se ha guardado el cambio en la bitácora")

                else:
                    print("Ha ocurrido un error, revise la ruta " +
                      str(pathCarpeta) + " y el archivo " + str(archivo))
                print(menu)
                opcion = int(input("Digite una de las opciones > "))
                print(menu)
                opcion = int(input("Digite una de las opciones > "))
                if (opcion == 0):
                    break
                elif(opcion == 1):
                    print()
                else:
                    print("El número digitado no es una opción") 
        except OSError as oS:
            print(oS)
