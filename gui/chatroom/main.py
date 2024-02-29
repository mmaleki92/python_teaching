import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QPushButton, QListWidgetItem
from PyQt5.QtCore import Qt

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadChats()

    def initUI(self):
        self.setWindowTitle('PyQt Telegram-like Chat')
        self.setGeometry(100, 100, 400, 600)

        self.layout = QVBoxLayout()

        self.chatList = QListWidget()
        self.layout.addWidget(self.chatList)

        self.messageInput = QLineEdit()
        self.messageInput.setPlaceholderText("Type a message...")
        self.layout.addWidget(self.messageInput)

        self.sendButton = QPushButton('Send')
        self.layout.addWidget(self.sendButton)

        self.setLayout(self.layout)

        # Connect the button click to sendMessage method
        self.sendButton.clicked.connect(self.sendMessage)
        
        # Connect the Enter key press to sendMessage method
        self.messageInput.returnPressed.connect(self.sendMessage)

        # StyleSheet
        self.applyStyleSheet()

    def loadChats(self):
        with open('chats.json', 'r') as file:
            data = json.load(file)
            for message in data['messages']:
                self.displayMessage(message)

    def sendMessage(self):
        text = self.messageInput.text()
        if text:  # Check if the text is not empty
            # For simplicity, we'll just display the message in the chatList
            # In a real application, you would also save this message to your chat history (e.g., a file or database)
            message = {"sender": "You", "text": text, "time": "Now"}  # Example message structure
            self.displayMessage(message)
            self.messageInput.clear()  # Clear the input field after sending

    def displayMessage(self, message):
        chatItem = QListWidgetItem(f"{message['sender']}: {message['text']} ({message['time']})")
        self.chatList.addItem(chatItem)

    def applyStyleSheet(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #EDEDED;
            }
            QListWidget {
                border: none;
                color: #333333;
                font-size: 14px;
            }
            QLineEdit {
                border: 2px solid #EDEDED;
                border-radius: 10px;
                padding: 5px;
                background-color: #FFFFFF;
            }
            QPushButton {
                background-color: #5682a3;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #4b7399;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
