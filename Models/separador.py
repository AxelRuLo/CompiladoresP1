
from numpy import append


class separador:
    def __init__(self, cadena):
        self.cadena = cadena

    def _separarID(self):
        isString = False
        listaSeparados = []
        listaEliminar = []
        listaIgual = ["="]
        cadenaTratada = self.cadena
        cadenaTratada = cadenaTratada.split(" = ")

        if len(cadenaTratada) > 2 or len(cadenaTratada)<2:
            return False
        
        if(self.cadena.count("()")>1):
            return False
        if(self.cadena.count("[]")>1):
            return False        
        if(self.cadena.count("{}")>1):
            return False

        if (cadenaTratada[1][0] == "'"):
            isString=True
            cadenaTratada[1] = cadenaTratada[1].replace(" ", "")
        if (cadenaTratada[1][0] == '"'):
            isString=True
            cadenaTratada[1] = cadenaTratada[1].replace(" ", "")

        cadena = cadenaTratada[0].split() + listaIgual + cadenaTratada[1].split()

        rango = len(cadena)
        for i in range(rango):
            if (
                cadena[i] == "let"
                or cadena[i] == "const"
                or cadena[i] == "var"
                or cadena[i] == "new"
            ):
                # print("es un lexema",cadena[i])
                listaSeparados.append(cadena[i])
                listaEliminar.append(i)
            elif( "()" in cadena[i] and isString == False):
                print("entro a parenteisi")
                cadena[i] = cadena[i].replace("()", " () ")
                listaParentesis = cadena[i].split()
                for i in listaParentesis:
                    listaSeparados.append(i)
            elif("[]" in cadena[i] and isString==False):
                print("entro a corchetes")
                cadena[i] = cadena[i].replace("[]", " [] ")
                listaParentesis = cadena[i].split()
                for i in listaParentesis:
                    listaSeparados.append(i)
            elif("{}" in cadena[i] and isString==False):
                print("entro a llaves")
                cadena[i] = cadena[i].replace("{}", " {} ")
                listaParentesis = cadena[i].split()
                for i in listaParentesis:
                    listaSeparados.append(i)
            else:
                listaSeparados.append(cadena[i])
        return listaSeparados

    def simbolosId(self):
        listaSimbolos = []
        simbolosCrudos = self._separarID()
        for i in simbolosCrudos:
            if(i != "new" and i != "const" and i != "var" and i != "let" and i != "{}" and i != "()" and i != "[]"):
                for x in i:
                    listaSimbolos.append(x)
            else:
                listaSimbolos.append(i)
        print(simbolosCrudos)
        print(listaSimbolos)


x = separador('const constobjet = new a();')
x.simbolosId()
