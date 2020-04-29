class AFD:
    
    def __init__(self):
        self.__nombreAfd = ''
        self.__arrayEstado = []
        self.__arrayAlfabeto = []
        self.__estadoIncial = ''
        self.__arrayEstadoAceptacion = []
        self.__arrayTransicion = []
        self.__cadenasEvaluadas = []
        self.__cadenasInvalidas = []
        self.__cadenasValidas = []

    def get_NombreAfd(self):
        return self.__nombreAfd

    def set_NombreAfd(self, nombreAfd):
        self.__nombreAfd = nombreAfd

    def get_ArrayEstado(self):
        return self.__arrayEstado

    def set_ArrayEstado(self, arrayEstado):
        self.__arrayEstado = arrayEstado

    def get_ArrayAlfabeto(self):
        return self.__arrayAlfabeto

    def set_ArrayAlfabeto(self, arrayAlfabeto):
        self.__arrayAlfabeto = arrayAlfabeto

    def get_EstadoInicial(self):
        return self.__estadoIncial

    def set_EstadoInicial(self, estadoInicial):
        self.__estadoIncial = estadoInicial

    def get_ArrayAceptacion(self):
        return self.__arrayEstadoAceptacion

    def set_ArrayAceptacion(self, array):
        self.__arrayEstadoAceptacion = array

    def get_ArrayTransicion(self):
        return self.__arrayTransicion

    def set_ArrayTransicion(self, arrayTransicion):
        self.__arrayTransicion = arrayTransicion

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