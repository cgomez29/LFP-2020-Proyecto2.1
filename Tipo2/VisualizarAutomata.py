import os
from ControladorAP import ControladorAP
from colorama import Fore, Style
from bean.AP import AP
from Grafo import Grafo

class VisualizarAutomata:

    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(VisualizarAutomata, self).__new__(self)
        return self.__instancia

    def __init__(self):
        self.controladorAP = ControladorAP()
        self.objAP = AP()

    def menu(self):
        while (True):
            os.system("cls")
            print("VISUALIZAR AUTOMATA")
            print("Nombre de la gramatica a utilizar?")
            print(">>", end="")
            nombre = input()
            
            if nombre.lower() == "salir":
                break
            
            self.objAP = self.controladorAP.buscarAP(nombre)
            if self.objAP != None :
                self.generarSextupla()
                break
            else: 
                print(Fore.RED + " \"" + nombre +  "\" Gramatica no existe!" + Style.RESET_ALL)
                input()
        
        


    def generarSextupla(self):
        ap = self.objAP

        print(Fore.GREEN + "S: " + Style.RESET_ALL, end="")
        for x in ap.get_Estados():
            print(Fore.BLUE + " \"" + x +  "\"," + Style.RESET_ALL, end= "")
        print("")

        print(Fore.GREEN + "Σ: " + Style.RESET_ALL, end="")
        for x in ap.get_Alfabeto():
            print(Fore.BLUE + " \"" + x +  "\"," + Style.RESET_ALL, end= "")
        print("")

        print(Fore.GREEN + "┌: " + Style.RESET_ALL, end="")
        for x in ap.get_Simbolos():
            print(Fore.BLUE + " \"" + x +  "\"," + Style.RESET_ALL, end= "")
        print("")

        print(Fore.GREEN + "L: " + Style.RESET_ALL, end="")
        print(Fore.BLUE + " \"" + ap.get_EstadoInicial() +  "\"" + Style.RESET_ALL)

        print(Fore.GREEN + "F: " + Style.RESET_ALL, end="")
        for x in ap.get_EstadoAcetacion():
            print(Fore.BLUE + " \"" + x +  "\"," + Style.RESET_ALL, end= "")
        print("")

        print(Fore.GREEN + "T: " + Style.RESET_ALL)
        for x in ap.get_Transicion():
            print(Fore.BLUE + " \"" + x +  "\"" + Style.RESET_ALL)

        self.graficarAutomata(ap.get_Estados(), ap.get_EstadoInicial(), ap.get_EstadoAcetacion(), ap.get_Transicion())
        input()
        


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
        os.system("x.gv.png")


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
