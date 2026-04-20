import csv

class VoteLogic:
    def __init__(self, filename="votes.csv") -> None:
        self.filename = filename
        self._votes = {'Isabella': 0, 'Genji': 0, 'Hannah': 0}

    def add_vote(self, candidate: str):
        if candidate in self._votes:
            self._votes[candidate] += 1
            self.save_to_csv(candidate)

    def save_to_csv(self, candidate):
        try:
            with open(self.filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([candidate])
        except Exception as e:
            print(f"Error saving: {e}")

    def get_results(self):
        return self._votes
