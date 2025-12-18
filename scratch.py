from PyQt5.QtCore import Qt


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Underverse')
main_win.resize(400,200)
main_win.show()

def SANIS():


asgor=QLabel('(@_@):')
asgor.setText('UNDERVERS')
papirus = QPushButton('Pypsik')

v_line = QVBoxLayout()



main_win.setLayout(v_line)

main_win.clicked.connect(SANIS)

app.exec_()


