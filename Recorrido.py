from colorama import Fore, Style

class Recorrido:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nodos = [] 
        self.nodos_aceptacion = []


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
        for n in self.nodos:
            for x in entrada:
                for a in n.lista_aristas:
                    if n.nombre == estadoSiguiente:
                        #if x == a.valor:
                        try:
                            if entrada[contador] == a.valor:
                                #ruta = ruta + str(n.nombre)+","+str(a.nodo_final.nombre)+","+str(a.valor)+"; "
                                estadoSiguiente = a.nodo_final.nombre
                                estadoActual = n.nombre
                                #print(ruta)
                                contador +=1
                                break
                        except IndexError as x:
                            pass

        
        if  self.esAceptacion(estadoSiguiente):
            print(Fore.GREEN + "Cadena valida!!!!" + Style.RESET_ALL)
            input()
            return True
        else:
            print(Fore.RED + "Cadena NO valida!!!!" + Style.RESET_ALL)
            input()
            return False



    def verificar(self, entrada):
        ruta = ""
        estadoSiguiente = self.getEstadoInicial().nombre
        estadoActual = ""
        contador = 0  
        for n in self.nodos:
            for x in entrada:
                for a in n.lista_aristas:
                    if n.nombre == estadoSiguiente:
                        #if x == a.valor:
                        try:
                            if entrada[contador] == a.valor:
                                ruta = ruta + str(n.nombre)+","+str(a.nodo_final.nombre)+","+str(a.valor)+"; "
                                estadoSiguiente = a.nodo_final.nombre
                                estadoActual = n.nombre
                                #print(ruta)
                                contador +=1
                                break
                        except IndexError as x:
                            pass

        
        if  self.esAceptacion(estadoSiguiente):
            tamano = len(ruta)
            ruta = ruta[0 : tamano - 2]
            print(Fore.YELLOW + "Ruta: " + ruta + Style.RESET_ALL)
            print(Fore.GREEN + "Cadena valida!!!!" + Style.RESET_ALL)
            input()
            return True
        else:
            print(Fore.RED + "Cadena NO valida!!!!" + Style.RESET_ALL)
            input()
            return False
                    
                            



    
