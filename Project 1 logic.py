import csv
import os


class VoteLogic:
    """Handles vote storage and CSV-backed vote totals."""

    def __init__(self, filename="votes.csv") -> None:
        self.filename = filename
        self._votes = {"Isabella": 0, "Genji": 0, "Hannah": 0}
        self._IDs = set()

        self.ensure_csv_exists()
        self.load_from_csv()

    def ensure_csv_exists(self) -> None:
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Candidate"])

    def load_from_csv(self) -> None:
        """Load vote totals and used IDs from the CSV file."""
        self._votes = {"Isabella": 0, "Genji": 0, "Hannah": 0}
        self._IDs = set()

        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                vote_id = row.get("ID", "").strip()
                candidate = row.get("Candidate", "").strip()

                if vote_id:
                    self._IDs.add(vote_id)

                if candidate in self._votes:
                    self._votes[candidate] += 1

    def add_vote(self, candidate: str, vote_id: str) -> bool:
        """Add a vote only if the ID has not already been used."""
        vote_id = vote_id.strip()
        candidate = candidate.strip()

        self.load_from_csv()

        if not vote_id:
            return False

        if vote_id in self._IDs:
            return False

        if candidate not in self._votes:
            return False

        self.save_to_csv(candidate, vote_id)
        self._IDs.add(vote_id)
        self._votes[candidate] += 1
        return True

    def save_to_csv(self, candidate: str, vote_id: str) -> None:
        """Save one vote row to the CSV file."""
        try:
            with open(self.filename, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([vote_id, candidate])
        except Exception as e:
            print(f"Error saving: {e}")

    def get_results(self) -> dict:
        """Return vote totals based on what is currently in the CSV file."""
        self.load_from_csv()
        return self._votes.copy()

    def id_exists(self, vote_id: str) -> bool:
        """Check whether a vote ID is already present in the CSV-backed set."""
        self.load_from_csv()
        return vote_id.strip() in self._IDs
