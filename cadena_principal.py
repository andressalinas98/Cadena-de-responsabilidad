class Control:
    def __init__(self):
        self.__succesor__ = None

    def set_succesor(self, succesor):
        self.__succesor__ = succesor

    def handler_request(self, opt):
        pass

class Default(Control):
    def obtener_nombre(self):
        return "Default"
    def handler_request(self, opt):
        print("Opción no valida")