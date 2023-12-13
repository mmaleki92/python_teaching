import sqlite3

class SchoolDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                StudentID INTEGER PRIMARY KEY,
                Name TEXT,
                Age INTEGER,
                Class TEXT
            );
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Teachers (
                TeacherID INTEGER PRIMARY KEY,
                Name TEXT,
                Subject TEXT
            );
        ''')
        # Add other table creations here
        self.conn.commit()

    def add_student(self, name, age, class_name):
        self.conn.execute('INSERT INTO Students (Name, Age, Class) VALUES (?, ?, ?)', (name, age, class_name))
        self.conn.commit()

    # Add other methods for interacting with the database

school_db = SchoolDB('school.db')
school_db.add_student('John Doe', 15, '10A')
