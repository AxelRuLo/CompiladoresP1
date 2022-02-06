import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5 import uic, QtWidgets 

text_file = ''

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/main.ui', self)
        self.label_alert.hide()
        self.label_file_sucessful.hide()
        self.pushButton_buscarArchivo.clicked.connect(self.openFileNameDialog)
        self.pushButton_cargarArchivo.clicked.connect(self.cargarArchivo)
        self.pushButton_analizarCodigo.clicked.connect(self.obtenerCodigo)
        self.pushButton_limpiarCodigo.clicked.connect(self.limpiarCodigo)


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
            print(texto)
            leer_archivo.close()


    def obtenerCodigo(self):
        llenar = True
        texto = self.textEdit_Campo.toPlainText()
        print(texto)
        new_list = list(texto)
        self.llenar_tabla(new_list, llenar)

    def limpiarCodigo(self):
        new_list = []
        llenar = False 
        self.textEdit_Campo.clear()
        self.textField_selected_file.clear()
        self.label_alert.hide()
        self.label_file_sucessful.hide()
        self.llenar_tabla(new_list, llenar)


    def llenar_tabla(self, list: list, llenar: bool):
        row = 0
        tamano = len(list)
        self.tabla_tokens.setRowCount(tamano)
        while row < tamano:
            if(llenar):
                self.tabla_tokens.setItem(row, 0, QtWidgets.QTableWidgetItem(str(list[row])))
                self.tabla_tokens.setItem(row, 1, QtWidgets.QTableWidgetItem(str(list[row])))
                self.tabla_tokens.setItem(row, 2, QtWidgets.QTableWidgetItem(str(list[row])))
            else:
                self.tabla_tokens.setItem(row, 0, QtWidgets.QTableWidgetItem(str('')))
                self.tabla_tokens.setItem(row, 1, QtWidgets.QTableWidgetItem(str('')))
                self.tabla_tokens.setItem(row, 2, QtWidgets.QTableWidgetItem(str('')))
            row+=1

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')