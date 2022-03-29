from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from Views.Ui_diagram_view import Ui_Form

class DiagramViewController(QWidget):
    def __init__(self):
        super(DiagramViewController, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        label_img = QLabel()
        label_img.setPixmap(QPixmap('./Resources/classes.png'))
        label_img.adjustSize()

        self.ui.verticalLayout_diagram.addWidget(label_img, alignment=Qt.AlignCenter)