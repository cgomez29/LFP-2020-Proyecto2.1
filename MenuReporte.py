import os
import re
import easygui as eg

from colorama import Fore, Style
from ControladorGramatica import ControladorGramatica
from ControladorAFD import ControladorAFD
from AFD import AFD
from Grafo import Grafo

# Importaciones para crear PDF
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class MenuReporte(object):
    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(MenuReporte, self).__new__(self)
        return self.__instancia
        
    def __init__(self):
        self.__controladorGramatica = ControladorGramatica()
        self.__controladorAFD = ControladorAFD()
        self.__obj = None #Podra ser de tipo AFD o de Tipo Gramatica
        self.__tipo = ""
        self.__grafo = Grafo("G1")
        self.__arrayNT2 = []
        self.__arrayT2 = [] 
        self.__recurIzq = True 

    def menuReporte(self):
        contador  = True
        bandera = True
        while (contador):
            os.system("cls")
            print("Ingresa el nombre de la Gramatica o AFD a utilizar:")
            print(">>", end="")
            nombre = input()
            objGram = self.__controladorGramatica.buscarGramatica(nombre) 
            objAFD = self.__controladorAFD.buscarAFD(nombre) 

            if (nombre.lower() == "salir"):
                bandera = False
                break

            if ((objGram) != None):
                self.__tipo = "Gramatica"                
                self.__obj = objGram 
                contador = False
            elif ((objAFD) != None):
                self.__tipo = "AFD"
                self.__obj = objAFD
                contador = False
            
            else: 
                print(Fore.RED + "La Gramatica o AFD: \"" + nombre +  "\" No existe! " + Style.RESET_ALL)
                input()
                contador = True

        while bandera:
            os.system("cls")
            print(Fore.YELLOW + self.__tipo + ": " + nombre + Style.RESET_ALL)
            print(Fore.WHITE + "1. Ver detalle")
            print("2. Generar Reporte")        
            print("3. Ayuda" + Style.RESET_ALL)        
            print(">>", end="")
            entrada = input()
            if entrada == "1":
                self.verDetalle()
            elif(entrada == "2"):
                self.generarReporte()
            elif(entrada == "3"):
                print("Lenguajes formales B+")
                print("Jóse Véliz")
                print("0")
                input()
            elif entrada.lower() == "salir":
                break


    def verDetalle(self):
        #__obj puede ser de tipo AFD o Gramatica
        if self.__tipo == 'AFD':
            print(Fore.LIGHTMAGENTA_EX + "Alfabeto" + Style.RESET_ALL)
            for x in self.__obj.get_ArrayAlfabeto():
                print(Fore.LIGHTGREEN_EX + str(x) + Style.RESET_ALL)

            print(Fore.LIGHTMAGENTA_EX + "Estados" + Style.RESET_ALL)
            for a in self.__obj.get_ArrayEstado():
                print(Fore.LIGHTGREEN_EX + str(a) + Style.RESET_ALL)            
            
            print(Fore.LIGHTMAGENTA_EX + "Estado inicial" + Style.RESET_ALL)            
            print(Fore.LIGHTGREEN_EX + str(self.__obj.get_EstadoInicial()) + Style.RESET_ALL)            
            
            print(Fore.LIGHTMAGENTA_EX + "Estados de aceptacion" + Style.RESET_ALL)            
            for w in self.__obj.get_ArrayAceptacion():
                print(Fore.LIGHTGREEN_EX + str(w) + Style.RESET_ALL)

            print(Fore.LIGHTMAGENTA_EX + "Transiciones" + Style.RESET_ALL)            
            for e in self.__obj.get_ArrayTransicion():
                print(Fore.LIGHTGREEN_EX + str(e) + Style.RESET_ALL)

            input()
            ## cambiar la variable estad de aceptacion por un arreglo
        else:
            print(Fore.LIGHTMAGENTA_EX + "No terminales" + Style.RESET_ALL)   
            for x in self.__obj.get_ArrayNT():
                print(Fore.LIGHTGREEN_EX + str(x) + Style.RESET_ALL)

            print(Fore.LIGHTMAGENTA_EX + "Terminales" + Style.RESET_ALL)
            for x in self.__obj.get_ArrayT():
                print(Fore.LIGHTGREEN_EX + str(x) + Style.RESET_ALL)

            print(Fore.LIGHTMAGENTA_EX + "Inicio" + Style.RESET_ALL)
            print(Fore.LIGHTGREEN_EX + str(self.__obj.get_NTInicial()) + Style.RESET_ALL)

            print(Fore.LIGHTMAGENTA_EX + "Producciones" + Style.RESET_ALL)            
            for x in self.__obj.get_ArrayProduccion():
                print(Fore.LIGHTGREEN_EX + str(x) + Style.RESET_ALL)
            
            input()
            

    def generarReporte(self):
        if self.__tipo == 'AFD':
            self.__grafo = Grafo('g1')

            for x in self.__obj.get_ArrayEstado():
                self.__grafo.agregarNodo(Nodo(x))

            # Trancisiones
            patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"


            for i in self.__obj.get_ArrayTransicion():
                estados = re.findall(patron, i)
                try:
                    x = estados.pop(0)
                    y = estados.pop(0)
                    z = estados.pop(0)
                    if y != "-":
                        self.__grafo.obtenerNodo(x).crearArista(self.__grafo.obtenerNodo(y), z)
                except IndexError:
                    print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
                    input()    
            
            # Estado Incial
            self.__grafo.setEstadoInicial(self.__obj.get_EstadoInicial())

            # Estado de aceptacion
            for x in self.__obj.get_ArrayAceptacion():
                self.__grafo.setearNodoAceptacion(x)

            
            self.__grafo.graficar()



            extension = ["*.pdf"]
            archivo = eg.filesavebox(msg="Guardar archivo",
                            title="Control: filesavebox",
                            default="Reporte.pdf",
                            filetypes=extension)
                # Ubicacion del arhivo a crear
            ruta = str(archivo)
            
            Story = []
            logotipo = "x.gv.png"
            doc = SimpleDocTemplate(ruta, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

            imagen = Image(logotipo, 7 * inch, 3 * inch, hAlign='CENTER', mask="auto")
            Story.append(imagen)
            estilos = getSampleStyleSheet()
            estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            
            texto = "AFD: "
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 8))

            texto = "Alfabeto"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 6))
            for x in self.__obj.get_ArrayAlfabeto():
                Story.append(Paragraph(str(x), estilos["Normal"]))
                Story.append(Spacer(1, 4))

            texto = "Estados"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 6))
            for a in self.__obj.get_ArrayEstado():
                Story.append(Paragraph(str(a), estilos["Normal"]))
                Story.append(Spacer(1, 4))

            texto = "Estado inicial"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 12))
            Story.append(Paragraph(str(self.__obj.get_EstadoInicial()), estilos["Normal"]))
            Story.append(Spacer(1, 4))

            texto = "Estados de aceptacion"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 6))
            for w in self.__obj.get_ArrayAceptacion():
                Story.append(Paragraph(str(w), estilos["Normal"]))
                Story.append(Spacer(1, 4))

            texto = "Transiciones"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 6))
            for e in self.__obj.get_ArrayTransicion():
                Story.append(Paragraph(str(e), estilos["Normal"]))
                Story.append(Spacer(1, 4))

            texto = "Cadenas evaluadas"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 8))
            for e in self.__obj.get_CadenasValidas():
                Story.append(Paragraph(str(e) + " Valida", estilos["Normal"]))
                Story.append(Spacer(1, 4))
            for e in self.__obj.get_CadenasInvalidas():
                Story.append(Paragraph(str(e) + " Invalida", estilos["Normal"]))
                Story.append(Spacer(1, 4))

            texto = "Cadenas Validas"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 8))
            for e in self.__obj.get_CadenasValidas():
                Story.append(Paragraph(str(e), estilos["Normal"]))
                Story.append(Spacer(1, 4))
            
            texto = "Cadenas Invalidas"           
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 8))
            for e in self.__obj.get_CadenasInvalidas():
                Story.append(Paragraph(str(e), estilos["Normal"]))
                Story.append(Spacer(1, 4))

            texto = 'Cristian Gomez - 201801480'
            Story.append(Paragraph(texto, estilos["Normal"]))
            Story.append(Spacer(1, 14))
            doc.build(Story)
            os.system(ruta)
        else:
            self.__grafo = Grafo('g1')
            objAFD = self.convertirGramatica(self.__obj)
            if (self.__recurIzq):
                for x in objAFD.get_ArrayEstado():
                    self.__grafo.agregarNodo(Nodo(x))

                # Trancisiones
                patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"


                for i in objAFD.get_ArrayTransicion():
                    estados = re.findall(patron, i)
                    try:
                        x = estados.pop(0)
                        y = estados.pop(0)
                        z = estados.pop(0)
                    except IndexError:
                        print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
                    
                    self.__grafo.obtenerNodo(x).crearArista(self.__grafo.obtenerNodo(y), z)
                
                # Estado Incial
                self.__grafo.setEstadoInicial(objAFD.get_EstadoInicial())

                # Estado de aceptacion
                for x in objAFD.get_ArrayAceptacion():
                    self.__grafo.setearNodoAceptacion(x)

                
                self.__grafo.graficar()

                extension = ["*.pdf"]
                archivo = eg.filesavebox(msg="Guardar archivo",
                                title="Control: filesavebox",
                                default="Reporte.pdf",
                                filetypes=extension)
                    # Ubicacion del arhivo a crear
                ruta = str(archivo)
                
                Story = []
                logotipo = "x.gv.png"
                doc = SimpleDocTemplate(ruta, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
                imagen = Image(logotipo, 7 * inch, 3 * inch, hAlign='CENTER', mask="auto")
                Story.append(imagen)
                estilos = getSampleStyleSheet()
                estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

                ################################# AFD
                texto = "AFD: "
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 8))

                texto = "Alfabeto"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 6))
                for x in objAFD.get_ArrayAlfabeto():
                    Story.append(Paragraph(str(x), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                texto = "Estados"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 6))
                for a in objAFD.get_ArrayEstado():
                    Story.append(Paragraph(str(a), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                texto = "Estado inicial"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 12))
                Story.append(Paragraph(str(objAFD.get_EstadoInicial()), estilos["Normal"]))
                Story.append(Spacer(1, 4))

                texto = "Estados de aceptacion"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 6))
                for w in objAFD.get_ArrayAceptacion():
                    Story.append(Paragraph(str(w), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                texto = "Transiciones"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 6))
                for e in objAFD.get_ArrayTransicion():
                    Story.append(Paragraph(str(e), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                ################################# Gramatica
                texto = "Gramatica: "
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 8))

                texto = "No terminales"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 6))
                for x in self.__obj.get_ArrayNT():
                    Story.append(Paragraph(str(x), estilos["Normal"]))
                    Story.append(Spacer(1, 4))


                texto = "Terminales"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 6))
                for x in self.__obj.get_ArrayT():
                    Story.append(Paragraph(str(x), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                texto = "Inicio"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 12))
                Story.append(Paragraph(str(self.__obj.get_NTInicial()), estilos["Normal"]))
                Story.append(Spacer(1, 4))

                texto = "Cadenas evaluadas"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 8))
                for e in self.__obj.get_CadenasValidas():
                    Story.append(Paragraph(str(e) + " Valida", estilos["Normal"]))
                    Story.append(Spacer(1, 4))
                for e in self.__obj.get_CadenasInvalidas():
                    Story.append(Paragraph(str(e) + " Invalida", estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                texto = "Cadenas Validas"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 8))
                for e in self.__obj.get_CadenasValidas():
                    Story.append(Paragraph(str(e), estilos["Normal"]))
                    Story.append(Spacer(1, 4))
                
                texto = "Cadenas Invalidas"           
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 8))
                for e in self.__obj.get_CadenasInvalidas():
                    Story.append(Paragraph(str(e), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                
                texto = 'Cristian Gomez - 201801480'
                Story.append(Paragraph(texto, estilos["Normal"]))
                Story.append(Spacer(1, 14))
                doc.build(Story)
                os.system(ruta)
            else:
                #self.quitarRecurIzq(self.__obj)
                print(Fore.RED + "Recursiva por la izquierda" + Style.RESET_ALL)
                input()
                self.__grafo = Grafo('g1')
                objAFD = self.convertirGramatica(self.__obj)
                if (objAFD != None):
                    for x in objAFD.get_ArrayEstado():
                        self.__grafo.agregarNodo(Nodo(x))

                    # Trancisiones
                    patron = "[a-zA-Z0-9-]+|[a-zA-Z0-9-]"


                    for i in objAFD.get_ArrayTransicion():
                        estados = re.findall(patron, i)
                        try:
                            x = estados.pop(0)
                            y = estados.pop(0)
                            z = estados.pop(0)
                        except IndexError:
                            print(Fore.RED + "Cadena no valida!" + Style.RESET_ALL)
                        
                        self.__grafo.obtenerNodo(x).crearArista(self.__grafo.obtenerNodo(y), z)
                    
                    # Estado Incial
                    self.__grafo.setEstadoInicial(objAFD.get_EstadoInicial())

                    # Estado de aceptacion
                    for x in objAFD.get_ArrayAceptacion():
                        self.__grafo.setearNodoAceptacion(x)

                    
                    self.__grafo.graficar()

                    extension = ["*.pdf"]
                    archivo = eg.filesavebox(msg="Guardar archivo",
                                    title="Control: filesavebox",
                                    default="Reporte.pdf",
                                    filetypes=extension)
                        # Ubicacion del arhivo a crear
                    ruta = str(archivo)
                    
                    Story = []
                    logotipo = "x.gv.png"
                    doc = SimpleDocTemplate(ruta, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
                    imagen = Image(logotipo, 7 * inch, 3 * inch, hAlign='CENTER', mask="auto")
                    Story.append(imagen)
                    estilos = getSampleStyleSheet()
                    estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

                    ################################# AFD
                    texto = "AFD: "
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 8))

                    texto = "Alfabeto"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 6))
                    for x in objAFD.get_ArrayAlfabeto():
                        Story.append(Paragraph(str(x), estilos["Normal"]))
                        Story.append(Spacer(1, 4))

                    texto = "Estados"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 6))
                    for a in objAFD.get_ArrayEstado():
                        Story.append(Paragraph(str(a), estilos["Normal"]))
                        Story.append(Spacer(1, 4))

                    texto = "Estado inicial"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 12))
                    Story.append(Paragraph(str(objAFD.get_EstadoInicial()), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                    texto = "Estados de aceptacion"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 6))
                    for w in objAFD.get_ArrayAceptacion():
                        Story.append(Paragraph(str(w), estilos["Normal"]))
                        Story.append(Spacer(1, 4))

                    texto = "Transiciones"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 6))
                    for e in objAFD.get_ArrayTransicion():
                        Story.append(Paragraph(str(e), estilos["Normal"]))
                        Story.append(Spacer(1, 4))

                    ################################# Gramatica
                    texto = "Gramatica: "
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 8))

                    texto = "No terminales"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 6))
                    for x in self.__obj.get_ArrayNT():
                        Story.append(Paragraph(str(x), estilos["Normal"]))
                        Story.append(Spacer(1, 4))


                    texto = "Terminales"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 6))
                    for x in self.__obj.get_ArrayT():
                        Story.append(Paragraph(str(x), estilos["Normal"]))
                        Story.append(Spacer(1, 4))

                    texto = "Inicio"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 12))
                    Story.append(Paragraph(str(self.__obj.get_NTInicial()), estilos["Normal"]))
                    Story.append(Spacer(1, 4))

                    texto = "Cadenas evaluadas"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 8))
                    for e in self.__obj.get_CadenasValidas():
                        Story.append(Paragraph(str(e) + " Valida", estilos["Normal"]))
                        Story.append(Spacer(1, 4))
                    for e in self.__obj.get_CadenasInvalidas():
                        Story.append(Paragraph(str(e) + " Invalida", estilos["Normal"]))
                        Story.append(Spacer(1, 4))

                    texto = "Cadenas Validas"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 8))
                    for e in self.__obj.get_CadenasValidas():
                        Story.append(Paragraph(str(e), estilos["Normal"]))
                        Story.append(Spacer(1, 4))
                    
                    texto = "Cadenas Invalidas"           
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 8))
                    for e in self.__obj.get_CadenasInvalidas():
                        Story.append(Paragraph(str(e), estilos["Normal"]))
                        Story.append(Spacer(1, 4))

                    
                    texto = 'Cristian Gomez - 201801480'
                    Story.append(Paragraph(texto, estilos["Normal"]))
                    Story.append(Spacer(1, 14))
                    doc.build(Story)
                    os.system(ruta)


    def convertirGramatica(self, obj):
        objAfd = AFD()
        objAfd.set_ArrayEstado(obj.get_ArrayNT())
        objAfd.set_ArrayAlfabeto(obj.get_ArrayT())
        objAfd.set_EstadoInicial(obj.get_NTInicial())


        ### Ingresando las producciones
        ## para AFD: A,B;0
        ## para Gramatica, A > 0 B [a-d5-8]
        #patron = "[a-z]|[0-9]"
        patron = "[a-z]|[0-9]"
        patron2 = "[A-Z]"
        self.__recurIzq = True

        arrayTransiciones = []
        for x in obj.get_ArrayProduccion():
            if not ( "epsilon" in x):
                x = x.split(">")
                ## primer valor
                valor1 = x[0]

                valor2 = re.findall(patron2, x[1])

                valor3 = re.findall(patron, x[1])
                try:
                    transicion = str(valor1) + "," + str(valor2.pop(0)) + ";" + str(valor3.pop(0))
                except IndexError as x:
                    self.__recurIzq = False
                    break
                transicion = transicion.replace(" ", "")
                
                arrayTransiciones.append(transicion)

        objAfd.set_ArrayTransicion(arrayTransiciones)

        ## ingresando los estados de aceptacion
        arrayAceptacion = []
        for x in obj.get_ArrayProduccion():
            if ( "epsilon" in x):
                x = x.replace(" ", "").split(">")
                arrayAceptacion.append(x[0])

        objAfd.set_ArrayAceptacion(arrayAceptacion)

        return objAfd
        



    def quitarRecurIzq(self, gram): #gramtica
        patron3 = "+[A-Z]"
        producciones = gram.get_ArrayProduccion()
        arrayProduc = []
        contador = 0
        for x in producciones:
            z =  w = x
            x = x.replace(" ", "").split(">")                
            if contador == 0:   
                self.__arrayNT2.append(x[0])
                contador += 1
            else:
                if self.existeNt(x[0]):
                    self.__arrayNT2.append(x[0])

            w = w.split(">") 

            if not ( "epsilon" in w[1]):
                #terminales = re.findall(patron3, w[1])
                w[1] = w[1].replace(" ", "")
                print(w[1])
                terminales = re.findall(patron3, w[1])
                #terminales = w[1]

                print(str(terminales))


        gram.set_ArrayNT(self.__arrayNT2)
        gram.set_ArrayT(self.__arrayT2)
        gram.set_ArrayProduccion(arrayProduc)
        input()
        ##return gram 


    def existeNt(self, nterminal):
        for x in self.__arrayNT2:
            if (x == nterminal):
                return False
        return True

    def existeT(self, alfabeto):
        for x in self.__arrayT2:
            if (x == alfabeto):
                return False
        return True

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_aristas = []
        self.inicial = False

    def crearArista(self, nodo_final, valor):
        self.lista_aristas.append(Arista(self, nodo_final, valor))

class Arista:
    def __init__(self, inicial, final, valor):
            self.nodo_inicial = inicial
            self.nodo_final = final
            self.valor = valor