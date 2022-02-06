import ply.lex as lex
import re

tokens = ["ID", "NUMEROS", "STRINGS","STRINGD", "LLAVES","IPARENTESIS","DPARENTESIS","NEW","PUNTOCOMA","CORCHETES","ESPACIO","OBJETOPROPIEDAD", "OPERADORESLOGICOS", "OPERADORESARITMETICOS"]
reservadas = {'if':'if','else':'else', 'elseif': 'elseif'}
tokens = tokens + list(reservadas.values())

t_ignore = r'\t'
t_CORCHETES = r'[{}]'
t_LLAVES = r'[[]]'
# t_ESPACIO = r'\s+'
t_NEW = r'new'
t_PUNTOCOMA = r';'
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'
t_OPERADORESLOGICOS = r'(<|>)(=)|(<|>)|(=)(=)(=)|(=)(=)'
t_OPERADORESARITMETICOS = r'[+]|-'

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

cadena_a_leer = "if (JUAN1a == 1){} else{}"
cadena = cadena_a_leer.replace(' ', '') #eliminar espacios
print(f'CADENA: {cadena}')

analizador = lex.lex()
analizador.input(cadena)

print("\n \n")
while True:
    tok = analizador.token()
    if(not tok) : break
    print(tok)

