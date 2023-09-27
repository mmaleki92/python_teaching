import sqlite3

# Connect to the database
# conn = sqlite3.connect(':memory:')  # Use in-memory database for demonstration
conn = sqlite3.connect('s.db')  # Use in-memory database for demonstration
cursor = conn.cursor()

# Create TableA and TableB
cursor.execute('''
CREATE TABLE TableA (
    key INTEGER PRIMARY KEY,
    valueA TEXT
)
''')

cursor.execute('''
CREATE TABLE TableB (
    key INTEGER PRIMARY KEY,
    valueB TEXT
)
''')

# Insert sample data into TableA and TableB
cursor.executemany("INSERT INTO TableA (key, valueA) VALUES (?, ?)", [(1, 'A1'), (2, 'A2'), (3, 'A3')])
cursor.executemany("INSERT INTO TableB (key, valueB) VALUES (?, ?)", [(1, 'B1'), (3, 'B3'), (4, 'B4')])
conn.commit()

# inner join
cursor.execute('''
SELECT TableA.key, TableA.valueA, TableB.valueB 
FROM TableA 
INNER JOIN TableB ON TableA.key = TableB.key
''')

print("INNER JOIN Results:")
for row in cursor.fetchall():
    print(row)

# 2. LEFT (OUTER) JOIN

cursor.execute('''
SELECT TableA.key, TableA.valueA, TableB.valueB 
FROM TableA 
LEFT JOIN TableB ON TableA.key = TableB.key
''')

print("\nLEFT JOIN Results:")
for row in cursor.fetchall():
    print(row)


# 3. CROSS JOIN
cursor.execute('''
SELECT TableA.key, TableA.valueA, TableB.valueB 
FROM TableA 
CROSS JOIN TableB
''')

print("\nCROSS JOIN Results:")
for row in cursor.fetchall():
    print(row)

