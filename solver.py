from PySide6 import QtGui, QtWidgets
from functions import solver, CUR_DIR
import clipboard

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(CUR_DIR + '\DATA\icon.ico'))
        self.setWindowTitle("Cracker")
        self.components()

    def components(self):

        # --- Create components ---
        self.main_layout = QtWidgets.QWidget(self)
        self.main_gridLayout = QtWidgets.QGridLayout(self)
        self.lbl_password = QtWidgets.QLabel(self)
        self.le_password = QtWidgets.QLineEdit(self)
        self.btn_copy = QtWidgets.QPushButton('Copy')
        self.lbl_lenght = QtWidgets.QLabel(self)
        self.sbox_length = QtWidgets.QSpinBox(self)
        self.btn_solve_pwrd = QtWidgets.QPushButton(self)

        # --- Add components ---
        self.main_gridLayout.addWidget(self.lbl_password, 0, 0, 1, 1)
        self.main_gridLayout.addWidget(self.le_password, 0, 1, 1, 1)
        self.main_gridLayout.addWidget(self.btn_copy, 2, 0, 2, 1)
        self.main_gridLayout.addWidget(self.lbl_lenght, 1, 0, 1, 1)
        self.main_gridLayout.addWidget(self.sbox_length, 1, 1, 1, 1)
        self.main_gridLayout.addWidget(self.btn_solve_pwrd, 2, 1, 2, 1)

        # --- Components settings ---
        self.lbl_password.setText('The password is :')
        self.lbl_lenght.setText('The lenght is :')
        self.btn_solve_pwrd.setText('Solve')

        # --- Setup connexions ---
        self.btn_solve_pwrd.clicked.connect(self.solve)
        self.btn_copy.clicked.connect(self.copy)

    def solve(self):
        result = solver()
        pwrd = result[0]
        length = result[1]
        self.le_password.setText(f"{pwrd}")
        self.sbox_length.setValue(length)

    def copy(self):
        clipboard.copy(self.le_password.text())

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()