import json
import uuid
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.id = str(uuid.uuid4())  # Generates a unique ID for each note
        self.title = title
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def update(self, title, content):
        self.title = title
        self.content = content

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'content': self.content, 'created_at': self.created_at}

class Notebook:
    def __init__(self, filename='notebook.json'):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def update_note_by_index(self, index, title, content):
        if 0 <= index < len(self.notes):
            self.notes[index].update(title, content)
            self.save_notes()
            return True
        return False

    def delete_note_by_index(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.save_notes()
            return True
        return False


    def add_note(self, title, content):
        self.notes.append(Note(title, content))
        self.save_notes()

    def update_note(self, note_id, title, content):
        note = self.find_note_by_id(note_id)
        if note:
            note.update(title, content)
            self.save_notes()
            return True
        return False

    def delete_note(self, note_id):
        note = self.find_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            return True
        return False

    def get_note(self, note_id):
        note = self.find_note_by_id(note_id)
        if note:
            return note.to_dict()
        return None

    def list_notes(self):
        return [note.to_dict() for note in self.notes]

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                notes_raw = json.load(file)
                for note in notes_raw:
                    restored_note = Note(note['title'], note['content'])
                    restored_note.id = note['id']  # Restoring the ID from the file
                    self.notes.append(restored_note)
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.list_notes(), file, indent=4)

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

# # Example usage:
# notebook = Notebook()
# notebook.add_note("Sample Note", "This is a sample note.")
# print(notebook.list_notes())

# # Updating a note by ID
# note_id = notebook.list_notes()[0]['id']  # Assuming you want to update the first note
# notebook.update_note(note_id, "Updated Sample Note", "This is an updated sample note.")
# print(notebook.list_notes())

# # Deleting a note by ID
# notebook.delete_note(note_id)
# print(notebook.list_notes())



def main():
    notebook = Notebook()
    commands = {
        'add': add_note,
        'update': update_note,
        'delete': delete_note,
        'list': list_notes,
        'exit': exit_app
    }

    while True:
        cmd = input("Enter command (add, update, delete, list, exit): ").strip().lower()
        if cmd in commands:
            commands[cmd](notebook)
        else:
            print("Unknown command. Please try again.")


def add_note(notebook):
    title = input("Enter note title: ").strip()
    print("Enter note content (type 'EOF' on a new line to finish):")
    content_lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        content_lines.append(line)
    content = "\n".join(content_lines)
    notebook.add_note(title, content)
    print("Note added successfully.")

def update_note(notebook):
    notebook.list_notes()  # Display the list of notes for user reference
    try:
        note_index = int(input("Enter the index of the note to update: ").strip())
        title = input("Enter new note title: ").strip()
        print("Enter new note content (type 'EOF' on a new line to finish):")
        content_lines = []
        while True:
            line = input()
            if line == "EOF":
                break
            content_lines.append(line)
        content = "\n".join(content_lines)
        if notebook.update_note_by_index(note_index, title, content):
            print("Note updated successfully.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric index.")


def delete_note(notebook):
    notebook.list_notes()  # Display the list of notes for user reference
    try:
        note_index = int(input("Enter the index of the note to delete: ").strip())
        if notebook.delete_note_by_index(note_index):
            print("Note deleted successfully.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric index.")


def list_notes(notebook):
    notes = notebook.list_notes()
    if notes:
        for index, note in enumerate(notes):
            print(f"Index: {index}, ID: {note['id']}, Title: {note['title']}, Created At: {note['created_at']}")
            print(f"Content:\n{note['content']}\n")
    else:
        print("No notes found.")

def exit_app(notebook):
    print("Exiting application.")
    exit(0)

def exit_app(notebook):
    print("Exiting application.")
    exit(0)

if __name__ == "__main__":
    main()
