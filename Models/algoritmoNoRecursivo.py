from xml.dom import ValidationErr
from prueba import analizador_lexico,separ_atributos
from analizadorGeneral import analizar
import string
import pandas


class AlgoritmoNoRecursivo:
    def __init__(self, direccion, reglaInicial):
        matriz = pandas.read_csv(direccion, header=0)
        self.matriz = matriz
        self.reglas = self.matriz["regla"].to_list()
        self.pila = ["$"]
        self.reglaInicial = reglaInicial
        self.pila.append(reglaInicial)

        pass

    def ejecutarAlgoritmo(self, listaSimbolos: list):
        self.pila.clear()
        self.pila.append("$")
        self.pila.append(self.reglaInicial)
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
                    return self.pila
             
                

                print(f"\n PASADA NUMERO {index} ")
                print(f"esta es mi pila {self.pila}")

                try:
                    simboloBusacar = listaSimbolos[index]
                except:
                    simboloBusacar = "$"

                try:
                    reglaAnalizar = self.pila.pop()
                except:
                    pass



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
                        return self.pila

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
                        or reglaNueva == "<"
                        or reglaNueva == ">"
                        or reglaNueva == "if"
                        or reglaNueva == "else"
                        or reglaNueva == "switch"
                        or reglaNueva == "case"
                        or reglaNueva == "break"
                        or reglaNueva == "default"
                        or reglaNueva == "else if"
                        or reglaNueva == "extends"
                        or reglaNueva == "class"
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
                return self.pila
        except Exception:
            print(Exception.args())
            return self.pila
        

    def _sustituirLegible(self, simbolo):
        if(simbolo == "elseif"):
            return "else if"
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
        if(regla == "$"):
            return False
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

def intAlgoritmo(texto:str):
    texto = texto.replace("else if","elseif")
    listas = analizador_lexico(texto)
    if(listas == False):
        return False

    listas = separ_atributos(listas.copy())

    alClase = AlgoritmoNoRecursivo("../cssvs/clases.csv","C")
    alFunciones = AlgoritmoNoRecursivo("../cssvs/funciones.csv","I")
    alWhiles = AlgoritmoNoRecursivo("../cssvs/whiles.csv","P")
    alIdentificadores = AlgoritmoNoRecursivo("../cssvs/identificador.csv","P")
    alSwitch = AlgoritmoNoRecursivo("../cssvs/switch.csv","T")
    alIf = AlgoritmoNoRecursivo("../cssvs/ifs.csv","T")
    resultado = None
    resultados = []
    pila_error = []
    for lista in listas:
        pila_error = []
        resultado = alClase.ejecutarAlgoritmo(lista.copy())
        if(resultado != 'valido'):
            pila_error.append(resultado.copy())
        if(resultado != 'valido'):
            resultado = alFunciones.ejecutarAlgoritmo(lista.copy()) 
            if(resultado != 'valido'):
                pila_error.append(resultado.copy())
        if(resultado != 'valido'):
            resultado = alWhiles.ejecutarAlgoritmo(lista.copy()) 
            if(resultado != 'valido'):
                pila_error.append(resultado.copy())
        if(resultado != 'valido'):
            resultado = alIdentificadores.ejecutarAlgoritmo(lista.copy())
            if(resultado != 'valido'):
                pila_error.append(resultado.copy())
        if(resultado != 'valido'):
            resultado = alSwitch.ejecutarAlgoritmo(lista.copy())
            if(resultado != 'valido'):
                pila_error.append(resultado.copy())
        if(resultado != 'valido'):
            resultado = alIf.ejecutarAlgoritmo(lista.copy())
            if(resultado != 'valido'):
                pila_error.append(resultado.copy())
        if(resultado != 'valido'):
            resultados.append([lista,pila_error])
        else:
            resultados.append(resultado)

    return resultados

# print(intAlgoritmo("if(true){ switch(mes){ case 1: if(5>5){} break; case 2: if(5>5){} case 3: if(5>5){}  } }else {}"))
# print(intAlgoritmo("function correr(){let algo = 5;let algo = 5;}"))
# print(intAlgoritmo("function prueba1(){let variable1 = 0; let variable1 = 5; switch(variable1){case 1:}}"))
print(intAlgoritmo("do{ switch(mes){ case 1: if(5>5){} break; case 2: if(5>5){} case 3: if(5>5){}  } }while(true); whila(true){}"))





 