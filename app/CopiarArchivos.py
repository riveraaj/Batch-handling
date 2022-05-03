from ast import Try
import math
import pathlib
from random import randint
import shutil
import datetime
import logging
import io
import time
import os

menu = """
        Menú Copiar Archivos
        -----------------------

1. Continuar en Copiar Archivos
0. Salir al Menú Principal
________________________________

"""
subMenu = """
        Menú Copiar Archivos
        -----------------------

1. Continuar
0. Salir al Menú Copiar Archivos
________________________________

"""

bienvenida = """
        Se encuentra en la opción Copiar Archivos
        -----------------------------------------
"""


class Copiado:

    pathOrigen = ''
    pathDestino = ''
    numberID = ''
    extensionesCopiado = []

    def __init__(self):
        
        global pathOrigen
        global pathDestino
        global numberID
        global extensionesCopiado
        
        print(bienvenida)
        opcion = str(input(
            "Tiene previamente el archivo '.txt' de configuración de archivos? (Y/N) > ")).upper()
        while (opcion != "N" and opcion != "Y"):
            print("No ha ingresado una opcion correcta")
            opcion = str(input(
                "Tiene previamente el archivo '.txt' de configuración de archivos? (Y/N) > ")).upper()
        try:
            if (opcion == "Y"):
                pathConfiguracion = str(
                    input("Digite la ruta de la carpeta del archivo de configuración > "))
                pathOr = str(
                    input("Digite nombre y extensión del archivo de configuración > "))
                pathA = pathConfiguracion + '/' + pathOr
                if (pathlib.Path(pathA).is_file()):
                    archivo = open(pathA, 'r')
                    datos = archivo.readlines()
                    for x in datos:
                        comprobar = x.split('=')
                        if (comprobar[0].strip() == 'Origen'):
                            pathOrigen = comprobar[1].strip('\n')
                        elif (comprobar[0].strip() == 'Destino'):
                            pathDestino = comprobar[1].strip('\n')
                        elif(comprobar[0].strip() == 'ID'):
                            numberID = comprobar[1].strip('\n')
                        elif (comprobar[0].strip() == 'CopyFiles'):
                            extensionesCopiado = comprobar[1].strip(
                                '\n').split(',')
                        elif (comprobar[0].strip() == 'MoveFiles'):
                            print()
                        else:
                            print('El archivo "'+pathA +
                                  '" no cumple con la configuración necesaria')
                    archivo.close()
                    self.copiadoArchivos()
                else:
                    print("\nHa ocurrido un error, revise la ruta " + str(pathA))
            elif(opcion == "N"):
                eleccion = str(input("Desea crear el archivo de configuración de archivos? (Y/N) > ")).upper()
                while (opcion != "N" and opcion != "Y"):
                    print("No ha ingresado una opcion correcta")
                    eleccion = str(input("Desea crear el archivo de configuración de archivos? (Y/N) > ")).upper()
                if(eleccion == "Y"):
                    pathO = str(input("Digite la ruta de la carpeta Origen de los archivos > "))
                    pathD = str(input("Digite la ruta de la carpeta Destino de los archivos > "))
                    numID = str(input("Digite el ID unico del proceso > "))
                    file = open("Configuracion.txt", "a")
                    file.write("Origen="+pathO + "\n")
                    file.write("Destino="+pathD + "\n")
                    file.write("ID=" +numID + "\n")
                    file.write("CopyFiles=xlsx,docx,txt" + "\n")
                    file.write("MoveFiles=xlsx,docx,txt" + "\n")       
                    file.close()          
                    archivo = open("Configuracion.txt", "r")
                    datos = archivo.readlines()
                    for x in datos:
                        comprobar = x.split('=')
                        if (comprobar[0].strip() == 'Origen'):
                            pathOrigen = comprobar[1].strip('\n')
                        elif (comprobar[0].strip() == 'Destino'):
                            pathDestino = comprobar[1].strip('\n')
                        elif(comprobar[0].strip() == 'ID'):
                            numberID = comprobar[1].strip('\n')
                        elif (comprobar[0].strip() == 'CopyFiles'):
                            extensionesCopiado = comprobar[1].strip(
                                '\n').split(',')
                        elif (comprobar[0].strip() == 'MoveFiles'):
                            extensionesMoviendo = comprobar[1].strip(
                                '\n').split(',')
                        else:
                            print('El archivo "'+pathA +
                                '" no cumple con la configuración necesaria')
                    archivo.close() 
                    self.copiadoArchivos()
                else:
                    copiadoAlternativa()
        except OSError:
            archivo.close()
            print(OSError.strerror)
        except BaseException:
            archivo.close()
            print(BaseException)

    def copiadoArchivos(self):
        global extensionesCopiado
        try:
            listaArchivos = os.listdir(pathOrigen)
            inicioTiempo = time.perf_counter()
            for x in extensionesCopiado:
                if ((x.endswith('xlsx')) or (x.endswith('docx')) or (x.endswith('txt'))):
                    for z in listaArchivos:
                        if (z.endswith('.'+x)):
                            pathArchivo = pathOrigen + '/' + z
                            shutil.copy(pathArchivo, pathDestino)
                            print("\nElemento copiado correctamente")
                            finalTiempo = time.perf_counter()
                            print("\nEl tiempo de ejecución del proceso de Copiar Archivos es de " +
                                  str(finalTiempo - inicioTiempo)+" segundos")
                            bitacora = input(
                                "\nDesea registrar este cambio en la bitácora? (Y/N) > ").upper()
                            while (bitacora != "N" and bitacora != "Y"):
                                print("No ha ingresado una opción correcta")
                                bitacora = input(
                                    "Desea registrar este cambio en la bitácora? (Y/N) > ").upper()
                            fecha_hora = datetime.datetime.now()
                            fecha_y_hora_en_texto = fecha_hora.strftime(
                                '%d/%m/%Y %H:%M:%S')
                            if bitacora == "Y":
                                bitacoraCopiar = logging.basicConfig(
                                    filename='Bitacora', level=logging.INFO)
                                logging.info("\n\n--- Copiar Archivos ---" + "\n" + "Identificacion de Batch: " + str(numberID) + "\n" + "Ruta de carpeta de los archivo: " +
                                             pathArchivo + "\n" + "Ruta de carpeta a copiar archivos: "+pathDestino + "\n" + "Fecha y hora: "+fecha_y_hora_en_texto+"\n")
                                print("Se ha guardado el cambio en la bitacora")
                else:
                    print("\nNo existe ningun archivo con las extensiones dadas")
        except FileNotFoundError:
            print(FileNotFoundError)
        except BaseException:
            print(BaseException)
            

