from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


class VoteView(QWidget):
    """ GUI class for the voting """
    def __init__(self) -> None:
        """ set's up the GUI's layout and widgets"""
        super().__init__()
        self.setWindowTitle("Voting")
        self.setFixedSize(600, 600)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        title = QLabel("Vote for the Candidate")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter Voter ID")
        layout.addWidget(self.id_input)

        self.isabella_button = QPushButton("Vote Isabella")
        self.genji_button = QPushButton("Vote Genji")
        self.hannah_button = QPushButton("Vote Hannah")
        self.results_button = QPushButton("Show Results")
        self.reset_button = QPushButton("Next Voter")
        self.exit_button = QPushButton("Exit")

        layout.addSpacing(25)
        layout.addWidget(self.isabella_button)
        layout.addSpacing(10)
        layout.addWidget(self.genji_button)
        layout.addSpacing(10)
        layout.addWidget(self.hannah_button)
        layout.addSpacing(20)
        layout.addWidget(self.results_button)
        layout.addSpacing(10)
        layout.addWidget(self.reset_button)
        layout.addSpacing(10)
        layout.addWidget(self.exit_button)

        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.message_label)
        self.setLayout(layout)
