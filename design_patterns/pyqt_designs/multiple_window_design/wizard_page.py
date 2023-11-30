import sys
from PyQt5.QtWidgets import QApplication, QWizard, QWizardPage, QVBoxLayout, QLabel, QLineEdit, QPushButton

class FirstPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle('First Page')
        layout = QVBoxLayout()
        self.label = QLabel('Enter your name:', self)
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

class SecondPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle('Second Page')
        layout = QVBoxLayout()
        self.label = QLabel('Enter your email:', self)
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

class ThirdPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle('Third Page')
        layout = QVBoxLayout()
        self.label = QLabel('Congratulations! Wizard Completed.', self)
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wizard = QWizard()
    wizard.addPage(FirstPage())
    wizard.addPage(SecondPage())
    wizard.addPage(ThirdPage())
    wizard.setWindowTitle('Wizard Design')
    wizard.show()
    sys.exit(app.exec_())
