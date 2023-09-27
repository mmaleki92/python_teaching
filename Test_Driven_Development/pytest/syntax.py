import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow


# Define the Python syntax highlighter
class PythonHighlighter(QSyntaxHighlighter):
    keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'print',
        'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False'
    ]

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)
        self.matchingRules = []  
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor('blue'))
        keywordFormat.setFontWeight(QFont.Bold)
        
        for word in self.keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = (pattern, keywordFormat)
            self.matchingRules.append(rule)
            
        self.commentFormat = QTextCharFormat()
        self.commentFormat.setForeground(QColor('gray'))
        self.commentStartExpression = QRegExp("#")
        
    def highlightBlock(self, text):
        for pattern, format in self.matchingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
        
        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = text.length()
            commentLength = endIndex - startIndex
            self.setFormat(startIndex, commentLength, self.commentFormat)
            startIndex = self.commentStartExpression.indexIn(text, startIndex + commentLength)


class PythonEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.highlighter = PythonHighlighter(self.textEdit.document())
        
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('PyQt5 Syntax Highlighter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = PythonEditor()
    sys.exit(app.exec_())
