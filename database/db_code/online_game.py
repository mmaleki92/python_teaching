import sqlite3

class GameDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                UserID INTEGER PRIMARY KEY,
                Username TEXT,
                Email TEXT
            );
        ''')
        # Add other table creations here
        self.conn.commit()

    def add_user(self, username, email):
        self.conn.execute('INSERT INTO Users (Username, Email) VALUES (?, ?)', (username, email))
        self.conn.commit()

    # Add other methods for interacting with the database

game_db = GameDB('game.db')
game_db.add_user('player1', 'player1@example.com')
