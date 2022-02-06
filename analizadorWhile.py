import ply.lex as lex

tokens = ["ID","NUMEROSFLOTANTES","NUMEROS","IPARENTESIS","DPARENTESIS","LLAVES","OPERADORES","PUNTOCOMA","COMMENT"]
reservadas = {'while':'WHILE',"True":"TRUE","False":"FALSE"}
tokens = tokens + list(reservadas.values())

t_ignore = ' \t'
t_LLAVES = r'[{}]'
t_PUNTOCOMA = r';'
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'

def analizadorVariable():

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if(t.value in reservadas):
            t.value = t.value
            t.type  = t.value.upper()
        return t

    def t_OPERADORES(t):
        r'(>=)|(==)|(<=)|(<)|(>)|(!=)'

        return t

    
    def t_NUMEROSFLOTANTES(t):
        r'\d+\.\d+'     
        t.value = float(t.value)
        return t

    def t_NUMEROS(t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_COMMENT(t):
        r'[/]{2,2}.*'
        pass

    def t_error(t):
        print(f"invalido {t.value}")
        t.lexer.skip(1)
    return lex.lex()

cadena = "while(10.1>10){}"

analizador=analizadorVariable()
analizador.input(cadena)

print("\n \n")
while True:
    tok = analizador.token()
    if(not tok) : break
    print(tok)