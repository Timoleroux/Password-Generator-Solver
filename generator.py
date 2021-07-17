from PyQt6 import QtCore, QtGui, QtWidgets
from functions import generator, writePassword, CUR_DIR
import clipboard

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(CUR_DIR + '\DATA\icon.ico'))
        self.setWindowTitle("Generator")
        self.setMinimumSize(QtCore.QSize(400, 188))
        self.setMaximumSize(QtCore.QSize(400, 188))
        self.components()

    def components(self):

        # --- Create components ---
        self.main_gridlayout = QtWidgets.QGridLayout(self)
        self.cbox_capital_letter = QtWidgets.QCheckBox(self)
        self.lbl_min = QtWidgets.QLabel(self)
        self.cbox_number = QtWidgets.QCheckBox(self)
        self.sld_max = QtWidgets.QSlider(self)
        self.sld_min = QtWidgets.QSlider(self)
        self.lbl_password = QtWidgets.QLabel(self)
        self.cbox_special_char = QtWidgets.QCheckBox(self)
        self.lbl_nbr_char = QtWidgets.QLabel(self)
        self.lbl_max = QtWidgets.QLabel(self)
        self.le_password = QtWidgets.QLineEdit(self)
        self.btn_copy = QtWidgets.QPushButton(self)
        self.btn_generate = QtWidgets.QPushButton(self)

        # --- Add components ---
        self.main_gridlayout.addWidget(self.cbox_capital_letter, 2, 0, 1, 1)
        self.main_gridlayout.addWidget(self.lbl_min, 3, 1, 1, 1)
        self.main_gridlayout.addWidget(self.cbox_number, 3, 0, 1, 1)
        self.main_gridlayout.addWidget(self.sld_max, 4, 2, 1, 6)
        self.main_gridlayout.addWidget(self.sld_min, 3, 2, 1, 6)
        self.main_gridlayout.addWidget(self.lbl_password, 0, 0, 1, 1)
        self.main_gridlayout.addWidget(self.cbox_special_char, 4, 0, 1, 1)
        self.main_gridlayout.addWidget(self.lbl_nbr_char, 2, 1, 1, 2)
        self.main_gridlayout.addWidget(self.lbl_max, 4, 1, 1, 1)
        self.main_gridlayout.addWidget(self.le_password, 1, 0, 1, 7)
        self.main_gridlayout.addWidget(self.btn_copy, 1, 7, 1, 1)
        self.main_gridlayout.addWidget(self.btn_generate, 6, 0, 1, 8)

        # --- Components settings ---
        self.cbox_capital_letter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cbox_number.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sld_max.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sld_max.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sld_max.setMaximum(50)
        self.sld_min.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sld_min.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sld_min.setMaximum(50)
        self.cbox_special_char.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_generate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # --- Components text ---
        self.lbl_min.setText("Min : 0")
        self.cbox_capital_letter.setText("Capital letters")
        self.cbox_number.setText("Numbers")
        self.lbl_password.setText("The password is :")
        self.cbox_special_char.setText("Special caracters")
        self.lbl_nbr_char.setText("Number of caracters :")
        self.lbl_max.setText("Max : 0")
        self.btn_copy.setText("Copy")
        self.btn_generate.setText("Generate")

        # --- Component connexions ---
        self.btn_generate.clicked.connect(self.generate)
        self.btn_copy.clicked.connect(self.copy)
        self.sld_max.valueChanged.connect(self.changeLabelMinMax)
        self.sld_min.valueChanged.connect(self.changeLabelMinMax)

    def generate(self):
        min = self.sld_min.value()
        max = self.sld_max.value()
        if min < max:
            cap = self.cbox_capital_letter.isChecked()
            nbr = self.cbox_number.isChecked()
            spe = self.cbox_special_char.isChecked()
            self.le_password.setText(generator(min, max, cap, nbr, spe))
            writePassword(self.le_password.text())
        else:
            self.le_password.setText("/!\\ Minimal value is bigger than the maximal /!\\")

    def copy(self):
        clipboard.copy(self.le_password.text())

    def changeLabelMinMax(self):
        min = self.sld_min.value()
        max = self.sld_max.value()

        self.lbl_min.setText(f"Min : {min}")
        self.lbl_max.setText(f"Max : {max}")

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()