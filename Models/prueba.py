

from operator import le
from analizadorGeneral import analizar


def analizador_lexico(text):
    frases_examinar = []
    # token,valor,linea = analizar("class Rectangulo extends Animal ()")
    token,valor,linea = analizar(text)
    if(token.__contains__("error")):
        return False
    else:
        token,valor = buscar_llaves(token.copy(),valor.copy())
        for j in range(len(token)):
            frase_examinar = []
            i = 0
            while(i < len(token[j])):
                if(token[j][i] == str(valor[j][i])):
                    frase_examinar.append(str(valor[j][i]))
                else:
                    if(
                        (
                            (token[j][i]=="LLAVES" and token[j].__contains__("class")) 
                            or (token[j][i]=="LLAVES" and token[j].__contains__("function")) 
                            or (token[j][i]=="LLAVES" and (token[j].__contains__("let") or token[j].__contains__("var") or token[j].__contains__("const ") or token[j].__contains__("new"))) 
                            )
                    or (token[j][i]=="CORCHETES" and (token[j].__contains__("let") or token[j].__contains__("var") or token[j].__contains__("const ") or token[j].__contains__("new")))
                    or (token[j][i]=="IPARENTESIS" and (token[j].__contains__("let") or token[j].__contains__("var") or token[j].__contains__("const ") or token[j].__contains__("new")))
                    ):
                        if(i+1 <len(token[j])):
                            if(token[j][i+1]=="LLAVES" or token[j][i+1]=="CORCHETES" or token[j][i+1]=="DPARENTESIS"):
                                frase_examinar.append(str(valor[j][i])+str(valor[j][i+1]))
                                i = i+1
                            else:
                                frase_examinar.append(str(valor[j][i]))
                        else:
                            frase_examinar.append(str(valor[j][i]))
                    else:
                        for caracter in str(valor[j][i]):
                            frase_examinar.append(caracter)
                i = i+1
            frases_examinar.append(frase_examinar)
        return frases_examinar

def buscar_llaves(token:list,valores:list):
    valor = valores.copy()
    llave = 0
    aux = []
    llaves=[]
    while(valor.__contains__("{") or valor.__contains__("}")):
        aux.clear()
        for i in range(len(valor)):
            if(valor[i] == "{" ):
                llave += 1
                if(llave ==1):
                    aux.append(i)
            if(valor[i] == "}"):
                if(llave == 1):
                    aux.append(i)
                llave -=1
        if(len(aux)>1):
            llaves.append(aux.copy())
            valor[aux[1]] = "-1"
            valor[aux[0]] = "-1"

    valores_new = []
    token_new = []
    llaves.reverse()
    for index_llave in llaves:
        if(index_llave[1]-index_llave[0] > 1):
            aux_1 = valores[index_llave[0]+1:index_llave[1]]
            while(aux_1.__contains__("******")):
                aux_1.remove("******")
            valores_new.append(aux_1.copy())

            aux_2 = token[index_llave[0]+1:index_llave[1]]
            while(aux_2.__contains__("******")):
                aux_2.remove("******")
            token_new.append(aux_2)

            for i in range(index_llave[0]+1,index_llave[1]):
                valores[i] = "******"
            for i in range(index_llave[0]+1,index_llave[1]):
                token[i] = "******"

    while(valores.__contains__("******")):
        valores.remove("******")
    while(token.__contains__("******")):
        token.remove("******")
    if(len(valores)>0):
        valores_new += [valores]
        token_new +=[token]
    return token_new,valores_new



    
# print(analizador_lexico("if(){let const = new []}"))