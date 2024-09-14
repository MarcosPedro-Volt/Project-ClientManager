
import sys
from PySide6.QtWidgets import (QApplication)
from client_app import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientApp()
    window.show()
    sys.exit(app.exec())