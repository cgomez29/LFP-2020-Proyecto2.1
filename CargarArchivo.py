import easygui
import os
import re
from easygui import *
from colorama import Fore, Style
from ControladorAFD import ControladorAFD
from ControladorGramatica import ControladorGramatica
from MenuAFD import MenuAFD
from MenuGramatica import MenuGramatica

class CargarArchivo(object):
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(CargarArchivo, self).__new__(self)
        return self.__instancia   


    def __init__(self):
        self.controlador = ControladorAFD()
        self.controladorGramatica = ControladorGramatica()
        self.menuAFD = MenuAFD()
        self.menuGramatica = MenuGramatica()
        
        self.__ruta = ""

        ## Para el AFD 
        self.nombreAFD = '' #Arreglo nombre de AFD
        self.arrayEstado = []
        self.arrayAlfabeto = []
        self.estadoIncial = ''
        self.arrayAceptacion = []
        self.arrayTransicion = []

        ## Para la gramtica
        self.__nombreGramatica = ""
        self.__arrayNT = []
        self.__arrayT = []
        self.__nTInicial = "" #guarda el nombre del no terminal inicial
        self.__producciones = []

    def openFile(self):
        while True:
            os.system("cls")
            print(Fore.WHITE + "1. AFD")
            print("2. Gramática" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == "1":
                self.__ruta = str(easygui.fileopenbox(title="Abrir AFD", filetypes=[["* .afd", "AFD files"]] , default='*.afd'))
                if self.__ruta != "None":
                    self.readArchivoAFD()
                else:
                    print(Fore.YELLOW + "Debes seleccionar un documento" + Style.RESET_ALL)
                    input()
            elif entrada == "2":
                self.__ruta = str(easygui.fileopenbox(title="Abrir Gramatica", filetypes=[["*.grm", "Gramatica files"]] , default='*.grm'))
                if self.__ruta != "None":
                    self.readArchivoGramatica()
                else:
                    print(Fore.YELLOW + "Debes seleccionar un documento" + Style.RESET_ALL)
                    input()
            elif entrada.lower() == "salir":
                break
    


    def readArchivoGramatica(self):
        patron1 = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"
        patron2 = "[A-Z]"
        patron3 = "[a-z]|[0-9]"
        patron4 = "[A-Z]|[0-9]"
        while True:
            nombre = os.path.split(self.__ruta)
            nombre = nombre[1]
            nombre = nombre.split(".")

            archivo = open(self.__ruta, "r")

            contador = 0
            if(self.controladorGramatica.nombreGramaticaRepetido(nombre[0])):
                self.__nombreGramatica = nombre[0]
                for line in archivo.readlines():
                    if line != "\n":
                        print(Fore.WHITE + str(line) + Style.RESET_ALL)
                        if "|" in line: 
                            line = line.replace(" ", "").split(">")
                            nt = line[0]
                            line = line[1].split("|")
                            for x in line: 
                                produc = nt + " > " + x

                                ##Agregando las producciones
                                self.__producciones.append(produc)
                                ######################################3
                                                        
                                
                                produc = produc.replace(" ", "").split(">")
                                
                                if contador == 0:   
                                    self.__arrayNT.append(produc[0])
                                    self.__nTInicial = produc[0]
                                    contador += 1
                                else:
                                    if self.existeNt(produc[0]):
                                        self.__arrayNT.append(produc[0])

                                if not ( "epsilon" in produc[1]):
                                    terminales = re.findall(patron3, produc[1])
                                    #print(str(terminales))
                                    for x in terminales:
                                        if self.existeT(x):
                                            self.__arrayT.append(x)
                                    
                        else:
                            #----------------------------------------------------------------------#
                            ##Agregando las producciones
                            self.__producciones.append(line)
                            ######################################3
                            line = line.replace(" ", "").split(">")
                            
                            if contador == 0:   
                                self.__arrayNT.append(line[0])
                                self.__nTInicial = line[0]
                                contador += 1
                            else:
                                if self.existeNt(line[0]):
                                    self.__arrayNT.append(line[0])

                            if not ( "epsilon" in line[1]):
                                terminales = re.findall(patron3, line[1])
                                for x in terminales:
                                    if self.existeT(x):
                                        self.__arrayT.append(x)

                input()
                archivo.close()
                print(Fore.YELLOW + "Desea realizar algunas modificaciones? s/n" + Style.RESET_ALL)
                entrada = input()

                if (entrada == "s"):
                    self.menuGramatica.modificar(self.__nombreGramatica, self.__arrayNT, self.__arrayT,
                        self.__nTInicial, self.__producciones)
                else:
                    self.controladorGramatica.crearGramatica(self.__nombreGramatica, self.__arrayNT,
                    self.__arrayT, self.__nTInicial, self.__producciones)
    
                    self.__arrayNT = []
                    self.__arrayT = []
                    self.__producciones = []

                    print(Fore.YELLOW + "Exito! Gramatica: " + self.__nombreGramatica  + Style.RESET_ALL)
                    input()
                
                break
            else:
                print(Fore.RED + " \"" + str(nombre[0]) +  "\" Nombre ya existe!" + Style.RESET_ALL)
                print(Fore.RED + " \"" + "Cambie el nombre de su archivo!! " + Style.RESET_ALL)
                input()
                break

    def readArchivoAFD(self):
        patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]+|false|true"

        while True:
            contador = 0
            nombre = os.path.split(self.__ruta)
            nombre = nombre[1]
            nombre = nombre.split(".")

            archivo = open(self.__ruta, "r")

            if(self.controlador.nombreAfdRepetido(nombre[0])):
                self.nombreAFD = nombre[0]
                x = y = z = p = q = ""
                try:
                    for line in archivo.readlines():
                        if line != "\n":
                            print(Fore.WHITE + str(line) + Style.RESET_ALL)
                            estados = re.findall(patron, line)
                            #print(estados)
                            try:
                                x = estados.pop(0) 
                                y = estados.pop(0)
                                z = estados.pop(0)
                                p = estados.pop(0)
                                q = estados.pop(0)
                                # X y P se corresponden
                                # Y y Q se corresponden
                            except IndexError:
                                print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
                            
                            if contador == 0:
                                self.arrayEstado.append(x)
                                self.estadoIncial = x
                                if(p == "true"):
                                    self.arrayAceptacion.append(x)
                            else:
                                if (self.existeEstado(x)):
                                    self.arrayEstado.append(x)

                                if(p == "true"):
                                    self.arrayAceptacion.append(x)
                                elif p == "false":
                                    self.eliminarAceptacion(x)
                            
                            if (self.existeEstado(y)):
                                self.arrayEstado.append(y)

                            if (q == "true"):
                                self.arrayAceptacion.append(y)
                            elif q == "false":
                                self.eliminarAceptacion(y)

                            if (self.existeAlfabeto(z)):
                                self.arrayAlfabeto.append(z)

                            self.arrayTransicion.append(x+","+y+";"+z)
                        contador +=1

                        #print("Array Acep: "+ str(self.arrayAceptacion))

                    archivo.close()

                    print(Fore.YELLOW + "Desea realizar algunas modificaciones? s/n" + Style.RESET_ALL)
                    entrada = input()

                    if (entrada == "s"):
                        self.menuAFD.modificar(self.nombreAFD, self.arrayEstado, self.arrayAlfabeto,
                            self.estadoIncial, self.arrayAceptacion, self.arrayTransicion)
                    else:
                        self.controlador.crearAFD(self.nombreAFD, self.arrayEstado,
                                self.arrayAlfabeto, self.estadoIncial, self.arrayAceptacion,
                                self.arrayTransicion)
                        self.arrayEstado = []
                        self.arrayAlfabeto = []
                        self.arrayAceptacion = []
                        self.arrayTransicion = []

                        print(Fore.YELLOW + "Exito! AFD: " + self.nombreAFD  + Style.RESET_ALL)
                        input()
                        
                except(FileNotFoundError,IOError):
                    print("")
                break
            else:
                print(Fore.RED + " \"" + str(nombre[0]) +  "\" Nombre ya existe!" + Style.RESET_ALL)
                print(Fore.RED + " \"" + "Cambie el nombre de su archivo!! " + Style.RESET_ALL)
                input()
                break
    
    ## Para el AFD
    ##Cambio de aceptacion
    def eliminarAceptacion(self, estado):
        contador = 0
        #print("Estado: " + estado)
        #print("Array: " + str(self.arrayAceptacion))
        for x in self.arrayAceptacion:
            if x == estado:
                self.arrayAceptacion.pop(contador)
                break
            contador +=1


    def existeEstado(self, estado):
        for x in self.arrayEstado:
            if (x == estado):
                return False
        return True

    def existeAlfabeto(self, alfabeto):
        for x in self.arrayAlfabeto:
            if (x == alfabeto):
                return False
        return True

    ## Para la gramatica

    def existeNt(self, nterminal):
        for x in self.__arrayNT:
            if (x == nterminal):
                return False
        return True

    def existeT(self, alfabeto):
        for x in self.__arrayT:
            if (x == alfabeto):
                return False
        return True