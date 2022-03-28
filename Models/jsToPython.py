import os
import re

def createFile(code:str):
    path = './Resources'
    isExist = os.path.exists(path)
    if not isExist:
      os.makedirs(path)

    textFile = open(f"{path}/class_generator.py", "w")
    textFile.write(code)
    textFile.close()
    
    os.system(f"pyreverse -o png {path}/class_generator.py -d {path}")


def parsingCode(code:str):
    #searching javascript function,variables and classes with regex
    rgx =  re.compile('\s*[A-Za-z_][A-Za-z_0-9]*?\s*\(.*?\)\s*{\s*.*?\s*}\s*')
    rgx_var = re.compile('{\s*[A-Za-z][A-Za-z_0-9]*?\s*.*\s*}')
    rgx_class = re.compile('\s*class\s*[A-Za-z_][A-Za-z_0-9]*\s*')

    #Replace elements
    code = code.replace('this', 'self').replace(' ', '').replace('\n', '')
    code = code.replace('class', '\n\nclass ')
    evaluate = re.findall(rgx, code)
    evaluate_class = re.findall(rgx_class, code)

    if(evaluate_class):
        listClass = evaluate_class
        for className in listClass:
            aux_class = className
            if(className.__contains__('extends')):
                className = className.replace('extends', '(')
                className = className + ')'

                code = code.replace(aux_class,className)

    if(evaluate):
        listFunctions = evaluate 
        for function in listFunctions:
            aux = function
            function = 'def' + function

            if(function.__contains__('constructor')):
                function = function.replace('constructor', '__init__')
                evaluateVar = re.findall(rgx_var, function)
                value = evaluateVar[0].replace('self','\n\t\tself').replace('new', '')   
                function = function.replace(evaluateVar[0], value)

            if(function.__contains__('def') and not function.__contains__('__init__')):
                if(function.__contains__('new')):
                    evaluateVar = re.findall(rgx_var, function)
                    function = function.replace(evaluateVar[0], '{pass }')
                else:
                    evaluateVar = re.findall(rgx_var, function)
                    function = function.replace(evaluateVar[0], '{pass }')
                
            function = function.replace('(', '(self,')
            function = function.replace('{', '{\n\t\t')
            function = function.replace('}', '}\n')
            function = function.replace(';', '')
            function = function.replace("def", "\n\tdef ")

            code = code.replace(aux, function)           
    else:
        print('function not found')


    code = list(code)
    
    for i in range(len(code)):
        if(code[i] == '{'):
            code[i] = ":"
        
        elif(code[i] == '}'):
            code[i] = ""


    code = "".join(code)
    createFile(code)



# code = """
#           class Rectangulo{
#     constructor (alto, ancho) {
#       this.alto = alto; 
#       this.ancho = ancho;
#       this.carro = Carro();
#     }

#     _12calcArea_ () {
#       return this.alto * this.ancho;
#     }
# }

#           class Artefactos{
#   constructor(artefacto1, artefacto2){
#         this.artefacto1 = artefacto1
#           this.artefacto2 = artefacto2
#   }

#         apagar(){
#     console.log('apagado')
#   }
# }


#         class Carro extends Artefactos{
#         constructor (alto, ancho) {
#           this.alto = alto; 
#         this.ancho = ancho;
#   }

#   encender () {
#           console.log('encender');
#     }
#   }
# """

# parsingCode(code)