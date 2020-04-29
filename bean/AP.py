class AP:
    
    def __init__(self):
        self.nombre = ""
        self.estados = []
        self.alfabeto = []
        self.simbolos = []
        self.transicion = []
        self.estadoInicial = ""
        self.estadosAceptacion = []

    def get_Nombre(self):
        return self.nombre

    def set_Nombre(self, x):
        self.nombre = x

    def get_Estados(self):
        return self.estados

    def set_Estados(self, x):
        self.estados = x

    def get_Alfabeto(self):
        return self.alfabeto

    def set_Alfabeto(self, x):
        self.alfabeto = x

    def get_Simbolos(self):
        return self.simbolos

    def set_Simbolos(self, x):
        self.simbolos = x

    def get_Transicion(self):
        return self.transicion

    def set_Transicion(self, x):
        self.transicion = x

    def get_EstadoInicial(self):
        return self.estadoInicial

    def set_EstadoInicial(self, x):
        self.estadoInicial = x

    def get_EstadoAcetacion(self):
        return self.estadosAceptacion

    def set_EstadoAcetacion(self, x):
        self.estadosAceptacion = x

