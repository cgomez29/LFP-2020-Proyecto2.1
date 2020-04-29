import os
from ControladorAP import ControladorAP
from colorama import Fore, Style
from bean.AP import AP
from Tipo2.RecorridoAP import RecorridoAP
from Tipo2.GenerarAP import GenerarAP

class ValidarCadena:

    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(ValidarCadena, self).__new__(self)
        return self.__instancia

    def __init__(self):
        self.controladorAP = ControladorAP()
        self.objAP = AP()
        self.cadena = ""

        ################3
        self.generarAP = GenerarAP()
        ################3


    def menu(self):
        contador  = True
        ####################
        self.generarAP.generarParaPruebas()
        ####################
        bandera = True
        while (contador):
            os.system("cls")
            print("VALIDAR CADENA")
            print("Nombre de la gramatica a utilizar?")
            print(">>", end="")
            nombre = input()
            if nombre.lower() == "salir":
                bandera = False
                break
            self.objAP = self.controladorAP.buscarAP(nombre)

            if self.objAP != None :
                contador = False

            else: 
                print(Fore.RED + " \"" + nombre +  "\" Gramatica no existe!" + Style.RESET_ALL)
                input()
                contador = True

        while bandera: 
            os.system("cls")
            print(Fore.WHITE + "1. Ingresar cadena")
            print("2. Resultado")
            print("3. Reporte")
            print("4. regresar" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.ingresarCadena()
            elif entrada == '2':
                self.resultado()
            elif entrada == '3':
                self.reporte()
            elif entrada.lower() == '4':
                break

    def ingresarCadena(self):
        while True:
            os.system("cls")
            print("INGRESE CADENA A VALUAR")
            print(">>", end="")
            entrada = input()
            if entrada.lower() == "salir":
                break
            
            self.cadena = entrada 
            self.mensaje("Cadena agregada existosamente!")

    def resultado(self): ## Validando cadena
        self.__recorrido = RecorridoAP('g1')
        obj = self.objAP

        for x in obj.get_Estados():
            self.__recorrido.agregarNodo(Nodo(x))

        # Trancisiones
        for i in obj.get_Transicion():
            i = i.replace(";", ",")
            i = i.split(",")
            try:
                x = i[0]
                y = i[3]
                z = i[1] + "," + i[2] + ";" + i[4]
            except IndexError:
                print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
            
            self.__recorrido.obtenerNodo(x).crearArista(self.__recorrido.obtenerNodo(y), z)
    
        # Estado Incial
        self.__recorrido.setEstadoInicial(obj.get_EstadoInicial())

        # Estado de aceptacion
        for x in obj.get_EstadoAcetacion():
            self.__recorrido.setearNodoAceptacion(x)
        ########################### Descomentar#############################################
        self.__recorrido.validar("λλλ" + self.cadena + "#")   
        #####self.__recorrido.validar("λλλab#")   

    
    def reporte(self):
        ## Tabla de repórte
        pass


    def mensaje(self, mensaje):
        print(Fore.GREEN + " " + mensaje+ Style.RESET_ALL);
        input()

    def mensajeError(self, mensaje):
        print(Fore.RED + " " + mensaje+ Style.RESET_ALL);
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