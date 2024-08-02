import sqlite3
import pandas as pd

conn = sqlite3.connect('example.db')

df = pd.read_sql_query("SELECT * FROM users", conn)

df.to_excel("example.xlsx")