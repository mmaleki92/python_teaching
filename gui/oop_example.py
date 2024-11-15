import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)

class CustomListItemWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        
        # Create layout
        main_layout = QHBoxLayout()
        
        # Create widgets to add to layout
        label = QLabel(text)
        button = QPushButton("Click Me")
        
        # Add widgets to layout
        main_layout.addWidget(label)
        main_layout.addWidget(button)
        
        # Set the layout for the custom widget
        self.setLayout(main_layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        main_layout = QVBoxLayout(self)
        
        # Create a QListWidget
        self.list_widget = QListWidget()
        
        # Add items with custom widgets to the list
        for i in range(5):
            item_text = f"Item {i + 1}"
            
            # Create a QListWidgetItem
            list_item = QListWidgetItem()
            
            # Create a custom widget with layout for each item
            custom_widget = CustomListItemWidget(item_text)
            
            # Set the custom widget for the list item
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, custom_widget)
        
        # Add QListWidget to the main layout
        main_layout.addWidget(self.list_widget)
        
        # Set layout for main window
        self.setLayout(main_layout)

# Application code
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
