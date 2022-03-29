

from operator import le
from Models.analizadorGeneral import analizar



def analizador_lexico(text):
    frases_examinar = []
    token,valor,linea = analizar(text)
    switch_token,switch_valor = [],[]
    if(token.__contains__("error")):
        return False
    else:
        token,valor = buscar_this(token.copy(),valor.copy())
        aux_token_aux = token.copy()
        aux_valor_aux = valor.copy()
        token,valor = buscar_switch(token.copy(),valor.copy())
        if(token != False):
            switch_token = token[len(token)-1].copy()
            switch_valor = valor[len(valor)-1].copy()
            token.pop()
            valor.pop()
            aux_token =[]
            aux_valor = []
            for t in range(len(token)):
                aux_token.extend(token[t])
                aux_valor.extend(valor[t])
            valor = aux_valor
            token =aux_token
        else: 
            token = aux_token_aux
            valor = aux_valor_aux
        token,valor = buscar_llaves(token.copy(),valor.copy())

        if(token != False):
            token, valor = separ_atributos(valor.copy(),token.copy())
            if(len(switch_token)>0):
                token.append(switch_token)
                valor.append(switch_valor)
            for j in range(len(token)):
                frase_examinar = []
                i = 0
                while(i < len(token[j])):
                    if(token[j][i] == str(valor[j][i]) or (token[j][i] == "OPERADORES") or (token[j][i] == "this")):
                        frase_examinar.append(str(valor[j][i]))
                    else:
                        if(
                            (
                                (token[j][i]=="LLAVES" and token[j].__contains__("class")) 
                                or (token[j][i]=="LLAVES" and (token[j].__contains__("function") or token[j].__contains__("constructor"))) 
                                or (token[j][i]=="LLAVES" and (token[j].__contains__("let") or token[j].__contains__("var") or token[j].__contains__("const ") or token[j].__contains__("new"))) 
                                or (token[j][i]=="LLAVES" and not (token[j].__contains__("while") or token[j].__contains__("switch") or token[j].__contains__("if")))
                                )
                        or (token[j][i]=="CORCHETES" and (token[j].__contains__("let") or token[j].__contains__("var") or token[j].__contains__("const ") or token[j].__contains__("new") or token[j].__contains__("this")))
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
        else:
            return False
        
def buscar_this(token:list,valores:list):
    token_aux = token
    for i in range(len(token_aux)):
        if(token_aux[i]=="this"):
            if(token_aux[i+1] == "OBJETOPROPIEDAD"):
                valores[i] = "this."
                valores[i+1] = valores[i+1][1:len(valores[i+1])]
    return token,valores

def buscar_llaves(token:list,valores:list):
    valor = valores.copy()
    if(llaves_completas(valor)):
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
    else:
        return False,False

def buscar_switch(token:list,valores:list):
    valor = valores.copy()
    if(token.__contains__("switch")):
        llave = 0
        final_switch = buscar_llaves_switch(valores.copy())[1]
        aux = []
        llaves=[]
        while(valor.__contains__(":")):
            aux.clear()
            for i in range(len(valor)):
                
                if(valor[i] == ":" ):
                    llave += 1
                    if(llave ==1):
                        aux.append(i)
                if((valor[i] == "break" or valor[i] == "case" or valor[i] == "default" or i == final_switch ) and llave>0):
                    if(llave == 1):
                        aux.append(i)
                    llave -=1
                    break
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

        token_new,valores_new = limpiar_switch(token_new.copy(),valores_new.copy())

        return token_new,valores_new
    else:
        return False,False

def limpiar_switch(token:list,valores:list):

    ultimo = len(valores)-1

    if(valores[ultimo][0] == "switch"):
        return token, valores
    else:
        indexs = buscar_llaves_switch(valores[ultimo])
        aux = valores[ultimo].copy()
        aux_token = token[ultimo].copy()
        switch_array = valores[ultimo][indexs[0]:indexs[1]+1]
        switch_token = token[ultimo][indexs[0]:indexs[1]+1]
        del aux[indexs[0]:indexs[1]+1]
        del aux_token[indexs[0]:indexs[1]+1]
        token[ultimo] = aux_token.copy()
        token.append(switch_token)
        valores[ultimo] = aux.copy()
        valores.append(switch_array)
        return token,valores


def buscar_llaves_switch(valores:list):
    switch = 0
    llave = 0
    index = 0
    for i in range(len(valores)):
        if(valores[i] == "switch"):
            switch = 1
            index = i
        if(valores[i] == "{" and switch > 0):
            llave += 1
        if(valores[i] == "}" and switch > 0):
            if(llave == 1):
                return [index, i]
            llave = 1


def llaves_completas(valores:list):
    llave_a = 0
    llave_c = 0
    for valor in valores:
        if (valor == "{"):
            llave_a +=1
        if(valor == "}"):
            llave_c +=1
    if(llave_a == llave_c):
        return True
    else:
        return False

def separ_atributos_2(lista : list):
    token = ['switch',"do",'if','function','class','let','const','var','while',"constructor","this"]
    indexs = []
    anterior = 0
    for valor in lista:
        index = []
        for i in range(len(valor)):
            if  token.__contains__(str(valor[i])):
                if(str(valor[i]) == "do" ):
                    anterior = 1
                    index.append(i)
                else:
                    if(str(valor[i]) == "while" and anterior == 1):
                        anterior=0
                    else:
                        index.append(i)
            else:
                if(i<len(valor)):
                    if(str(valor[i]) == "{}" ):
                        
                        if(i+1<len(valor)):
                            index.append(i+1);

                        
        indexs.append(index)
    for i in range(len(indexs)):
        if(len(indexs[i])>1):
            aux_valor = lista[i]
            valor_new = []
            for j in range(len(indexs[i])):
                if(j+1<len(indexs[i])):
                    valor_new.append(aux_valor[indexs[i][j]:indexs[i][j+1]])
                else:
                    valor_new.append(aux_valor[indexs[i][j]:len(aux_valor)])
            del lista[i]
            lista.extend(valor_new)
    return lista

def separ_atributos(lista : list,token1:list):
    token = ['switch',"do",'if','function','class','let','const','var','while',"constructor","this."]
    indexs = []
    anterior = 0
    for valor in lista:
        index = []
        for i in range(len(valor)):
            if  token.__contains__(str(valor[i])):
                if(str(valor[i]) == "do" ):
                    anterior = 1
                    index.append(i)
                else:
                    if(str(valor[i]) == "while" and anterior == 1):
                        anterior=0
                    else:
                        index.append(i)
                        
        indexs.append(index)
    for i in range(len(indexs)):
        if(len(indexs[i])>1):
            aux_valor = lista[i]
            aux_Token = token1[i]
            valor_new = []
            token_new = []
            for j in range(len(indexs[i])):
                if(j+1<len(indexs[i])):
                    valor_new.append(aux_valor[indexs[i][j]:indexs[i][j+1]])
                    token_new.append(aux_Token[indexs[i][j]:indexs[i][j+1]])
                else:
                    valor_new.append(aux_valor[indexs[i][j]:len(aux_valor)])
                    token_new.append(aux_Token[indexs[i][j]:len(aux_Token)])
            lista[i] = -1
            token1[i] = -1
            lista.extend(valor_new)
            token1.extend(token_new)
    # print(lista)
    while(token1.__contains__(-1)):
        token1.remove(-1)
    while(lista.__contains__(-1)):
        lista.remove(-1)
  
            
    return token1,lista


    
# print(analizador_lexico("if(){let const = new []}"))