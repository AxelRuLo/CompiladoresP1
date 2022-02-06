import ply.lex as lex
import re

tokens = ["ID", "NUMEROS","IPARENTESIS","DPARENTESIS","LLAVES","ESPACIO","COMA"]
reservadas = {'function':'function'}
tokens = tokens + list(reservadas.values())

t_ignore = r'\t'
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'
t_LLAVES = r'[{}]'
t_ESPACIO = r'\s+'
t_COMA = r'\,'


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

cadena = "function square(number) \{\}"
cadena1 = "function myFunc(theObject) \{\}"
cadena2 = "function map(f, a) \{\}"
cadena3 = "function suma(number) \{\}"
cadena4 = "function _suma(number) \{\}"
cadena5 = "function _s_u_m_a(number) \{\}"
cadena6 = "function Suma(number) \{\}"
cadena7 = "function _2s_u_m_a(number) \{\}"




analizador = lex.lex()
# analizador.input(cadena)
analizador.input(cadena1)
# analizador.input(cadena2)
# analizador.input(cadena3)
# analizador.input(cadena4)
# analizador.input(cadena5)
# analizador.input(cadena6)
# analizador.input(cadena7)


print("\n \n")
while True:
    tok = analizador.token()    
    if(not tok) : break
    print(tok)




