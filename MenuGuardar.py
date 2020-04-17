import os
import re
import easygui as eg
from colorama import Fore, Style

from ControladorGramatica import ControladorGramatica
from ControladorAFD import ControladorAFD

class MenuGuardar(object):
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(MenuGuardar, self).__new__(self)
        return self.__instancia
        
    def __init__(self):
        self.__controladorGramatica = ControladorGramatica()
        self.__controladorAFD = ControladorAFD()
        self.__obj = None #Podra ser de tipo AFD o de Tipo Gramatica
        self.__tipo = ""
        

    def menuGuardar(self):
        contador  = True
        while (contador):
            os.system("cls") 
            print("Ingresa el nombre de la Gramatica o AFD a guardar:")
            print(">>", end="")
            nombre = input()
            if nombre.lower() == "salir":
                break
            objGram = self.__controladorGramatica.buscarGramatica(nombre) 
            objAFD = self.__controladorAFD.buscarAFD(nombre) 

            if ((objGram) != None):
                self.__tipo = "Gramatica"                
                self.__obj = objGram 
                self.guardar()
                contador = False
            elif ((objAFD) != None):
                self.__tipo = "AFD"
                self.__obj = objAFD
                self.guardar()
                contador = False
            else: 
                print(Fore.RED + "La Gramatica o AFD: \"" + nombre +  "\" No existe! " + Style.RESET_ALL)
                input()
                contador = True
        
        

    def guardar(self):
        patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"
        if self.__tipo == "AFD":
            extension = ["*.afd"]     
            archivo = eg.filesavebox(msg="Guardar archivo",
                        title="Control: filesavebox",
                        default="automata.afd",
                        filetypes=extension)
            ruta = str(archivo)
            file = open(ruta, "w")

            ## A,A;1
            for w in self.__obj.get_ArrayTransicion():
                estados = re.findall(patron, w)
                try:
                    x = estados.pop(0) 
                    y = estados.pop(0)
                    z = estados.pop(0)
                    p = "false"
                    q = "false"
                    # X y P se corresponden
                    # Y y Q se corresponden
                except IndexError:
                    print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL) 
                if self.esAceptacion(x):
                    p = "true"
                if self.esAceptacion(y):
                    q = "true"
                file.write(x + "," + y + "," + z + ";" + p + ","+ q + "\n")
            file. close()
            os.system(ruta)
        else:
            extension  = ["*.grm"]
            archivo = eg.filesavebox(msg="Guardar archivo",
                        title="Control: filesavebox",
                        default="gramatica.grm",
                        filetypes=extension)
            ruta = str(archivo)
            file = open(ruta, "w")
            for x in self.__obj.get_ArrayProduccion():
                file.write(x + "\n")
            file.close()
            os.system(ruta)

    def esAceptacion(self, estado):
        for x in self.__obj.get_ArrayAceptacion():
            if (estado == x):
                return True
        return False
            


        

        
        
        