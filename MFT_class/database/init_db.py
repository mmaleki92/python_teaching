import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    create_date TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    licence_number TEXT NOT NULL,
    approved TEXT NOT NULL,
    active_since TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INTEGER PRIMARY KEY,
    driver_id INTEGER,
    model TEXT,
    licence_plate TEXT,
    status TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    trip_id INTEGER,
    amount INTEGER,
    method TEXT,
    paid_on TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    trip_id INTEGER,
    rating INTEGER,
    comment TEXT,
    review_date TEXT
)
''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS reviews (
#     review_id INTEGER PRIMARY KEY,
#     trip_id INTEGER,
#     rating INTEGER,
#     comment TEXT,
#     review_date TEXT
# )
# ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS trips (
    trip_id INTEGER PRIMARY KEY,
    passenger_id  INTEGER,
    driver_id  INTEGER,
    vehicle_id  INTEGER,
    start_time  TEXT,
    end_time TEXT,
    pickup_location TEXT,
    dropoff_location TEXT,
    fare TEXT
)
''')

conn.commit()
conn.close()
