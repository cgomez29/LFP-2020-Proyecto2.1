import re
import os
from colorama import Fore, Style
from graphviz import Digraph
from ControladorAFD import ControladorAFD

class MenuAFD(object):
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(MenuAFD, self).__new__(self)
        return self.__instancia

    def __init__(self):
        self.controlador = ControladorAFD()
        self.nombreAFD = '' #Arreglo nombre de AFD
        self.arrayEstado = []
        self.arrayAlfabeto = []
        self.estadoIncial = ''
        self.arrayAceptacion = []
        self.arrayTransicion = []


    def menuAFD(self):
        contador  = True
        bandera = True
        while (contador):
            os.system("cls")
            print("Ingresa el nombre para el AFD")
            print(">>", end="")
            nombre = input()
            if nombre.lower() == "salir":
                bandera = False
                break
            if (self.controlador.nombreAfdRepetido(nombre)):
                self.nombreAFD = nombre
                contador = False
            else:
                print(Fore.RED + " \"" + nombre +  "\" Nombre ya existe!" + Style.RESET_ALL)
                contador = True

        while bandera:
            os.system("cls")    
            print(Fore.WHITE + "1. Ingresar estados")
            print("2. ingresar Alfabeto")
            print("3. Estado inicial")
            print("4. Estado de aceptacion")
            print("5. Transiciones")
            print("6. Ayuda" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.estado()
            elif entrada == '2':
                self.alfabeto()
            elif entrada == '3':
                self.estadoInicialExiste()
            elif entrada == '4':
                self.estadoAceptacionExiste()
            elif entrada == '5':
                self.menuModos()
            elif entrada == '8':
                self.generarAFD()
            elif entrada == '9':
                self.controlador.printArreglo()
            elif entrada == '6':
                print("Lenguajes formales B+")
                print("Jóse Véliz")
                print("0")
                input()
            elif entrada.lower() == 'salir':
                if len(self.arrayAceptacion) != 0:
                    self.controlador.crearAFD(self.nombreAFD, self.arrayEstado,
                        self.arrayAlfabeto, self.estadoIncial, self.arrayAceptacion,
                        self.arrayTransicion)
                    self.arrayEstado = []
                    self.arrayAlfabeto = []
                    self.arrayAceptacion = []
                    self.arrayTransicion = []
                    
                    break
                else:
                    print(Fore.RED +"Al menos tienes que ingresar un estado de aceptacion!!" + Style.RESET_ALL)
                    input()
                    
    def generarAFD(self):
        f = Digraph('finite_state_machine', filename='fsm.gv')
        f.attr(rankdir='LR', size='8,5')
        f.attr('node', shape='doublecircle')
        f.node(self.estadoAceptacion)
        f.attr('node', shape='circle')
        f.edge(self.estadoIncial, self.estadoAceptacion , label='SS(B)')
        f.view()
    
    def menuModos(self):
        while True:
            os.system("cls")
            print(Fore.YELLOW + "Elija el modo para ingresar las transiciones" + Style.RESET_ALL)
            print(Fore.WHITE + "1. Modo1")
            print("2. Modo2" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.modoOne()
                break
            elif entrada  == '2':
                self.modoTwo()
            else:
                break

    def modoTwo(self):
        patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"
        bandera = True
        while bandera:
            os.system("cls")
            print("Ingresa tu transicion: ")
            contador = True
            while contador:
                print("Ingrese los terminales")
                print(">>", end="")
                entrada = input()
                entrada = entrada.replace("[","").replace("]","")
                entrada = re.findall(patron, entrada)
                for x in entrada:
                    if(self.verificarTerminales(x) == False):
                        contador = False
                        break
                
                if contador == False:
                    print(Fore.RED + "Terminales no validos!" + Style.RESET_ALL)
                    input()
                    contador = True
                else:
                    print(Fore.GREEN + "Aceptado!" + Style.RESET_ALL)
                    contador = False 

            contador = True
            while contador:
                print("Ingrese los no terminales")
                print(">>", end="")
                entrada1 = input()
                entrada1 = entrada1.replace("[","").replace("]","")
                entrada1 = re.findall(patron, entrada1)
                for x in entrada1:
                    if(self.verificarNoTerminales(x) == False):
                        contador = False
                        break
                
                if contador == False:
                    print(Fore.RED + "No Terminales no validos!" + Style.RESET_ALL)
                    input()
                    contador = True
                else:
                    print(Fore.GREEN + "Aceptado!" + Style.RESET_ALL)
                    contador = False 
            
            contador = True
            while contador:
                print("Ingrese los simbolos destino:")
                print(">>", end="")
                entrada2 = input()
                entrada2 = entrada2.replace("[","").replace("]","")
                entrada2 = re.findall(patron, entrada2)
                for x in entrada2:
                    if (x == "-"):
                        continue 
                    if(self.verificarNoTerminales(x) == False):
                        contador = False
                        break
                
                if contador == False:
                    print(Fore.RED + "Simbolos destinos validos!" + Style.RESET_ALL)
                    input()
                    contador = True
                else:
                    print(Fore.GREEN + "Aceptado!" + Style.RESET_ALL)
                    contador = False
                    bandera = False 
                    #print("entrada" +  str(entrada))
                    #print("entrada1" +  str(entrada1))
                    #print("entrada2" +  str(entrada2))
                    input()

        #while
        iteracion = len(str(entrada))
        contador = 1
        #for i in entrada1: ## No terminales
        while True: 
            if entrada2:
                for i in entrada1:
                    for j in entrada: ## terminales
                        cadena = str(i)+","+str(entrada2.pop(0))+";"+str(j) 
                        self.arrayTransicion.append(cadena)
                        #print("cadena: " + cadena)
                        #input()
                    
            else:
                break
            contador +=1
            



    def verificarTerminales(self, terminal): ##Metodo para validar si existe el alfabeto
        if (len(self.arrayAlfabeto) == 0):
            return False
        for e in self.arrayAlfabeto:
            if terminal == e:
                return True
        return False

    def verificarNoTerminales(self, noTerminal): ##Metodo para validar si existe los estados
        if (len(self.arrayEstado) == 0):
            return False
        for a in self.arrayEstado:
            if noTerminal == a:
                return True
        return False

    def modoOne(self):
        bandera = True
        while bandera:
            os.system("cls")
            print("Ingresa tu transicion")
            print(">>", end="")
            entrada = input()
            
            if (self.verificarTransicion(entrada)):
                self.arrayTransicion.append(entrada)
            else:
                print(Fore.RED + "Transicion no valida!" + Style.RESET_ALL)
            
            print(Fore.YELLOW + "Desea ingresar otra transicion s/n?" + Style.RESET_ALL)
            entrada = input()
            if entrada == 's':
                bandera = True
            else:
                bandera = False

    def verificarTransicion(self, cadena):
        patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"

        estados = re.findall(patron, cadena)
        print(estados)
        bandera = True

        try:
            x = estados.pop(0)
            y = estados.pop(0)
            z = estados.pop(0)
        except IndexError:
            print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
            return False

        # SI  el metodo estadoRepetido o 
        # simboloRepetido RETORNA TRUE eñ ESTADO o el alfabeto no existen.
        print("R: " + str(x) + str(y) + str(z) )
        if ((self.estadoRepetido(str(x)) == True)):
            bandera = False
        if ((self.estadoRepetido(str(y)) == True)):
            bandera = False
        if ((self.simboloRepetido(str(z)) == True)):
            bandera = False

        return bandera


    def estadoAceptacionExiste(self): #recibe el estado que va ser de aceptacion
        contador = True
        if (len(self.arrayEstado)) != 0:
            os.system("cls")
            print("Ingrese el estado de aceptacion")
            print(">>", end="")
            dato = input()
            bandera = True
            while bandera: 
                for e in self.arrayEstado:
                    if(dato == e):
                        self.arrayAceptacion.append(dato)
                        contador = False
                        print('Estado de Aceptacion: ' + dato)
                        print(Fore.YELLOW + "Desea seguir ingresando estado de aceptacion s/n ?"+ Style.RESET_ALL)
                        print(">>", end="")
                        entrada = input()
                        if(entrada == 's'):
                            bandera = True
                        else:
                            bandera = False
                if contador == True:
                    print(Fore.RED + "El estado no existe!" + Style.RESET_ALL)
                    input()
                    bandera = False
        else: 
            print(Fore.RED + "Porfavor ingrese estados" + Style.RESET_ALL)
            input()

    def estadoInicialExiste(self): #recibe el estado inicial
        contador = True
        if (len(self.arrayEstado)) != 0:
            os.system("cls")
            print("Ingrese el estado inicial")
            print(">>", end="")
            dato = input()
            for e in self.arrayEstado:
                if(dato == e):
                    self.estadoIncial = dato
                    contador = False
                    print('Estado inicial: ' + self.estadoIncial)   
                    input()
            if contador == True:
                print(Fore.RED + "El estado no existe!" + Style.RESET_ALL)
                input()
        else: 
            print(Fore.RED + "Porfavor ingrese estados" + Style.RESET_ALL)
            input()

    
    def estado(self):
        contador = True
        while (contador):
            os.system("cls")
            print("Ingresar estados")
            print(">>", end="")
            dato = input()
            if(self.estadoRepetido(dato) and self.simboloRepetido(dato)):
                self.arrayEstado.append(dato)
                print(Fore.YELLOW + "Desea seguir ingresando estados s/n ?"+ Style.RESET_ALL)
                dato = input()
                if (dato == 's'):
                    contador = True
                else:
                    contador = False
            else:
                print(Fore.RED + " \"" + dato +  "\" Estado ya existe!" + Style.RESET_ALL)
                input()

    def alfabeto(self): #simbolos
        contador = True
        while (contador):
            os.system("cls")
            print("Ingresar simbolos")
            print(">>", end="")
            dato = input()
            if(self.estadoRepetido(dato) and self.simboloRepetido(dato)):
                self.arrayAlfabeto.append(dato)
                print(Fore.YELLOW + "Desea seguir ingresando estados s/n ?"+ Style.RESET_ALL)
                dato = input()
                if (dato == 's'):
                    contador = True
                else:
                    contador = False
            else:
                print(Fore.RED + " \"" + dato +  "\" Simbolo ya existe!" + Style.RESET_ALL)
                input()
   
    def simboloRepetido(self, estado):  #Alfabeto
        if (len(self.arrayAlfabeto) == 0):
            return True
        for e in self.arrayAlfabeto:
            if estado == e:
                return False
        return True


    def estadoRepetido(self, valor):
        if (len(self.arrayEstado) == 0):
            return True
        for a in self.arrayEstado:
            if valor == a:
                return False
        return True


    # De arhivo cargado
    def modificar(self, nombre, arrayE, arrayA, estadoI, arrayAcep, arrayTran):
        self.nombreAFD = nombre
        self.arrayEstado = arrayE
        self.arrayAlfabeto = arrayA
        self.estadoIncial = estadoI
        self.arrayAceptacion = arrayAcep
        self.arrayTransicion = arrayTran

        self.menuAFD2(nombre)

    def menuAFD2(self, nombre):
        self.nombreAFD = nombre
        while True:
            os.system("cls")   
            print(Fore.YELLOW + "Modificar: " + Style.RESET_ALL) 
            print(Fore.WHITE + "1. Ingresar estados")
            print("2. ingresar Alfabeto")
            print("3. Estado inicial")
            print("4. Estado de aceptacion")
            print("5. Transiciones")
            print("6. Ayuda" + Style.RESET_ALL)
            print(">>", end="")
            entrada = input()
            if entrada == '1':
                self.estado()
            elif entrada == '2':
                self.alfabeto()
            elif entrada == '3':
                self.estadoInicialExiste()
            elif entrada == '4':
                self.estadoAceptacionExiste()
            elif entrada == '5':
                self.menuModos()
            elif entrada == '8':
                self.generarAFD()
            elif entrada == '9':
                self.controlador.printArreglo()
            elif entrada == '6':
                print("Lenguajes formales B+")
                print("Jóse Véliz")
                print("0")
            elif entrada.lower() == 'salir':
                if len(self.arrayAceptacion) != 0:
                    self.controlador.crearAFD(self.nombreAFD, self.arrayEstado,
                        self.arrayAlfabeto, self.estadoIncial, self.arrayAceptacion,
                        self.arrayTransicion)
                    self.arrayEstado = []
                    self.arrayAlfabeto = []
                    self.arrayAceptacion = []
                    self.arrayTransicion = []
                    
                    break
                else:
                    print(Fore.RED +"Al menos tienes que ingresar un estado de aceptacion!!" + Style.RESET_ALL)
                    input()
