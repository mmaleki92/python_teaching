import sqlite3
from datetime import datetime

class MetroSystem:
    def __init__(self, db_name="metro_system.db"):
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        # Establish connection and create tables if they do not exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    card_id TEXT UNIQUE NOT NULL,
                    balance REAL DEFAULT 0.0
                )
            """)
            # Transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    card_id TEXT NOT NULL,
                    amount REAL NOT NULL,
                    transaction_type TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (card_id) REFERENCES users(card_id)
                )
            """)

    def register_user(self, name, card_id):
        # Add a new user to the database
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (name, card_id) VALUES (?, ?)
                """, (name, card_id))
                print(f"User {name} registered successfully.")
        except sqlite3.IntegrityError:
            print("Card ID already exists. Registration failed.")

    def add_credit(self, card_id, amount):
        # Add credit to a user's card
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE users SET balance = balance + ? WHERE card_id = ?
            """, (amount, card_id))
            if cursor.rowcount > 0:
                cursor.execute("""
                    INSERT INTO transactions (card_id, amount, transaction_type, timestamp)
                    VALUES (?, ?, ?, ?)
                """, (card_id, amount, 'credit', datetime.now().isoformat()))
                print(f"Added ${amount:.2f} to card {card_id}.")
            else:
                print("Card ID not found.")

    def enter_metro(self, card_id, fare):
        # Deduct fare from a user's card balance when they enter the metro
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT balance FROM users WHERE card_id = ?
            """, (card_id,))
            result = cursor.fetchone()
            if result:
                current_balance = result[0]
                if current_balance >= fare:
                    cursor.execute("""
                        UPDATE users SET balance = balance - ? WHERE card_id = ?
                    """, (fare, card_id))
                    cursor.execute("""
                        INSERT INTO transactions (card_id, amount, transaction_type, timestamp)
                        VALUES (?, ?, ?, ?)
                    """, (card_id, -fare, 'debit', datetime.now().isoformat()))
                    print(f"Fare ${fare:.2f} deducted. Remaining balance: ${current_balance - fare:.2f}")
                else:
                    print("Insufficient balance. Please recharge your card.")
            else:
                print("Card ID not found.")

    def check_balance(self, card_id):
        # Check the balance of a user's card
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT balance FROM users WHERE card_id = ?
            """, (card_id,))
            result = cursor.fetchone()
            if result:
                print(f"Card {card_id} balance: ${result[0]:.2f}")
            else:
                print("Card ID not found.")

    def generate_report(self, report_type="transactions"):
        # Generate a report of all transactions or users
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            if report_type == "transactions":
                cursor.execute("""
                    SELECT * FROM transactions
                """)
                transactions = cursor.fetchall()
                print("Transactions Report:")
                for trans in transactions:
                    print(trans)
            elif report_type == "users":
                cursor.execute("""
                    SELECT * FROM users
                """)
                users = cursor.fetchall()
                print("Users Report:")
                for user in users:
                    print(user)
            else:
                print("Invalid report type. Choose 'transactions' or 'users'.")

# Usage example
if __name__ == "__main__":
    metro = MetroSystem()

    # Register users
    metro.register_user("Alice", "CARD123")
    metro.register_user("Bob", "CARD456")

    # Add credit
    metro.add_credit("CARD123", 50)
    metro.add_credit("CARD456", 30)

    # Check balance
    metro.check_balance("CARD123")

    # Enter metro (deduct fare)
    metro.enter_metro("CARD123", 2.5)
    metro.enter_metro("CARD456", 5)

    # Generate reports
    metro.generate_report("users")
    metro.generate_report("transactions")
