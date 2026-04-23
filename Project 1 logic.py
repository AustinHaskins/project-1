import csv

class VoteLogic:
    """ Handles vote storage and the file name """
    def __init__(self, filename="votes.csv") -> None:
        self.filename = filename
        self._votes = {'Isabella': 0, 'Genji': 0, 'Hannah': 0}
        self._ID = set()

    def add_vote(self, candidate: str, vote_id: str) -> bool:
        """ Adds a vote for a given candidate and saves it to CSV."""
        if vote_id in self._votes:
            return False
        if candidate in self._votes:
            self._votes[candidate] += 1
            self._ID.add(vote_id)
            self.save_to_csv(candidate, vote_id)
            return True
        return False
    def save_to_csv(self, candidate, vote_id):
        """ Saves the vote to the CSV file """
        try:
            with open(self.filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([vote_id, candidate])
        except Exception as e:
            print(f"Error saving: {e}")

    def get_results(self):
        """ Returns the current vote counts """
        return self._votes
