import string
import pandas
from pyparsing import col


class AlgoritmoNoRecursivo:
    def __init__(self, direccion, reglaInicial):
        matriz = pandas.read_csv(direccion, header=0)
        self.matriz = matriz
        self.reglas = self.matriz["regla"].to_list()
        self.pila = []
        self.pila.append("$")
        self.pila.append(reglaInicial)
        self.buscarReglaExisitente("NO", "")

        pass

    def ejecutarAlgoritmo(self):
        pass

    def _sustituirLegible(self, simbolo):
        if string.ascii_lowercase.__contains__(simbolo):
            return "a...z"
        if string.ascii_uppercase.__contains__(simbolo):
            return "A...Z"
        if str.isdigit(simbolo):
            return "0...9"
        return simbolo

    def buscarReglaExisitente(self, regla, simboloBuscar):
        simboloBuscar = self._sustituirLegible(simboloBuscar)
        indexBusqueda = self.reglas.index(regla)
        nuevaRegla = ""
        for columna in self.matriz:
            if columna != "regla":
                print(columna)
                # print(self.matriz[columna][indexBusqueda])
                if columna == simboloBuscar:
                    if self.matriz[columna][indexBusqueda] != "-1":
                        nuevaRegla = self.matriz[columna][indexBusqueda]
                        print("ENCONTRADO")

        if nuevaRegla == "":
            print("no hay conincidencias")
            return False
        else:
            print(f"se encontro conicidencia con la regla {nuevaRegla}")
        return nuevaRegla


AlgoritmoNoRecursivo("cssvs/identificador.csv", "P")
# AlgoritmoNoRecursivo("cssvs\whiles.csv", "P")
