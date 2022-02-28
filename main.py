import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from Models.algoritmoNoRecursivo import intAlgoritmo

from Models.analizadorGeneral import analizar
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

        self.label_alert.hide()
        self.label_file_sucessful.hide()
        self.pushButton_buscarArchivo.clicked.connect(self.openFileNameDialog)
        self.pushButton_cargarArchivo.clicked.connect(self.cargarArchivo)
        self.pushButton_analizarCodigo.clicked.connect(self.ejecutarCodigo)
        self.pushButton_limpiarCodigo.clicked.connect(self.limpiarCodigo)
        self.pushButton_erroresLexico.clicked.connect(self.mostrarErroresLexico)
        self.pushButton_erroresLexico.hide()
        self.label_lexicoValido.hide()


    def openFileNameDialog(self):
        global text_file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Javascript Files (*.js)", options=options)
        if fileName:
            text_file = fileName
            self.textField_selected_file.setText(fileName)
            self.label_alert.hide()


    def cargarArchivo(self):
        global text_file
        if(len(text_file) == 0):
            self.label_alert.show()
        else:
            self.label_file_sucessful.show()
            leer_archivo = open(text_file)
            texto = leer_archivo.read()
            self.textEdit_Campo.setText(texto)
            leer_archivo.close()


    def ejecutarCodigo(self):
        global lista
        indexError = 0
        lexicoValido = False
        llenar = True
        texto = self.textEdit_Campo.toPlainText()
        
        algoritmoNoRecursivo = intAlgoritmo(texto)

        for x in algoritmoNoRecursivo:
            if(x != 'valido'):
                indexError = x
                lexicoValido = False
                print(f'INDEX ERROR:{indexError}')
                break
            else:
                lexicoValido = True
        
        lista = indexError

        if(texto == ''):
            self.label_lexicoValido.hide()
            self.pushButton_erroresLexico.hide()
        else:
            if(lexicoValido):
                self.label_lexicoValido.show()
                self.pushButton_erroresLexico.hide()
            else:
                self.label_lexicoValido.hide()
                self.pushButton_erroresLexico.show()

        listaTokens,listaValorTokens,listaLineaEncontrado = analizar(texto)

        self.llenar_tabla(listaTokens, listaValorTokens, listaLineaEncontrado , llenar)

    def limpiarCodigo(self):
        new_list = []
        new_list_2 = []
        new_list_3 = []

        llenar = False 
        self.textEdit_Campo.clear()
        self.textField_selected_file.clear()
        self.label_alert.hide()
        self.label_file_sucessful.hide()
        self.pushButton_erroresLexico.hide()
        self.label_lexicoValido.hide()
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
        self.demo.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
