import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
from mendeleev import element



def show_element_info(element_symbol):
    # Fetch element data using mendeleev
    el = element(element_symbol)

    # Prepare the message box content
    info = f"Name: {el.name}\nSymbol: {el.symbol}\nAtomic Number: {el.atomic_number}\nAtomic Weight: {el.atomic_weight}\n" \
           f"Electron Configuration: {el.ec}"

    # Show message box
    msg = QMessageBox()
    msg.setWindowTitle(el.name)
    msg.setText(info)
    msg.exec_()

    
def create_periodic_table():
    # Define the elements (partial list for brevity)
    elements = {
        'H': (1, 1), 'He': (18, 1),
        'Li': (1, 2), 'Be': (2, 2), 'B': (13, 2), 'C': (14, 2), 'N': (15, 2), 'O': (16, 2), 'F': (17, 2), 'Ne': (18, 2),
        'Na': (1, 3), 'Mg': (2, 3), 'Al': (13, 3), 'Si': (14, 3), 'P': (15, 3), 'S': (16, 3), 'Cl': (17, 3), 'Ar': (18, 3),
        'K': (1, 4), 'Ca': (2, 4), 'Sc': (3, 4), 'Ti': (4, 4), 'V': (5, 4), 'Cr': (6, 4), 'Mn': (7, 4), 'Fe': (8, 4),
        'Co': (9, 4), 'Ni': (10, 4), 'Cu': (11, 4), 'Zn': (12, 4), 'Ga': (13, 4), 'Ge': (14, 4), 'As': (15, 4), 'Se': (16, 4),
        'Br': (17, 4), 'Kr': (18, 4),
        'Rf': (4, 7), 'Db': (5, 7), 'Sg': (6, 7), 'Bh': (7, 7), 'Hs': (8, 7), 'Mt': (9, 7), 'Ds': (10, 7), 'Rg': (11, 7),
        'Cn': (12, 7), 'Nh': (13, 7), 'Fl': (14, 7), 'Mc': (15, 7), 'Lv': (16, 7), 'Ts': (17, 7), 'Og': (18, 7)
    }

    # Create the application and the main window
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Periodic Table')

    # Create a grid layout
    layout = QGridLayout(window)

    # Add buttons for each element
    for symbol, (x, y) in elements.items():
        button = QPushButton(symbol)
        button.clicked.connect(lambda _, s=symbol: show_element_info(s))
        layout.addWidget(button, y, x)  # Row, Column

    # Set the layout and show the window
    window.setLayout(layout)
    window.show()

    # Run the application
    sys.exit(app.exec_())

if __name__ == '__main__':
    create_periodic_table()
