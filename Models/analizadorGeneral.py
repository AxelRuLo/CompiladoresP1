import ply.lex as lex
import re


tokens = ["ID","COMMENT","NUMEROSFLOTANTES", "NUMEROS", "IGUAL", "STRINGS","STRINGD", "LLAVES","IPARENTESIS","DPARENTESIS","NEW","PUNTOCOMA","CORCHETES","OBJETOPROPIEDAD","OPERADORES","COMA","OPERADORESARITMETICOS"]
reservadas = {"do":"do",'if':'if','else':'else', 'elseif': 'elseif','function':'function','class':'class','extends':'extends','let':'let','const':'const','var':'var','while':'while',"true":"true","false":"false"}
tokens = tokens + list(reservadas.values())

t_ignore = ' \t\n'
t_IGUAL = r'='
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
    
    return lex.lex()

def analizar(cadena):
    analizador = _analizadorVariable()
    analizador.input(cadena)
    listaTokens = []
    while True:
        tok = analizador.token()
        listaTokens.append(tok)
        if(not tok) : break
        print(tok)
    print("---------------")
    print(listaTokens)
    return listaTokens
