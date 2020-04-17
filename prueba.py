import easygui
import os


ruta =  str(easygui.fileopenbox(title="Abrir AFD", filetypes=[["* .afd", "AFD files"]] , default='*.afd'))

name = os.path.split(ruta)
name = name[1]
name = name.split(".")


print(name[0])            




while True:
    if(self.controlador.nombreAfdRepetido(nombre)):
        self.nombreAFD = nombre[0]
        break
                else:
                    print(Fore.RED + " \"" + nombre +  "\" Nombre ya existe!" + Style.RESET_ALL)
                    print(Fore.RED + " \"" + "Cambie el nombre de su archivo!! " + Style.RESET_ALL)
                    input()
                    break
            