# VM Activate
# source venv/bin/activate
# .\env\Scripts\activate

import sys
from PySide6.QtWidgets import QApplication
from main import Main

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
