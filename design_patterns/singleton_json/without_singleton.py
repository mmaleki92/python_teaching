import json
import os

class Database:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, 'r') as file:
            return json.load(file)

    def add_note(self, note):
        self.data.setdefault('notes', []).append(note)
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file)

    def get_notes(self):
        return self.data.get('notes', [])

# Example usage:
db1 = Database('notes.json')
db1.add_note('First note')

db2 = Database('notes.json')
db2.add_note('Second note')

print(db1.get_notes())  # This might not include 'Second note' due to db2 overwriting the file
