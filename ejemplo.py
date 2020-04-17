from graphviz import Digraph

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_aristas = []

    def crearArista(self, nodo_final, valor):
        self.lista_aristas.append(Arista(self, nodo_final, valor))

class Arista:
    def __init__(self, inicial, final, valor):
            self.nodo_inicial = inicial
            self.nodo_final = final
            self.valor = valor


class Grafo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nodos = [] 
        self.nodos_aceptacion = []

    def agrergarNodo(self, nodo):
        self.nodos.append(nodo)

    def obtenerNodo(self, nombre):
        for n in self.nodos:
            if n.nombre == nombre:
                return n

    ####
    def setearNodoAceptacion(self, nombre):
        pass

    def graficar(self):
        f = Digraph(format='png', name="x")
        f.attr(rankdir='LR', size='8,5')
        f.attr('node', shape ='circle')

        for n in self.nodos:
            f.node(n.nombre)

        ## Transiciones
        for n in self.nodos:
            for a in n.lista_aristas:
                f.edge(n.nombre, a.nodo_final.nombre, label=a.valor)

        f.render()
nt = ['A', 'B','C','D', 'E']

grafo_prueba = Grafo('g1')

for x in nt:
    grafo_prueba.agrergarNodo(Nodo(x))


grafo_prueba.obtenerNodo('A').crearArista(grafo_prueba.obtenerNodo('B'), 'a')
grafo_prueba.obtenerNodo('A').crearArista(grafo_prueba.obtenerNodo('C'), 'b')
grafo_prueba.obtenerNodo('A').crearArista(grafo_prueba.obtenerNodo('A'), 'c')
grafo_prueba.obtenerNodo('B').crearArista(grafo_prueba.obtenerNodo('C'), 'a')
grafo_prueba.obtenerNodo('C').crearArista(grafo_prueba.obtenerNodo('D'), 'a')
grafo_prueba.obtenerNodo('D').crearArista(grafo_prueba.obtenerNodo('E'), 'b')

grafo_prueba.graficar()


##Crar Grafo