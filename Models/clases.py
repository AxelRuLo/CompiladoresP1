import ply.lex as lex
import re

tokens = ["ID", "NUMEROS","LLAVES","ESPACIO"]
reservadas = {'class':'class','extends':'extends'}
tokens = tokens + list(reservadas.values())

t_ignore = r'\t'
t_LLAVES = r'[{}]'
t_ESPACIO = r'\s+'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if(t.value in reservadas):
        t.value = t.value
        t.type  = t.value
    return t

# def t_NUMEROS(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t

def t_error(t):
    print(f"invalido {t.value[0]}")
    t.lexer.skip(1)

cadena = "class _Rectangulo2 extends Animal\{\}"

analizador = lex.lex()
analizador.input(cadena)

print("\n \n")
while True:
    tok = analizador.token()
    if(not tok) : break
    print(tok)




