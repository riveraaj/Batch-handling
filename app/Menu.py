import CopiarArchivos as oA
import MoverArchivos as mA
import EliminarArchivos as eA
import io
from os import remove
import os

menu = """
        Menú Principal
        --------------

1. Copiar Archivos
2. Mover Archivos
3. Eliminar Archivos
4. Visualizar Bitácora
5. Eliminar Bitácora
6. Eliminar Configuración
0. Salir
________________________________
        """

def Menu():
    try:
        while True:
            print(menu)
            opcion = int(input("Digite una de las opciones > "))   
            if (opcion == 1):
                oA.Copiado()
            elif (opcion == 2):
                mA.Moviendo()
            elif (opcion == 3):
                eA.Eliminar()
            elif (opcion == 4):
                bitacora = io.open("Bitacora", "r")
                registro = bitacora.read()
                bitacora.close()
                print("\n--- Bitácora  ---\n\n"+registro)
            elif (opcion == 5):
                if(os.path.exists("Bitacora")):                  
                    os.remove("Bitacora")
                    print("Bitácora eliminada correctamente")
                else:
                    print("El archivo no existe")
            elif (opcion == 6):
                pathConfiguracion = str(
                    input("Digite la ruta de la carpeta del archivo de configuración > "))
                pathOr = str(
                    input("Digite nombre y extensión del archivo de configuración > "))
                pathA = pathConfiguracion + '/' + pathOr
                remove(pathA)
                print("Configuracion eliminada correctamente")
            elif (opcion == 0):
                break
            else : 
                print("El número digitado no es una opción")
    except BaseException:
        pass    

Menu()