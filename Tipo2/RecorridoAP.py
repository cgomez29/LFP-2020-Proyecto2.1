from colorama import Fore, Style
from Tipo2.Pila import Pila
import re

class RecorridoAP:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nodos = [] 
        self.nodos_aceptacion = []
        self.pila = Pila()
        self.contador2 = 0

    def agregarNodo(self, nodo):
        self.nodos.append(nodo)

    def obtenerNodo(self, nombre):
        for n in self.nodos:
            if n.nombre == nombre:
                return n

    def setearNodoAceptacion(self, nombre):
        self.nodos_aceptacion.append(self.obtenerNodo(nombre))

    def esAceptacion(self, nombre):
        for n in self.nodos_aceptacion:
            if n.nombre == nombre:
                return True
        
        return False

    def setEstadoInicial(self, nombre):
        self.obtenerNodo(nombre).inicial = True
    
    def getEstadoInicial(self):
        for n in self.nodos:
            if n.inicial:
                return n
        
        return None


    def validar(self, entrada):
        ruta = ""
        estadoSiguiente = self.getEstadoInicial().nombre
        contador = 0  
        estadoActual = ""
        tamanoCadena = len(entrada)
        
        print(Fore.RED + "ENTRADA: " + entrada + Style.RESET_ALL)
        
        for n in self.nodos:
            print(Fore.CYAN + "-------------------------------------------- "+ Style.RESET_ALL)
            print(Fore.BLUE + "nodo: " + n.nombre + Style.RESET_ALL)
            
            for x in entrada:
                
                for a in n.lista_aristas:    
                    
                    ##print(Fore.CYAN + "aristaCompleta: " + a.valor + Style.RESET_ALL)
                    if n.nombre == estadoSiguiente:
                        try:
                            dato = str(a.valor).replace(";", ",").split(",")
                            ##print(Fore.WHITE + "prueba: " + dato)
                            if entrada[contador] == dato[0]:
                                self.pila.printPila()
                            
                                print(Fore.GREEN + "entrada: " + entrada[contador] + Style.RESET_ALL)
                                print(Fore.GREEN + "leo: : " + dato[0] + Style.RESET_ALL)
                                print(Fore.GREEN + "Pop: : " + dato[1] + Style.RESET_ALL)
                                print(Fore.GREEN + "push: " + dato[2] + Style.RESET_ALL)
                                
                                ## Para los primeros 2
                                if self.esLambda(entrada[contador]) and self.esLambda(dato[1]):
                                   self.pila.push(dato[2])
                                
                                ## seteo de las SS
                                patron = "[a-z]|[A-Z]"
                                if self.esLambda(entrada[contador]) and self.esLambda(dato[1]) == False:
                                    self.pila.pop()
                                    x = re.findall(patron, dato[2])
                                    for w in reversed(x):
                                        self.pila.push(w)


                                
                                ##Realizaso el paso 3
                                if self.esLambda(entrada[contador]) == False and self.esLambda(dato[1]) == False:
                                    print("Estoy aqui1")
                                    print(Fore.MAGENTA + "entrada: " + entrada[contador] + Style.RESET_ALL)
                                    print(Fore.MAGENTA + "leo: : " + dato[0] + Style.RESET_ALL)
                                    print(Fore.MAGENTA + "Pop: : " + dato[1] + Style.RESET_ALL)
                                    print(Fore.MAGENTA + "push: " + dato[2] + Style.RESET_ALL)
                                    if entrada[contador] == self.pila.inspeccionar():
                                        print("Estoy aqui2")
                                        self.pila.pop()
                                    else:
                                        arista = self.buscarArista(n.lista_aristas, self.pila.inspeccionar())
                                        if (arista != None):
                                            self.pila.pop()
                                            x = re.findall(patron, dato[2])
                                            for w in reversed(x):
                                                self.pila.push(w)
                                            contador -=1

                                estadoSiguiente = a.nodo_final.nombre
                                #estadoActual = n.nombre
                                contador +=1
                                continue

                            
            
                        except IndexError as x:
                            #print(Fore.WHITE + "----------------CATH-------------------- "+ Style.RESET_ALL)
                            break

        contador +=1

        if contador == tamanoCadena and self.pila.inspeccionar() == "#":
            print(Fore.GREEN + "Cadena valida!!!!" + Style.RESET_ALL)
            print(Fore.MAGENTA + "Estado actural: " + estadoActual + Style.RESET_ALL)
            input()
        else:
            print(Fore.RED + "Cadena no valida!!!!" + Style.RESET_ALL)
            input()

        #self.pila.printPila()        
        #print("tamano: "  + str(contador))       
        #print("contador: " + str(tamanoCadena))       
        input()

    def buscarArista(self, arrayArista, buscar):
        count = 0 
        for x in arrayArista:
            y = str(x.valor).replace(";", ",").split(",")
            if buscar == y[1]:
                return y[2]
            count +=1

        return None

    def esLambda(self, valor): ## El metodo dice, Es lambda??
        if valor == "λ":
            return True
        return False
