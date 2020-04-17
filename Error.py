from colorama import Fore, Style

class Error:

    __instancia = None

    def __new__(self):
        if not self.__instancia:
            self.__instancia = super(Error, self).__new__(self)
        return self.__instancia   


    def __init__(self):
        pass

    def mensaje(self, mensaje):
        print(Fore.RED + "✘ " + mensaje + Style.RESET_ALL)