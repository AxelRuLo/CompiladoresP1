import ply.lex as lex
import re


tokens = ["ID","COMMENT","NUMEROSFLOTANTES","DOSPUNTOS", "NUMEROS", "IGUAL", "STRINGS","STRINGD", "LLAVES","IPARENTESIS","DPARENTESIS","NEW","PUNTOCOMA","CORCHETES","OBJETOPROPIEDAD","OPERADORES","COMA","OPERADORESARITMETICOS"]
reservadas = {'switch':'switch','case':'case', 'default': 'default',"do":"do",'if':'if','else':'else', 'elseif': 'elseif','function':'function','class':'class','extends':'extends','let':'let','const':'const','var':'var','while':'while',"true":"true","false":"false"}
tokens = tokens + list(reservadas.values())

t_ignore = ' \t\n'
t_IGUAL = r'='
t_DOSPUNTOS = r':'
t_LLAVES = r'[{}]'
t_CORCHETES= r'[\[\]]'
t_NEW = r'new'
t_PUNTOCOMA = r';'
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'
t_COMA = r'\,'
t_OPERADORESARITMETICOS = r'[+]|-'

def _analizadorVariable():



    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if(t.value in reservadas):
            t.value = t.value
            t.type  = t.value
        return t

    def t_COMMENT(t):
        r'[/][/].*[\t\n]'
        return t
    
    def t_OPERADORES(t):
        r'(===)|(>=)|(==)|(<=)|(<)|(>)|(!=)'

        return t

    def t_NUMEROSFLOTANTES(t):
        r'\d+\.\d+'

        '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'        
        t.value = float(t.value)
        return t

    def t_NUMEROS(t):
        # r'\d+[.]\d+'
        r'\d+'
        t.value = int(t.value)
        return t


    def t_OBJETOPROPIEDAD(t):
        r'\b\.[a-z-A-Z_][a-zA-Z0-9_]*\b'
        if(t.value in reservadas):
            t.value = t.value
            t.type  = t.value
        return t


    def t_STRINGS(t):
        r"['][a-zA-Z0-9!#$%&/'*+-.{}^_`\s|~:]*[']"
        return t

    def t_STRINGD(t):
        r'["][a-zA-Z0-9!#$%&/"*+-.{}^_`\s|~:]*["]'
        return t

    def t_error(t):
        print(f"invalido {t.value}")
        t.lexer.skip(1)
        return t
    
    return lex.lex()

def analizar(cadena):
    analizador = _analizadorVariable()
    analizador.input(cadena)
    listaTokens = []
    listaValorTokens = []
    listaLineaEncontrado = []
    listaGeneralTokens = []

    while True:
        tok = analizador.token()
        listaGeneralTokens.append(tok)
        if(not tok) : break
        # print(tok)
    # print("---------------")
    for index in range(len(listaGeneralTokens)-1):
        listaTokens.append(listaGeneralTokens[index].type)
        listaValorTokens.append(listaGeneralTokens[index].value)
        listaLineaEncontrado.append(listaGeneralTokens[index].lexpos)
    print(listaGeneralTokens)
    print(listaTokens)
    print(listaValorTokens)
    print(listaLineaEncontrado)
    return listaTokens,listaValorTokens,listaLineaEncontrado


