import sqlite3

def connect_db():
    return sqlite3.connect("example.db")

def create_user(user):
    con = connect_db()
    cur = con.cursor()

    cur.execute("""INSERT INTO users (username, email, phone_number, create_date) VALUES (?, ?, ?, ?)""", (
        user.username,
        user.email,
        user.phone_number,
        user.create_date))
    con.commit()
    cur.close()
    con.close()

