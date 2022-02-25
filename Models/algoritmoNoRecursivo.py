import pandas


class AlgoritmoNoRecursivo:
    def __init__(self, direccion, reglaInicial):
        matriz = pandas.read_csv(direccion, header=0)
        self.matriz = matriz
        self.pila = []
        self.pila.append("$")
        self.pila.append(reglaInicial)
        print(matriz)
        print(self.pila)
        pass

    # def _encontrar


# AlgoritmoNoRecursivo("cssvs\identificador.csv", "P")
# AlgoritmoNoRecursivo("cssvs\whiles.csv", "P")
