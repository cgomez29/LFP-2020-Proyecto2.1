from bean.AFD import AFD

class ControladorAFD(object):
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(ControladorAFD, self).__new__(self)
        return self.__instancia
    
    def __init__(self):
        self.__arregloAFD = [] #Arreglo de afd creados



    def crearAFD(self, nombreAfd, arrayEstado, arrayAlfabeto,
        estadoInicial, arrayAceptacion, arrayTransicion):
        
        obj_AFD = AFD()

        obj_AFD.set_NombreAfd(nombreAfd)
        obj_AFD.set_ArrayEstado(arrayEstado)
        obj_AFD.set_ArrayAlfabeto(arrayAlfabeto)
        obj_AFD.set_EstadoInicial(estadoInicial)
        obj_AFD.set_ArrayAceptacion(arrayAceptacion)
        obj_AFD.set_ArrayTransicion(arrayTransicion)
        self.__arregloAFD.append(obj_AFD)


    def printArreglo(self):
        print(self.__arregloAFD)

    #Retorna el objeto AFD, si existe el AFD
    def buscarAFD(self, nombre):
        for afd in self.__arregloAFD:
            if nombre == afd.get_NombreAfd():
                return afd
        return None

    def nombreAfdRepetido(self, nombreAfd):
        if (len(self.__arregloAFD) == 0):
            return True
        for e in self.__arregloAFD:
            if nombreAfd == e.get_NombreAfd():
                return False
        return True


    def llenarCadenas(self, nombre, valuadas):
        for x in self.__arregloAFD:
            if nombre == x.get_NombreAfd():
                array = x.get_CadenasEvaluadas()
                array.append(valuadas)
                x.set_CadenasEvaluadas(array)

    def llenarInvalidas(self, nombre, invalidas):
        for x in self.__arregloAFD:
            if nombre == x.get_NombreAfd():
                array = x.get_CadenasInvalidas()
                array.append(invalidas)
                x.set_CadenasInvalidas(array)

    def llenarValidas(self, nombre, validas):
        for x in self.__arregloAFD:
            if nombre == x.get_NombreAfd():
                array = x.get_CadenasValidas()
                array.append(validas)
                x.set_CadenasValidas(array)
