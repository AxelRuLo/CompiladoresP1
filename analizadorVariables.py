import ply.lex as lex
import re

tokens = ["ID", "NUMEROS", "IGUAL", "STRINGS","STRINGD", "LLAVES","IPARENTESIS","DPARENTESIS","NEW","PUNTOCOMA","CORCHETES","ESPACIO","OBJETOPROPIEDAD",]
reservadas = {'let':'let','const':'const','var':'var'}
tokens = tokens + list(reservadas.values())

t_ignore = r'\t'
t_IGUAL = r'='
t_CORCHETES = r'[{}]'
t_LLAVES = r'[[]]'
t_ESPACIO = r'\s+'
t_NEW = r'new'
t_PUNTOCOMA = r';'
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if(t.value in reservadas):
        t.value = t.value
        t.type  = t.value
    return t

def t_NUMEROS(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OBJETOPROPIEDAD(t):
    # r'[a-zA-Z_][a-zA-Z0-9_]*[.][a-z-A-Z_][a-zA-Z0-9_]*'
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
    print(f"invalido {t.value[0]}")
    t.lexer.skip(1)

cadena = "valor = 0"

analizador = lex.lex()
analizador.input(cadena)

print("\n \n")
while True:
    tok = analizador.token()
    if(not tok) : break
    print(tok)




