import json
from datetime import datetime

class Note:
    def __init__(self):
        self.title = input("Title:")
        self.note = input("Note:")
        self.date = str(datetime.now()) 

class ShowNotes:
    def __init__(self, notebook):
        self.notebook = notebook

    def show_1(self):
        for n in self.notebook:
            print("Title", n.title)
            print("note", n.note)
            print("Date:", n.date)
            print("-" * 10)

    def show_2(self):
        for n in self.notebook:
            print("Title", n.title)
            # print("note", n.note)
            # print("Date:", n.date)
            print("-" * 10)

class Storage:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_json():
        with open(self.file_name, "w") as f:
            json.dump(self.notebook, f)

    def load_json():
        pass

def add_note(notebook):
    """add note to notebook"""
    note = Note()
    notebook.append(note)
    return notebook

def show_notes(notebook):
    """show notebook notes"""
    show_notes = ShowNotes(notebook)
    show_notes.show_1()

notebook = []

while True:
    x = input("""
0: add note
1: end
2: show
3: store
""")
    if x == "0":
        notebook = add_note(notebook)
    elif x == "1":
        break
    elif x == "2":
        show_notes(notebook)
    elif x == "3":
        
