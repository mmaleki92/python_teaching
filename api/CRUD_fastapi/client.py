
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import json

app = QApplication([])
window = QWidget()
lbl = QLabel("Hi!", parent=window)
btn = QPushButton("update", parent=window)
btn.move(100, 100)

response = requests.get("http://192.168.1.120:8000/items/2")
data = json.loads(response.content)

window.show()
app.exec()

