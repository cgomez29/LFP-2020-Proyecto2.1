class Gramatica:
    
    def __init__(self):
        self.__nombreGramatica = ""
        self.__arrayNT = []
        self.__arrayT = []
        self.__nTInicial = "" #guarda el nombre del no terminal inicial
        self.__producciones = []
        self.__cadenasEvaluadas = []
        self.__cadenasInvalidas = []
        self.__cadenasValidas = []
        self.__sinRecursividad = []
    
    def get_NombreGramatica(self):
        return self.__nombreGramatica

    def set_NombreGramatica(self, nombreGramatica):
        self.__nombreGramatica = nombreGramatica

    def get_ArrayNT(self):
        return self.__arrayNT

    def set_ArrayNT(self, arrayNT):
        self.__arrayNT = arrayNT

    def get_ArrayT(self):
        return self.__arrayT

    def set_ArrayT(self, arrayT):
        self.__arrayT = arrayT

    def get_NTInicial(self):
        return self.__nTInicial

    def set_NTInicial(self, nTinicial):
        self.__nTInicial = nTinicial

    def get_ArrayProduccion(self):
        return self.__producciones

    def set_ArrayProduccion(self, producciones):
        self.__producciones = producciones

    def get_CadenasEvaluadas(self):
        return self.__cadenasEvaluadas

    def set_CadenasEvaluadas(self, cadena):
        self.__cadenasEvaluadas = cadena

    def get_CadenasInvalidas(self):
        return self.__cadenasInvalidas

    def set_CadenasInvalidas(self, cadena):
        self.__cadenasInvalidas = cadena

    def get_CadenasValidas(self):
        return self.__cadenasValidas

    def set_CadenasValidas(self, cadena):
        self.__cadenasValidas = cadena

    def get_SinRecursividad(self):
        return self.__sinRecursividad

    def set_SinRecursividad(self, cadena):
        self.__sinRecursividad = cadena
    