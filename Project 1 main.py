import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from controller import VoteController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = VoteController()
    controller.run()
    sys.exit(app.exec())
