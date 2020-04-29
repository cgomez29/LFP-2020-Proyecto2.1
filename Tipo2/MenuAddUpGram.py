import os
from ControladorGramatica import ControladorGramatica
from colorama import Fore, Style
from bean.Gramatica import Gramatica

class MenuAddUpGram:

    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(MenuAddUpGram, self).__new__(self)
        return self.__instancia

    def __init__(self):
        self.__nombreGramatica = ""
        self.__arrayT = []
        self.__arrayNT = []
        self.__nTInicial = "" #guarda el nombre del no terminal inicial
        self.__arrayProducciones = []        
        self.controladorGramatica = ControladorGramatica()
    

    def menu(self):
        contador  = True

        bandera = True
        while (contador):
            os.system("cls")
            print("Ingresa el nombre para la gramatica")
            print(">>", end="")
            nombre = input()
            if nombre.lower() == "salir":
                bandera = False
                break
            if (self.controladorGramatica.nombreGramaticaRepetido(nombre)):
                self.__nombreGramatica = nombre
                contador = False
            else: 
                print(Fore.GREEN + "Gramatica: \"" + nombre +  "\" - MODIFICAR" + Style.RESET_ALL)
                input()   
                g = Gramatica() 
                g = self.controladorGramatica.buscarGramatica(nombre)
                self.__nombreGramatica = g.get_NombreGramatica()
                self.__arrayT = g.get_ArrayT()
                self.__arrayNT = g.get_ArrayNT()
                self.__nTInicial = g.get_NTInicial()
                self.__arrayProducciones = g.get_ArrayProduccion()  
                contador = False
    

        while bandera: 
            os.system("cls")
            print(Fore.WHITE + "1. Ingresar terminales")
            print("2. Ingresar no terminales")
            print("3. Ingresar producciones")
            print("4. Borrar producciones")
            print("5. No terminal inicial")
            print("6. regresar" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.ingresarTerminales()
            elif entrada == '2':
                self.ingresarNoTerminales()
            elif entrada.lower() == '6':
                self.controladorGramatica.crearGramatica(self.__nombreGramatica,
                 self.__arrayNT, self.__arrayT, self.__nTInicial, self.__arrayProducciones)
                break

    
    def ingresarTerminales(self):
        while True:
            os.system("cls")
            print("Ingrese el no terminal")
            print(">>", end="")
            entrada = input()

            if (entrada.lower() == "salir"):
                break
            else:
                self.__arrayT.append(entrada)
                self.mensaje("Terminal agregado con exito!")


    def ingresarNoTerminales(self):
        while True:
            os.system("cls")
            print("Ingrese el terminal")
            print(">>", end="")
            entrada = input()

            if (entrada.lower() == "salir"):
                break
            else:
                self.__arrayNT.append(entrada)
                self.mensaje("No Terminal agregado con exito!")

    def ingresarProduccion(self):
        while True:
            os.system("cls")
            print("Ingrese la producción")
            print(">>", end="")
            entrada = input()

            if (entrada.lower() == "salir"):
                break
            else:
                self.__arrayProducciones.append(entrada)
                self.mensaje("Producción agregado con exito!")


    def ingresarNTInicial():
        os.system("cls")
        print("Ingrese el No terminal inicial")
        print(">>", end="")
        entrada = input()
        self.__arrayProducciones.append(entrada)
        self.mensaje("No terminal inicial agregado con exito!")

    def borrarProduccion():
        pass


    def mensaje(self, mensaje):
        print(Fore.GREEN + " " + mensaje+ Style.RESET_ALL);
        input()

    def mensajeError(self, mensaje):
        print(Fore.RED + " " + mensaje+ Style.RESET_ALL);
        input()