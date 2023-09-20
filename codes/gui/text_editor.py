import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
import yaml

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create a text edit widget
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        
        # Create menu actions
        self.open_action = QAction('Open', self)
        self.open_action.triggered.connect(self.open_file)
        self.save_action = QAction('Save', self)
        self.save_action.triggered.connect(self.save_file)
        
        # Create menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        
        # Set window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('YAML Editor')
        self.show()
        
        # Store data as dictionary
        self.data = {}
    
    def open_file(self):
        # Open file dialog to select YAML file
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open YAML File', '', 'YAML Files (*.yaml *.yml)')
        
        if file_name:
            # Load YAML file into dictionary
            with open(file_name, 'r') as f:
                self.data = yaml.load(f, Loader=yaml.FullLoader)
            
            # Display YAML data in text edit widget
            self.text_edit.setText(yaml.dump(self.data, indent=4))
    
    def save_file(self):
        # Open file dialog to save YAML file
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save YAML File', '', 'YAML Files (*.yaml *.yml)')
        
        if file_name:
            # Save text edit contents to dictionary
            self.data = yaml.safe_load(self.text_edit.toPlainText())
            
            # Write dictionary to YAML file
            with open(file_name, 'w') as f:
                yaml.dump(self.data, f, default_flow_style=False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
