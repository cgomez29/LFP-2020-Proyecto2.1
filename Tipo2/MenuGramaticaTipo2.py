from colorama import Fore, Style
import os
import sys
from Tipo2.MenuAddUpGram import MenuAddUpGram
from Tipo2.ValidarCadena import ValidarCadena
from Tipo2.GenerarAP import GenerarAP
from Tipo2.VisualizarAutomata import VisualizarAutomata

class MenuGramTipo2:
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(MenuGramTipo2, self).__new__(self)
        return self.__instancia


    def __init__(self):
        self.menuGramAddUpp = MenuAddUpGram()
        self.validarCadena = ValidarCadena()
        self.generarAP = GenerarAP()
        self.visualizarAutomata = VisualizarAutomata()

    def menu(self):
        while True: 
            os.system("cls")
            print(Fore.WHITE + "1. Ingresar/Modificar Gramática")
            print("2. Generar autómata de pila")
            print("3. Visualizar autómata")
            print("4. Validar cadena")
            print("5. regresar")
            print("Salir" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.menuGramAddUpp.menu()
            elif entrada == '2':
                self.generarAP.menu()
            elif entrada == '3':
                self.visualizarAutomata.menu()
            elif entrada == '4':
                self.validarCadena.menu()           
            elif entrada == '5':
                break   
            elif entrada.lower() == 'salir':
                sys.exit()