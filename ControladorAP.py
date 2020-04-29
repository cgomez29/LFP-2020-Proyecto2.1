from bean.AP import AP

class ControladorAP(object):
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(ControladorAP, self).__new__(self)
        return self.__instancia
    
    def __init__(self):
        self.__arregloAP = [] #Arreglo de AP creados

    def crearAP(self, nombre ,estados, alfabeto, simbolos,
        estadoInicial, estadosAceptacion, transiciones):


        if self.buscarAP(nombre) == None:
            obj_AP = AP()

            obj_AP.set_Nombre(nombre)
            obj_AP.set_Estados(estados)
            obj_AP.set_Alfabeto(alfabeto)
            obj_AP.set_Simbolos(simbolos)
            obj_AP.set_Transicion(transiciones)
            obj_AP.set_EstadoInicial(estadoInicial)
            obj_AP.set_EstadoAcetacion(estadosAceptacion)
            self.__arregloAP.append(obj_AP)
        else:
            for x in self.__arregloAP:
                x.set_Estados(estados)
                x.set_Alfabeto(alfabeto)
                x.set_Simbolos(simbolos)
                x.set_Transicion(transiciones)
                x.set_EstadoInicial(estadoInicial)
                x.set_EstadoAcetacion(estadosAceptacion)


    #Retorna el objeto AP, si existe el AP
    def buscarAP(self, nombre):
        for ap in self.__arregloAP:
            if nombre == ap.get_Nombre():
                return ap
        return None

    
