import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem
from Controller.diagramViewController import DiagramViewController
from Models.algoritmoNoRecursivo import intAlgoritmo
from PyQt5 import QtWidgets, uic
from Models.analizadorGeneral import analizar
from Models.jsToPython import parsingCode
from Models.prueba import llaves_completas 

text_file = ''
lista = []

class SecondWindow(QWidget):
    def __init__(self, listErrors:list):
        super().__init__()
        self.listErrors = listErrors
        uic.loadUi('./Views/view_errores_lexico.ui', self)
        self.llenar_tabla()
        self.tabla_errores.setColumnWidth(1,350)


    def llenar_tabla(self):
        lista_datos = self.listErrors[0]
        lista_pila = self.listErrors[1]
        row = 0
        tamano = 0
        tamano_datos = len(lista_datos)
        tamano_pila = len(lista_pila)

        if(tamano_datos >= tamano_pila):
            tamano = tamano_datos
        elif(tamano_datos <= tamano_pila):
            tamano = tamano_pila

        self.tabla_errores.setRowCount(tamano)
        
        while row < tamano_datos:
            self.tabla_errores.setItem(row, 0, QtWidgets.QTableWidgetItem(str(lista_datos[row])))
            row+=1

        row = 0

        while row < tamano_pila:
            self.tabla_errores.setItem(row, 1, QtWidgets.QTableWidgetItem(str(lista_pila[row])))
            row+=1
      


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/main.ui', self)

        self.label_alert.setVisible(False)
        self.label_file_sucessful.setVisible(False)
        self.pushButton_buscarArchivo.clicked.connect(self.openFileNameDialog)
        self.pushButton_cargarArchivo.clicked.connect(self.cargarArchivo)
        self.pushButton_analizarCodigo.clicked.connect(self.ejecutarCodigo)
        self.pushButton_limpiarCodigo.clicked.connect(self.limpiarCodigo)
        self.pushButton_erroresLexico.clicked.connect(self.mostrarErroresLexico)
        self.pushButton_verDiagramaUML.clicked.connect(self.mostrarDiagrama)
        self.label_claseNoEncontrada.setVisible(False)
        self.pushButton_verDiagramaUML.setVisible(False)
        self.pushButton_erroresLexico.setVisible(False)
        self.label_lexicoValido.setVisible(False)
        self.label_lexicoInvalido.setVisible(False)
        self.label_sintaticoValido.setVisible(False)
        self.label_sintaticoInvalido.setVisible(False)


    def openFileNameDialog(self):
        global text_file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",";Javascript Files (*.js)", options=options)
        if fileName:
            text_file = fileName
            self.textField_selected_file.setText(fileName)
            self.label_alert.setVisible(False)


    def cargarArchivo(self):
        global text_file
        if(len(text_file) == 0):
            self.label_alert.setVisible(True)
        else:
            self.label_file_sucessful.setVisible(True)
            leer_archivo = open(text_file)
            texto = leer_archivo.read()
            self.textEdit_Campo.setText(texto)
            leer_archivo.close()


    def ejecutarCodigo(self):
        global lista
        indexError = 0
        isLexicoValido = False
        isSintacticoValido = False
        lexicoValido = False
        llenar = True
        texto = self.textEdit_Campo.toPlainText()
        # print(texto)
        
        algoritmoNoRecursivo = intAlgoritmo(texto)
        # print(f'ALGORITMO: {algoritmoNoRecursivo}')
        if(algoritmoNoRecursivo != False):
            # print('ENTRE')
            for x in algoritmoNoRecursivo:
                if(x != 'valido'):
                    indexError = x
                    lexicoValido = False
                    # print(f'INDEX ERROR:{indexError}')
                    break
                else:
                    lexicoValido = True
            
            lista = indexError

            if(texto == ''):
                isSintacticoValido = False
                isLexicoValido = False
                self.label_sintaticoValido.setVisible(False)
                self.pushButton_erroresLexico.setVisible(False)
                self.label_sintaticoInvalido.setVisible(False)
                self.label_lexicoValido.setVisible(False)
                self.label_lexicoInvalido.setVisible(False)
                self.pushButton_verDiagramaUML.setVisible(False)
            else:
                if(lexicoValido):
                    isSintacticoValido = True
                    self.label_sintaticoValido.setVisible(True)
                    self.pushButton_erroresLexico.setVisible(False)
                    self.label_sintaticoInvalido.setVisible(False)
                else:
                    isSintacticoValido = False
                    self.label_sintaticoValido.setVisible(False)
                    self.label_sintaticoInvalido.setVisible(True)
                    self.pushButton_erroresLexico.setVisible(True)
                    self.pushButton_verDiagramaUML.setVisible(False)
                    self.pushButton_verDiagramaUML.setVisible(False)
        else:
            self.label_sintaticoInvalido.setVisible(True)
            self.pushButton_verDiagramaUML.setVisible(False)


        listaTokens,listaValorTokens,listaLineaEncontrado = analizar(texto)
        if(listaTokens.__contains__("error")):
            self.label_lexicoInvalido.setVisible(True)
            self.pushButton_verDiagramaUML.setVisible(False)
            isLexicoValido = False
        else:
            if(len(listaTokens) > 0):
                self.label_lexicoValido.setVisible(True)
                isLexicoValido = True
        
        self.llenar_tabla(listaTokens, listaValorTokens, listaLineaEncontrado , llenar)

        if(isLexicoValido and isSintacticoValido):
            texto = self.textEdit_Campo.toPlainText()
            if(texto.__contains__('class')):
                self.labe_notificacion.setText("")
                token,valor, indice = analizar(texto)
                if(self.comprobar(token.copy(),valor.copy())):
                    self.pushButton_verDiagramaUML.setVisible(True)
                    self.label_claseNoEncontrada.setVisible(False)
                else:
                    self.pushButton_verDiagramaUML.setVisible(False)
                    
            else:
                self.label_claseNoEncontrada.setVisible(True)
                print('CLASE NO ENCONTRADA')

    def limpiarCodigo(self):
        new_list = []
        new_list_2 = []
        new_list_3 = []

        llenar = False 
        self.textEdit_Campo.clear()
        self.textField_selected_file.clear()
        self.label_alert.setVisible(False)
        self.label_file_sucessful.setVisible(False)
        self.pushButton_erroresLexico.setVisible(False)
        self.label_sintaticoValido.setVisible(False)
        self.label_sintaticoInvalido.setVisible(False)
        self.label_lexicoValido.setVisible(False)
        self.label_lexicoInvalido.setVisible(False)
        self.pushButton_verDiagramaUML.setVisible(False)
        self.llenar_tabla(new_list, new_list_2, new_list_3, llenar)


    def llenar_tabla(self, listaTokens: list, listaValorTokens: list, listaLineaEncontrado: list , llenar: bool):
        row = 0
        tamano = len(listaTokens)
        self.tabla_tokens.setRowCount(tamano)
        while row < tamano:
            if(llenar):
                self.tabla_tokens.setItem(row, 0, QtWidgets.QTableWidgetItem(str(listaTokens[row])))
                self.tabla_tokens.setItem(row, 1, QtWidgets.QTableWidgetItem(str(listaValorTokens[row])))
                self.tabla_tokens.setItem(row, 2, QtWidgets.QTableWidgetItem(str(listaLineaEncontrado[row])))
            else:
                self.tabla_tokens.setItem(row, 0, QtWidgets.QTableWidgetItem(str('')))
                self.tabla_tokens.setItem(row, 1, QtWidgets.QTableWidgetItem(str('')))
                self.tabla_tokens.setItem(row, 2, QtWidgets.QTableWidgetItem(str('')))
            row+=1

    def mostrarErroresLexico(self):
        global lista
        listError = lista
        w = SecondWindow(listError)
        self.demo = w
        self.demo.setVisible(True)

    
    def mostrarDiagrama(self):
        texto = self.textEdit_Campo.toPlainText()
        parsingCode(texto)
        view = DiagramViewController()
        self.demo = view
        self.demo.show()
        
    def comprobar(self,token,valor):
        nombreClases = []
        nombreExtends = []
        nombreObjeto = []
        
        
        for i in range(len(token)):
            if token[i] == 'class':
                nombreClases.append(valor[i+1]);
            if token[i] == 'extends':
                nombreExtends.append(valor[i+1]);
            if token[i] == 'new':
                nombreObjeto.append(valor[i+1]);
        for ext in nombreExtends:
            contiene = nombreClases.__contains__(ext)
            if(contiene == False):
                print('no existe la clase que quiere heredar ')
                self.labe_notificacion.setText("No existe la clase que quiere heredar")
                return False
        for obj in nombreObjeto:
            contiene = nombreClases.__contains__(obj)
            if(contiene == False):
                print('no existe la clase que quiere instanciar ')
                self.labe_notificacion.setText("No existe la clase que quiere instanciar")
                return False
        return True
        
                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    demo = Window()
    demo.setVisible(True)

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
