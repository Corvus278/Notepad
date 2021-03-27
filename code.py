import des
import codecs

import sys
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, des.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionNew.triggered.connect(self.New)
        self.actionSave.triggered.connect(self.Save)

    def New(self):
        self.textEdit.setText('')

    def Save(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить', 'D:/', filter=('.txt'))[0]
        with codecs.open(file + '.txt', 'w', encoding='utf8') as f:
            f.write(self.textEdit.toPlainText())
            f.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()