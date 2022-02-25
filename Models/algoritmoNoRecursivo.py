from analizadorGeneral import analizar
import string
import pandas


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

        if len(cadenaTratada) > 2 or len(cadenaTratada) < 2:
            return False

        if self.cadena.count("()") > 1:
            return False
        if self.cadena.count("[]") > 1:
            return False
        if self.cadena.count("{}") > 1:
            return False

        if cadenaTratada[1][0] == "'":
            isString = True
            cadenaTratada[1] = cadenaTratada[1].replace(" ", "")
        if cadenaTratada[1][0] == '"':
            isString = True
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
            elif "()" in cadena[i] and isString == False:
                # print("entro a parenteisi")
                cadena[i] = cadena[i].replace("()", " () ")
                listaParentesis = cadena[i].split()
                for i in listaParentesis:
                    listaSeparados.append(i)
            elif "[]" in cadena[i] and isString == False:
                # print("entro a corchetes")
                cadena[i] = cadena[i].replace("[]", " [] ")
                listaParentesis = cadena[i].split()
                for i in listaParentesis:
                    listaSeparados.append(i)
            elif "{}" in cadena[i] and isString == False:
                # print("entro a llaves")
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
        # print(simbolosCrudos)
        if simbolosCrudos == False:
            return False
        for i in simbolosCrudos:
            if (
                i != "new"
                and i != "const"
                and i != "var"
                and i != "let"
                and i != "{}"
                and i != "()"
                and i != "[]"
            ):
                for x in i:
                    listaSimbolos.append(x)
            else:
                listaSimbolos.append(i)
        # print(simbolosCrudos)
        # print(listaSimbolos)
        return listaSimbolos

def seprar(text):
    frase_examinar = []
    # token,valor,linea = analizar("class Rectangulo extends Animal ()")
    token,valor,linea = analizar(text)
    if(token.__contains__("error")):
        return False
    else:
        # buscar_llaves(token.copy(),valor.copy())
        i = 0
        while(i < len(token)):
            if(token[i] == str(valor[i])):
                frase_examinar.append(str(valor[i]))
            else:
                if(token[i]=="LLAVES" or token[i]=="CORCHETES" or token[i]=="IPARENTESIS"):
                    if(i+1 <len(token)):

                        if(token[i+1]=="LLAVES" or token[i+1]=="CORCHETES" or token[i+1]=="DPARENTESIS"):
                            frase_examinar.append(str(valor[i])+str(valor[i+1]))
                            i = i+1
                        else:
                            frase_examinar.append(str(valor[i]))
                    else:
                        frase_examinar.append(str(valor[i]))
                else:
                    for caracter in str(valor[i]):
                        frase_examinar.append(caracter)
            i = i+1
        return frase_examinar

class AlgoritmoNoRecursivo:
    def __init__(self, direccion, reglaInicial):
        matriz = pandas.read_csv(direccion, header=0)
        self.matriz = matriz
        self.reglas = self.matriz["regla"].to_list()
        self.pila = []
        self.pila.append(reglaInicial)

        print(self.reglas)

        pass

    def ejecutarAlgoritmo(self, listaSimbolos: list):
        # print(listaSimbolos)
        try:

            
            if listaSimbolos == False:
                print("invalido")
                return False

            numeroElementosListaSimbolos = len(listaSimbolos)
            # print(numeroElementosListaSimbolos)
            index = 0

            print("INICIA EL ALGORITMO \n")
            while numeroElementosListaSimbolos > -1:

                if(len(self.pila)==0 and index!=len(listaSimbolos)):
                    return "no valida"
             
                

                print(f"\n PASADA NUMERO {index} ")
                print(f"esta es mi pila {self.pila}")

                try:
                    simboloBusacar = listaSimbolos[index]
                except:
                    simboloBusacar = "$"

                try:
                    reglaAnalizar = self.pila.pop()
                except:
                    if(len(listaSimbolos)<index):
                        print(listaSimbolos[index])



                self.pila.append(reglaAnalizar)

                print(
                    f"esta es mi simbolo {simboloBusacar}, esta es mi regla analizar : {reglaAnalizar}"
                )

                if simboloBusacar == reglaAnalizar:
                    self.pila.pop()
                    index = index + 1
                    numeroElementosListaSimbolos = numeroElementosListaSimbolos - 1
                else:
                    reglaNueva = self._buscarReglaExisitente(reglaAnalizar, simboloBusacar)
                    if reglaNueva == False:
                        return "error"

                    if (
                        reglaNueva == ";"
                        or reglaNueva == "."
                        or reglaNueva == "_"
                        or reglaNueva == "{}"
                        or reglaNueva == "="
                        or reglaNueva == "[]"
                        or reglaNueva == "a...z"
                        or reglaNueva == "var"
                        or reglaNueva == "cost"
                        or reglaNueva == "A...Z"
                        or reglaNueva == "0...9"
                        or reglaNueva == "let"
                        or reglaNueva == "new"
                        or reglaNueva == "{"
                        or reglaNueva == "}"
                        or reglaNueva == "("
                        or reglaNueva == ")"
                        or reglaNueva == "while"
                        or reglaNueva == "do"
                        or reglaNueva == "false"
                        or reglaNueva == "true"
                        or reglaNueva == "=="
                        or reglaNueva == "==="
                        or reglaNueva == "!=="
                        or reglaNueva == ">="
                        or reglaNueva == "<="
                        or reglaNueva == "!="
                    ):
                        self.pila.pop()
                        index = index + 1
                        numeroElementosListaSimbolos = numeroElementosListaSimbolos - 1
                    elif reglaNueva == "vacio":
                        self.pila.pop()
                    else:
                        self.pila.pop()
                        reglaNuevaSeparada = reglaNueva.split()
                        reglaNuevaSeparada.reverse()
                        self.pila.extend(reglaNuevaSeparada)

                # if(index+1 ==len(listaSimbolos)):
                    # break

            if(len(self.pila)==0 and simboloBusacar=="$"):
                return "valido"
            else:
                return "no valido"
        except ValueError :
            return ValueError
        

    def _sustituirLegible(self, simbolo):
        if len(simbolo) > 1:
            return simbolo
        if string.ascii_lowercase.__contains__(simbolo):
            return "a...z"
        if string.ascii_uppercase.__contains__(simbolo):
            return "A...Z"
        if str.isdigit(simbolo):
            return "0...9"
        return simbolo

    def _buscarReglaExisitente(self, regla, simboloBuscar):
        print(f"estoy buscando el simbolo {simboloBuscar} con la regla {regla}")
        simboloBuscar = self._sustituirLegible(simboloBuscar)
        indexBusqueda = self.reglas.index(regla)
        nuevaRegla = ""
        for columna in self.matriz:
            if columna != "regla":
                # print(columna)
                # print(self.matriz[columna][indexBusqueda])
                if columna == simboloBuscar:
                    if self.matriz[columna][indexBusqueda] != "-1":
                        nuevaRegla = self.matriz[columna][indexBusqueda]
                        # print(f"ENCONTRADO {nuevaRegla}")

        if nuevaRegla == "":
            print("no hay conincidencias")
            return False
        else:
            print(f"se encontro conicidencia con la regla {nuevaRegla}")
        return nuevaRegla




 