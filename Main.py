import sys 
import os
import msvcrt
from graphviz import Digraph
from colorama import Fore, Style

from menu.MenuAFD import MenuAFD
from menu.MenuGramatica import MenuGramatica
from menu.MenuCadena import MenuCadena
from menu.CargarArchivo import CargarArchivo
from menu.MenuReporte import MenuReporte
from Error import Error
from menu.MenuGuardar import MenuGuardar
from Tipo2.MenuGramaticaTipo2 import MenuGramTipo2

class Main:
    __instancia = None

    @staticmethod
    def getInstancia():
        if Main.__instancia == None:
            Main()
        return Main.__instancia

    def __init__(self):
        if Main.__instancia != None:
            raise Exception("This class is a singleton!")
        else:
            Main.__instancia = self

        self.error = Error()
        self.menuAFD = MenuAFD()
        self.cargarArchivo = CargarArchivo()
        self.menuGramatica = MenuGramatica()
        self.menuCadena = MenuCadena()
        self.menuReporte = MenuReporte()
        self.menuGuardar = MenuGuardar()
        self.menuGramTipo2 = MenuGramTipo2()

    def menuPrincipal(self):
        os.system("cls")
        print(Fore.GREEN + "Lenguajes formales")
        print("Seccion B+")
        print("Carne: 201801480" + Style.RESET_ALL)
        try:
            while True:
                m = str(msvcrt.getch(),'utf -8')
                if m == "\r":
                    os.system("cls")
                    self.menuSecundario()
                    break
                else:
                    self.menuPrincipal()
        except UnicodeDecodeError:    
            self.error.mensaje("Desea salir? s/n")
            entrada = input()
            if (entrada == "s"):
                sys.exit()


    def menuSecundario(self):
        while True:
            os.system("cls")
            print(Fore.WHITE + "1. Crear un AFD")
            print("2. Crear Gramática")        
            print("3. Evaluar Cadenas")        
            print("4. Reportes")        
            print("5. Cargar archivo de entrada")        
            print("6. Guardar")        
            print("7. Gramáticas tipo2 y AP")        
            print("Salir" + Style.RESET_ALL)        
            print(">>", end="")
            entrada = input()
            if entrada == "1":
                self.menuAFD.menuAFD()
            elif(entrada == "2"):
                self.menuGramatica.menuGramatica()
            elif(entrada == "3"):
                self.menuCadena.menuCadena()
            elif(entrada == "4"):
                self.menuReporte.menuReporte()
            elif(entrada == "5"):
                self.cargarArchivo.openFile()
            elif(entrada == "6"):
                self.menuGuardar.menuGuardar()
            elif(entrada == "7"):
                self.menuGramTipo2.menu()
            elif(entrada == "0"):
                self.menuReporte.generarReporte() #Borrar esto
            elif entrada.lower() == "salir":
                main.menuPrincipal()


main = Main().getInstancia()

main.menuPrincipal()
