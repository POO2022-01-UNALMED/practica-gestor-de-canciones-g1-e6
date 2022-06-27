class UsuarioNoExiste(Exception):
    def __init__(self, nombre):
        super().__init__("el usuario {} no exixte".format(nombre))
        self._nombre = nombre
    def mostrar_mensaje(self):
        return ("no existe el usuario con nombre " + self._nombre)