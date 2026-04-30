from PyQt6.QtWidgets import QMessageBox
from logic import VoteLogic
from look import VoteView


class VoteController:
    """ Connects the GUI and the Logic """
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

    def show_message(self, text) -> None:
        """ Function that displays a popup message """
        msg = QMessageBox()
        msg.setText(text)
        msg.exec()

    def disable_buttons(self) -> None:
        """ Disables voting buttons after a vote."""
        self.view.isabella_button.setEnabled(False)
        self.view.genji_button.setEnabled(False)
        self.view.hannah_button.setEnabled(False)

    def reset_vote(self) -> None:
        """ Resets voting ability for the next user """
        self.has_voted = False
        self.view.isabella_button.setEnabled(True)
        self.view.genji_button.setEnabled(True)
        self.view.hannah_button.setEnabled(True)

        self.view.id_input.clear()
        self.show_message("Ready for next voter")
    def vote_isabella(self) -> None:
        """ Votes for Isabella """
        vote_id = self.view.id_input.text()
        if vote_id == "":
            self.show_message("Enter an ID!")
            return
        success = self.logic.add_vote("Isabella", vote_id)
        if not success:
            self.show_message("This ID already voted!")
        else:
            self.has_voted = True
            self.disable_buttons()
            self.view.message_label.setText("Vote recorded for Isabella")
    def vote_genji(self) -> None:
        """ Votes for Genji """
        vote_id = self.view.id_input.text()

        if vote_id == "":
            self.show_message("Enter an ID!")
            return
        success = self.logic.add_vote("Genji", vote_id)

        if not success:
            self.show_message("This ID already voted!")
        else:
            self.has_voted = True
            self.disable_buttons()
            self.view.message_label.setText("Vote recorded for Genji")
    def vote_hannah(self) -> None:
        """ Votes for Hannah """
        vote_id = self.view.id_input.text()

        if vote_id == "":
            self.show_message("Enter an ID!")
            return
        success = self.logic.add_vote("Hannah", vote_id)

        if not success:
            self.show_message("This ID already voted!")
        else:
            self.has_voted = True
            self.disable_buttons()
            self.view.message_label.setText("Vote recorded for Hannah")

    def results(self) -> None:
        """ Displays the current voting results. """
        results = self.logic.get_results()
        text = (
                f"Isabella: {results["Isabella"]}\n"
                f"Genji: {results["Genji"]}\n"
                f"Hannah: {results["Hannah"]}\n"
        )
        self.view.message_label.setText(text)

    def run(self) -> None:
        """ Runs the GUI"""
        self.view.show()
