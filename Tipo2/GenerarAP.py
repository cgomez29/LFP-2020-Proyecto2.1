import os
from ControladorGramatica import ControladorGramatica
from colorama import Fore, Style
from bean.Gramatica import Gramatica
from graphviz import Digraph
from Tipo2.Pila import Pila
from Grafo import Grafo
from bean.AP import AP
from ControladorAP import ControladorAP

class GenerarAP:

    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(GenerarAP, self).__new__(self)
        return self.__instancia

    def __init__(self):
        self.ControladorGramatica = ControladorGramatica()
        self.objGramatica = Gramatica()
        self.controladorAP = ControladorAP()
        self.objAP = AP()
        self.estados = []
        self.alfabeto = []
        self.simbolos = []
        self.transicion = []
        self.estadoInicial = ""
        self.estadosAceptacion = []
        self.nombre = ""
        self.__grafo = Grafo("G1")

    def menu(self):
        while (True):
            os.system("cls")
            print("GENERAR AUTOMATA DE PILA")
            print("Nombre de la gramatica a utilizar?")
            print(">>", end="")
            self.nombre = input()
            if self.nombre.lower() == "salir":
                break
            self.objGramatica = self.ControladorGramatica.buscarGramatica(self.nombre)

            if self.objGramatica != None:
                self.generar()
                break
            else:
                print(Fore.RED + " \"" + self.nombre +
                      "\" Gramatica no existe!" + Style.RESET_ALL)
                input()
                break


    #################################
    def generarParaPruebas(self):
        self.objGramatica = self.ControladorGramatica.buscarGramatica("q")         
        self.nombre = "q"
        self.generar()
    #################################

    def generar(self):
        grm = self.objGramatica
        # S
        self.estados = ["i", "p", "q", "f"]
        # Σ
        self.alfabeto = grm.get_ArrayT()

        # ┌
        for x in grm.get_ArrayT():
            self.simbolos.append(x)
        for x in grm.get_ArrayNT():
            self.simbolos.append(x)
        self.simbolos.append("#")

        # L
        self.estadoInicial = "i"
        # F
        self.estadosAceptacion.append("f") 

        # Se teando transiciones para Automata en estado Q
        # leo, pop, push
        self.transicion.append("i,λ,λ;p,#")
        self.transicion.append("p,λ,λ;q," + grm.get_NTInicial())
        for x in grm.get_ArrayT():
            self.transicion.append("q,"+x + "," + x + ";q,λ")
        for x in grm.get_ArrayProduccion():
            x = x.replace(" ", "")
            x = x.split(">")
            self.transicion.append("q,λ," + x[0] + ";q," + x[1])
        self.transicion.append("q,λ,#;f,λ")

        print(Fore.GREEN + str(self.estados) + Style.RESET_ALL)
        print(Fore.GREEN + str(self.alfabeto) + Style.RESET_ALL)
        print(Fore.GREEN + str(self.simbolos) + Style.RESET_ALL)
        print(Fore.GREEN + str(self.estadoInicial) + Style.RESET_ALL)
        print(Fore.GREEN + str(self.estadosAceptacion) + Style.RESET_ALL)
        print(Fore.GREEN + str(self.transicion) + Style.RESET_ALL)
        input()
        self.controladorAP.crearAP(self.nombre, self.estados, self.alfabeto,
            self.simbolos, self.estadoInicial, self.estadosAceptacion, self.transicion)


        self.graficarAutomata(self.estados, self.estadoInicial, self.estadosAceptacion, self.transicion)


    def graficarAutomata(self, estados, estadoInicial, estadosAceptacion, transiciones):
        self.__grafo = Grafo('g1')
        for x in estados:
            self.__grafo.agregarNodo(Nodo(x))

        # Trancisiones

        for i in transiciones:
            i = i.replace(";", ",")
            i = i.split(",")
            try:
                x = i[0]
                y = i[3]
                z = i[1] + "," + i[2] + ";" + i[4]
            except IndexError:
                print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
            self.__grafo.obtenerNodo(x).crearArista(self.__grafo.obtenerNodo(y), z)

        # Estado Incial
        self.__grafo.setEstadoInicial(estadoInicial)

        # Estado de aceptacion
        for x in estadosAceptacion:
            self.__grafo.setearNodoAceptacion(x)

        self.__grafo.graficar()
        ################### quitar numerales
        ##os.system("x.gv.png")
        ###################


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
