import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Re-run the program with admin rights, might not work if the user doesn't have admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class DNSChangerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()

        # Widgets
        self.primary_dns_input = QLineEdit(self)
        self.secondary_dns_input = QLineEdit(self)
        apply_button = QPushButton('Apply DNS', self)
        deactivate_button = QPushButton('Deactivate Custom DNS', self)

        # Layout Setup
        layout.addWidget(QLabel("Primary DNS:"))
        layout.addWidget(self.primary_dns_input)
        layout.addWidget(QLabel("Secondary DNS:"))
        layout.addWidget(self.secondary_dns_input)
        layout.addWidget(apply_button)
        layout.addWidget(deactivate_button)

        # Signals and Slots
        apply_button.clicked.connect(self.change_dns)
        deactivate_button.clicked.connect(self.deactivate_dns)

        # Set Layout
        self.setLayout(layout)
        self.setWindowTitle('DNS Changer for Windows')
        self.show()

    def change_dns(self):
         
        primary_dns = self.primary_dns_input.text()
        secondary_dns = self.secondary_dns_input.text()
        if primary_dns == "" or secondary_dns=="":
            print("using Shecan!")
            primary_dns = "178.22.122.100"
            secondary_dns = "185.51.200.2"
        # For simplicity, we're assuming the network adapter is named "Wi-Fi". Modify as per your system.
        command1 = f"netsh interface ip set dns name=\"Ethernet\" static {primary_dns} primary"
        command2 = f"netsh interface ip add dns name=\"Ethernet\" addr={secondary_dns} index=2"
        
        result1 = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        result2 = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        
        out1, err1 = result1.communicate()
        out2, err2 = result2.communicate()

        if err1:
            # Display the error in your GUI
            print(err1.decode('utf-8'))
        if err2:
            # Display the error in your GUI
            print(err2.decode('utf-8'))
        
    def deactivate_dns(self):
        # This command will set the DNS settings to be obtained automatically.
        command = f"netsh interface ip set dns name=\"Ethernet\" dhcp"
        
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        
        out, err = result.communicate()
        
        if err:
            # Display the error in your GUI
            print(err.decode('utf-8'))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DNSChangerApp()
    sys.exit(app.exec_())
