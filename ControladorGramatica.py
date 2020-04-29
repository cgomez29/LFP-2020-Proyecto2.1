from bean.Gramatica import Gramatica

class ControladorGramatica(object):
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(ControladorGramatica, self).__new__(self)
        return self.__instancia
    
    def __init__(self):
        self.__arregloGramatica = [] #Arreglo de afd creados
        ant = []
        t = []
        inicial = ""
        producci = []

        ant.append("i") 
        ant.append("P") 
        ant.append("q") 
        ant.append("f")
        t.append("a") 
        t.append("b") 
        inicial = "S" 
        producci.append("S > a S b")
        producci.append("S > epsilon")
        #producci.append("S > ab")

        self.crearGramatica("q", ant, t, inicial, producci)




    def crearGramatica(self, nombreGramatica, arrayNT, arrayT,
        nTInicial, producciones):
        obj_Gramatica = Gramatica()
        
        obj_Gramatica.set_NombreGramatica(nombreGramatica)
        obj_Gramatica.set_ArrayNT(arrayNT)
        obj_Gramatica.set_ArrayT(arrayT)
        obj_Gramatica.set_NTInicial(nTInicial)
        obj_Gramatica.set_ArrayProduccion(producciones)
        self.__arregloGramatica.append(obj_Gramatica)


    def printArreglo(self):
        print(self.__arregloGramatica)

    #Retorna el objeto gramatica si existe la gramatica
    def buscarGramatica(self, nombre):
        #print("Tamaño: " + str(len(self.__arregloGramatica)))
        for g in self.__arregloGramatica:
            if nombre == g.get_NombreGramatica():
                return g 
        return None

    def nombreGramaticaRepetido(self, nombreGramatica):
        #print("Tamaño: " + str(len(self.__arregloGramatica)))
        if(len(self.__arregloGramatica)) == 0:
            return True
        for e in self.__arregloGramatica:
            if nombreGramatica == e.get_NombreGramatica():
                return False
        return True


    def llenarCadenas(self, nombre, valuadas):
        for x in self.__arregloGramatica:
            if nombre == x.get_NombreGramatica():
                array = x.get_CadenasEvaluadas()
                array.append(valuadas)
                x.set_CadenasEvaluadas(array)

    def llenarInvalidas(self, nombre, invalidas):
        for x in self.__arregloGramatica:
            if nombre == x.get_NombreGramatica():
                array = x.get_CadenasInvalidas()
                array.append(invalidas)
                x.set_CadenasInvalidas(array)

    def llenarValidas(self, nombre, validas):
        for x in self.__arregloGramatica:
            if nombre == x.get_NombreGramatica():
                array = x.get_CadenasValidas()
                array.append(validas)
                x.set_CadenasValidas(array)
