import os
from ControladorGramatica import ControladorGramatica
from colorama import Fore, Style

class MenuGramatica:
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(MenuGramatica, self).__new__(self)
        return self.__instancia

    def __init__(self):
        self.__nombreGramatica = ""
        self.__arrayNT = []
        self.__arrayT = []
        self.__nTInicial = "" #guarda el nombre del no terminal inicial
        self.__arrayProducciones = []        
        self.controladorGramatica = ControladorGramatica()

    def menuGramatica(self):
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
                print(Fore.RED + " \"" + nombre +  "\" Nombre ya existe!" + Style.RESET_ALL)
                input()
                contador = True

        while bandera: 
            os.system("cls")
            print(Fore.WHITE + "1. Ingresar NT")
            print("2. Ingresar terminales")
            print("3. NT inicial")
            print("4. Producciones")
            print("5. Mostrar gramatica transformada")
            print("6. Ayuda" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.noTerminales()
            elif entrada == '2':
                self.terminales()
            elif entrada == '3':
                self.nTInicialExiste()
            elif entrada == '4':
                self.producciones()
            elif entrada == '5':
                self.gramaticaTransformada()
            elif entrada == '6':
                print("Lenguajes formales B+")
                print("Jóse Véliz")
                print("0")
                input()
            elif entrada.lower() == 'salir':
                self.controladorGramatica.crearGramatica(self.__nombreGramatica, self.__arrayNT,
                    self.__arrayT, self.__nTInicial, self.__arrayProducciones)
            
                self.__arrayNT = []
                self.__arrayT = []
                self.__arrayProducciones = []
                break
    
    def noTerminales(self):
        contador = True
        while (contador):
            os.system("cls")
            print("Ingresar No Terminales")
            print(">>", end="")
            dato = input()
            if(self.nTRepetido(dato) and self.terminalRepetido(dato)):
                self.__arrayNT.append(dato)
                print(Fore.YELLOW + "Desea seguir ingresando NT s/n ?"+ Style.RESET_ALL)
                dato = input()
                if (dato == 's'):
                    contador = True
                else:
                    contador = False
            else:
                print(Fore.RED + " \"" + dato +  "\" NT ya existe!" + Style.RESET_ALL)
                input()

    def terminales(self):
        contador = True
        while (contador):
            os.system("cls")
            print("Ingresar terminales")
            print(">>", end="")
            dato = input()
            if(self.terminalRepetido(dato) and self.nTRepetido(dato)):
                self.__arrayT.append(dato)
                print(Fore.YELLOW + "Desea seguir ingresando T s/n ?"+ Style.RESET_ALL)
                dato = input()
                if (dato == 's'):
                    contador = True
                else:
                    contador = False
            else:
                print(Fore.RED + " \"" + dato +  "\" terminal ya existe!" + Style.RESET_ALL)
                input()

    def nTInicialExiste(self): #comprueba que el NT exista y lo guarda
        contador = True
        if (len(self.__arrayNT) != 0):
            os.system("cls")
            print("Ingrese NT inicial")
            print(">>", end="")
            dato = input()
            for e in self.__arrayNT:
                if(dato == e):
                    self.__nTInicial = dato
                    contador = False
                    print('NT inicial: ' + self.__nTInicial)   
                    input()
            if contador == True:
                print(Fore.RED + "El NT no existe!" + Style.RESET_ALL)
                input()
        else: 
            print(Fore.RED + "Porfavor ingrese NT" + Style.RESET_ALL)
            input()

    def producciones(self):
        while True:
            os.system("cls")
            print("Ingrese su producción")
            print(">>", end="")
            dato = input()
            if(dato.lower() == "salir"):
                print(Fore.GREEN + "Producciones guardadas" + Style.RESET_ALL)
                input()
                break
            self.__arrayProducciones.append(dato)



    def gramaticaTransformada(self):
        print(Fore.YELLOW + "Esta función no se encuentra disponible!" + Style.RESET_ALL)
        input()


    def terminalRepetido(self, terminal):  #Alfabeto
        if (len(self.__arrayT) == 0):
            return True
        for e in self.__arrayT:
            if terminal == e:
                return False    
        return True       

    def nTRepetido(self, valor):
        if (len(self.__arrayNT) == 0):
            return True
        for a in self.__arrayNT:
            if valor == a:
                return False
        return True


    def modificar(self, nombre, arrayNT, arrayT, nTInicial, arrayProduccion):
        self.__nombreGramatica = nombre
        self.__arrayNT = arrayNT
        self.__arrayT = arrayT
        self.__nTInicial = nTInicial
        self.__arrayProducciones = arrayProduccion

        self.menuGramatica2(nombre)


    def menuGramatica2(self, nombre):
        
        while True: 
            os.system("cls")
            print(Fore.WHITE + "1. Ingresar NT")
            print("2. Ingresar terminales")
            print("3. NT inicial")
            print("4. Producciones")
            print("5. Mostrar gramatica transformada")
            print("6. Ayuda" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.noTerminales()
            elif entrada == '2':
                self.terminales()
            elif entrada == '3':
                self.nTInicialExiste()
            elif entrada == '4':
                self.producciones()
            elif entrada == '5':
                self.gramaticaTransformada()
            elif entrada == '6':
                print("Lenguajes formales B+")
                print("Jóse Véliz")
                print("0")
                input()
            elif entrada.lower() == 'salir':
                self.controladorGramatica.crearGramatica(self.__nombreGramatica, self.__arrayNT,
                    self.__arrayT, self.__nTInicial, self.__arrayProducciones)
                
                
                self.__arrayNT = []
                self.__arrayT = []
                self.__arrayProducciones = []
                break