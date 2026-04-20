import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from logic import VoteLogic
from look import VoteView

class VoteController:
    def __init__(self) -> None:
        self.logic = VoteLogic()
        self.view = VoteView()

        self.has_voted = False

        self.view.isabella_button.clicked.connect(self.vote_isabella)
        self.view.genji_button.clicked.connect(self.vote_genji)
        self.view.hannah_button.clicked.connect(self.vote_hannah)
        self.view.results_button.clicked.connect(self.results)
        self.view.reset_button.clicked.connect(self.reset_vote)
        self.view.exit_button.clicked.connect(self.view.close)

    def show_message(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.exec()
    def disable_buttons(self):
        self.view.isabella_button.setEnabled(False)
        self.view.genji_button.setEnabled(False)
        self.view.hannah_button.setEnabled(False)

    def reset_vote(self):
        self.has_voted = False
        self.view.isabella_button.setEnabled(True)
        self.view.genji_button.setEnabled(True)
        self.view.hannah_button.setEnabled(True)

        self.show_message("Ready for next voter")
    def vote_isabella(self) -> None:
        if self.has_voted:
            self.show_message("You already voted!")
        else:
            self.logic.add_vote("Isabella")
            self.has_voted = True
            self.disable_buttons()
            self.show_message("Vote recorded for Isabella")
    def vote_genji(self) -> None:
        if self.has_voted:
            self.show_message("You already voted!")
        else:
            self.logic.add_vote("Genji")
            self.has_voted = True
            self.disable_buttons()
            self.show_message("Vote recorded for Genji")
    def vote_hannah(self) -> None:
        if self.has_voted:
            self.show_message("You already voted!")
        else:
            self.logic.add_vote("Hannah")
            self.has_voted = True
            self.disable_buttons()
            self.show_message("Vote recorded for Hannah")
    def results(self) -> None:
        results = self.logic.get_results()
        text = (
                f"Isabella: {results["Isabella"]}\n"
                f"Genji: {results["Genji"]}\n"
                f"Hannah: {results["Hannah"]}\n"
        )
        self.show_message(text)

    def run(self):
        self.view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = VoteController()
    controller.run()
    sys.exit(app.exec())
