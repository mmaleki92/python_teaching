import os
import json

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonDatabase(metaclass=SingletonMeta):
    def __init__(self, filepath):
        if not hasattr(self, 'initialized'):  # This ensures initialization happens only once
            self.filepath = filepath
            self.data = self._load()
            self.initialized = True

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
db1 = SingletonDatabase('notes.json')
db1.add_note('First note')

db2 = SingletonDatabase('notes.json')
db2.add_note('Second note')

print(db1.get_notes())  # This will correctly include both notes
