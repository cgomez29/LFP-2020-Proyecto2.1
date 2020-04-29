import os
import re
from ControladorGramatica import ControladorGramatica
from colorama import Fore, Style
from ControladorAFD import ControladorAFD
from Recorrido import Recorrido
from bean.AFD import AFD

class MenuCadena(object):
    #Menu de evaluar cadena
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(MenuCadena, self).__new__(self)
        return self.__instancia


    def __init__(self):
        self.controladorGramatica = ControladorGramatica()
        self.controladorAFD = ControladorAFD()
        self.__obj = None
        self.__tipo = ""
        self.__recorrido = Recorrido("G1")
        self.__nombre = ""

    def menuCadena(self):
        contador  = True
        bandera = True
        while (contador):
            os.system("cls")
            print("Ingresa el nombre de la gramatica a utilizar:")
            print(">>", end="")
            nombre = input()
            if nombre.lower() == "salir":
                bandera = False
                break

            objGram = self.controladorGramatica.buscarGramatica(nombre) 
            objAfd = self.controladorAFD.buscarAFD(nombre)
            self.__nombre = nombre
            if ((objGram) != None):
                self.__obj = objGram 
                self.__tipo = "Gramatica"
                contador = False
            elif ((objAfd) != None):
                self.__obj = objAfd
                self.__tipo = "AFD"
                contador = False
            else: 
                print(Fore.RED + "La gramatica o el AFD: \"" + nombre +  "\" No existe! " + Style.RESET_ALL)
                input()
                contador = True

        while bandera:    
            os.system("cls")
            print(Fore.GREEN + str(self.__tipo) + ": " + nombre + Style.RESET_ALL)
            print(Fore.WHITE + "1. Solo Validar")
            print("2. Ruta en AFD")     
            print("3. Expandir con gramatica")
            print("4. Ayuda" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                print("Ingrese cadena a evaluar")
                print(">>", end="")
                entrada = input()
                if (self.__tipo == "AFD"):
                    self.soloValidar(self.__obj, entrada)
                    self.controladorAFD.llenarCadenas(nombre, entrada)
                else:
                    self.controladorGramatica.llenarCadenas(nombre, entrada)
                    self.convertirGramatica2(self.__obj, entrada) #Covierte la gramatica a un afd
            if entrada == '2':
                print("Ingrese cadena a evaluar")
                print(">>", end="")
                entrada = input()
                if (self.__tipo == "AFD"):
                    self.rutaAFD(self.__obj, entrada)
                else:
                    self.convertirGramatica(self.__obj, entrada) #Covierte la gramatica a un afd

            if entrada == '3':
                self.expandirGramatica()
            elif entrada == '4':
                print("Lenguajes formales B+")
                print("Jóse Véliz")
                print("0")
                input()
            elif entrada.lower() == 'salir':
                break


    def convertirGramatica(self, obj, entrada):
        objAfd = AFD()
        objAfd.set_ArrayEstado(obj.get_ArrayNT())
        objAfd.set_ArrayAlfabeto(obj.get_ArrayT())
        objAfd.set_EstadoInicial(obj.get_NTInicial())


        ### Ingresando las producciones
        ## para AFD: A,B;0
        ## para Gramatica, A > 0 B [a-d5-8]
        #patron = "[a-z]|[0-9]"
        patron = "[a-z]|[0-9]"
        patron2 = "[A-Z]"
        bandera = True
        arrayTransiciones = []
        for x in obj.get_ArrayProduccion():
            if not ( "epsilon" in x):
                x = x.split(">")
                ## primer valor
                valor1 = x[0]

                valor2 = re.findall(patron2, x[1])

                valor3 = re.findall(patron, x[1])
                try:
                    transicion = str(valor1) + "," + str(valor2.pop(0)) + ";" + str(valor3.pop(0))
                except IndexError as x:
                    bandera = False
                    break

                transicion = transicion.replace(" ", "")
                
                arrayTransiciones.append(transicion)
        
        objAfd.set_ArrayTransicion(arrayTransiciones)

        ## ingresando los estados de aceptacion
        arrayAceptacion = []
        for x in obj.get_ArrayProduccion():
            if ( "epsilon" in x):
                x = x.replace(" ", "").split(">")
                arrayAceptacion.append(x[0])

        objAfd.set_ArrayAceptacion(arrayAceptacion)

        #self.controladorAFD.crearAFD("cris" ,objAfd.get_ArrayEstado(), objAfd.get_ArrayAlfabeto(),
        #   objAfd.get_EstadoInicial(), objAfd.get_ArrayAceptacion(), objAfd.get_ArrayTransicion() )
        if bandera:
            if self.rutaAFD(objAfd, entrada):
                if (self.__tipo == "AFD"):
                    self.controladorAFD.llenarValidas(self.__nombre, entrada)
                else:
                    self.controladorGramatica.llenarValidas(self.__nombre, entrada)
            else:
                if (self.__tipo == "AFD"):
                    self.controladorAFD.llenarInvalidas(self.__nombre, entrada)
                else:
                    self.controladorGramatica.llenarInvalidas(self.__nombre, entrada)
        else:
            print(Fore.RED + "Recursiva por la izquierda" + Style.RESET_ALL)
            input()

    def rutaAFD(self, obj, entrada):
        self.__recorrido = Recorrido('g1')

        for x in obj.get_ArrayEstado():
            self.__recorrido.agregarNodo(Nodo(x))

        # Trancisiones
        patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"

        for i in obj.get_ArrayTransicion():
            estados = re.findall(patron, i)
            try:
                x = estados.pop(0)
                y = estados.pop(0)
                z = estados.pop(0)
            except IndexError:
                print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
                
            self.__recorrido.obtenerNodo(x).crearArista(self.__recorrido.obtenerNodo(y), z)
    
        # Estado Incial
        self.__recorrido.setEstadoInicial(obj.get_EstadoInicial())

            # Estado de aceptacion
        for x in obj.get_ArrayAceptacion():
            self.__recorrido.setearNodoAceptacion(x)

        self.__recorrido.verificar(entrada)   


    def convertirGramatica2(self, obj, entrada):
        objAfd = AFD()
        objAfd.set_ArrayEstado(obj.get_ArrayNT())
        objAfd.set_ArrayAlfabeto(obj.get_ArrayT())
        objAfd.set_EstadoInicial(obj.get_NTInicial())

        patron = "[a-z]|[0-9]"
        patron2 = "[A-Z]"
        bandera = True
        arrayTransiciones = []
        for x in obj.get_ArrayProduccion():
            if not ( "epsilon" in x):
                x = x.split(">")
                ## primer valor
                valor1 = x[0]

                valor2 = re.findall(patron2, x[1])

                valor3 = re.findall(patron, x[1])
                try:
                    transicion = str(valor1) + "," + str(valor2.pop(0)) + ";" + str(valor3.pop(0))
                except IndexError as x:
                    bandera = False
                    break

                transicion = transicion.replace(" ", "")
                
                arrayTransiciones.append(transicion)
        if bandera:
            objAfd.set_ArrayTransicion(arrayTransiciones)

            ## ingresando los estados de aceptacion
            arrayAceptacion = []
            for x in obj.get_ArrayProduccion():
                if ( "epsilon" in x):
                    x = x.replace(" ", "").split(">")
                    arrayAceptacion.append(x[0])

            objAfd.set_ArrayAceptacion(arrayAceptacion)

            self.soloValidar(objAfd, entrada)
        else:
            print(Fore.RED + "Recursiva por la izquierda" + Style.RESET_ALL)
            input()

    def soloValidar(self, obj, entrada):
        self.__recorrido = Recorrido('g1')

        for x in obj.get_ArrayEstado():
            self.__recorrido.agregarNodo(Nodo(x))

        # Trancisiones
        patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"

        for i in obj.get_ArrayTransicion():
            estados = re.findall(patron, i)
            try:
                x = estados.pop(0)
                y = estados.pop(0)
                z = estados.pop(0)
            except IndexError:
                print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
                
            self.__recorrido.obtenerNodo(x).crearArista(self.__recorrido.obtenerNodo(y), z)
    
        # Estado Incial
        self.__recorrido.setEstadoInicial(obj.get_EstadoInicial())

            # Estado de aceptacion
        for x in obj.get_ArrayAceptacion():
            self.__recorrido.setearNodoAceptacion(x)
            
          
        if self.__recorrido.validar(entrada):
            if (self.__tipo == "AFD"):
                self.controladorAFD.llenarValidas(self.__nombre, entrada)
            else:
                self.controladorGramatica.llenarValidas(self.__nombre, entrada)
        else:
            if (self.__tipo == "AFD"):
                self.controladorAFD.llenarInvalidas(self.__nombre, entrada)
            else:
                self.controladorGramatica.llenarInvalidas(self.__nombre, entrada)



    def expandirGramatica(self):
        print("En construccion!!")
        input()
    


class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_aristas = []
        self.inicial = False

    def crearArista(self, nodo_final, valor):
        self.lista_aristas.append(Arista(self, nodo_final, valor))

class Arista:
    def __init__(self, inicial, final, valor):
            self.nodo_inicial = inicial
            self.nodo_final = final
            self.valor = valor