def copiadoAlternativa():
    try:
        id = randint(10000, 19999)
        aux = id
        if (aux == id):
            id = randint(1000, 19999)
        else:
            id = id
        opcion = 0
        while (True):
            pathCarpeta = input("\nDigite la ruta de la carpeta del archivo: ")
            archivo = input("Digite el nombre y la extensión del archivo: ")
            pathArchivo = pathCarpeta + "/" + archivo
            if (pathlib.Path(pathArchivo).is_file()):
                while (True):
                    pathFinal = input(
                        "Digite la ruta de la carpeta a copiar el archivo: ")
                    if(pathlib.Path(pathFinal).is_dir()):
                        inicioTiempo = time.perf_counter()
                        copiarArchivo = shutil.copy(pathArchivo, pathFinal)
                        finalTiempo = time.perf_counter()
                        print("\nEl tiempo de ejecucion del proceso de Copiar Archivos es de " +
                                str(finalTiempo - inicioTiempo)+" segundos")
                        print("\nArchivo copiado correctamente\n")
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
                            bitacoraCopiar = logging.basicConfig(
                                filename='Bitacora', level=logging.INFO)
                            logging.info("\n\n--- Copiar Archivos ---" + "\n" + "Identificación de Batch: " + str(id) + "\n" + "Ruta de carpeta del archivo: " +
                                        pathArchivo + "\n" + "Ruta de carpeta a copiar archivo: "+pathFinal + "\n" + "Fecha y hora: "+fecha_y_hora_en_texto+"\n")
                            print("Se ha guardado el cambio en la bitácora")
                        break
                    else:
                        print("\nHa ocurrido un error, revise la ruta " +
                                str(pathFinal) + " y el archivo " + str(archivo))
                        print(subMenu)
                        opcion = int(input("Digite una de las opciones > "))
                        if (opcion == 0):
                            break
                        elif(opcion == 1):
                            print()
                        else:
                            print("El número digitado no es una opción")
            else:
                print("Ha ocurrido un error, revise la ruta " +
                        str(pathCarpeta) + " y el archivo " + str(archivo))
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
