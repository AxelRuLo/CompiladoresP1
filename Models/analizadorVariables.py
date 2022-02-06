import ply.lex as lex
import re


tokens = ["ID","NUMEROSFLOTANTES", "NUMEROS", "IGUAL", "STRINGS","STRINGD", "LLAVES","IPARENTESIS","DPARENTESIS","NEW","PUNTOCOMA","CORCHETES","OBJETOPROPIEDAD",]
reservadas = {'let':'let','const':'const','var':'var'}
tokens = tokens + list(reservadas.values())

t_ignore = ' \t\n'
t_IGUAL = r'='
t_LLAVES = r'[{}]'
t_CORCHETES= r'[\[\]]'
t_NEW = r'new'
t_PUNTOCOMA = r';'
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'

def analizadorVariable():


    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if(t.value in reservadas):
            t.value = t.value
            t.type  = t.value
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


    def t_COMMENT(t):
        r'[/][/].*'
        pass

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

cadena = "valor = {\n}'/////jalsdfjk'"

analizador=analizadorVariable()
analizador.input(cadena)

print("\n \n")
while True:
    tok = analizador.token()
    if(not tok) : break
    print(tok)




