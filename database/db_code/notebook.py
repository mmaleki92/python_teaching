import sqlite3

class NotebookDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Notes (
                NoteID INTEGER PRIMARY KEY,
                Title TEXT,
                Content TEXT,
                Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        # Add other table creations here
        self.conn.commit()

    def add_note(self, title, content):
        self.conn.execute('INSERT INTO Notes (Title, Content) VALUES (?, ?)', (title, content))
        self.conn.commit()

    # Add other methods for interacting with the database

notebook_db = NotebookDB('notebook.db')
notebook_db.add_note('Meeting Notes', 'Discussed project milestones...')
