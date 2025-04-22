import sqlite3

class Database:
    def __init__(self, db_name="data.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sorular (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            soru TEXT,
            secenek1 TEXT,
            secenek2 TEXT,
            secenek3 TEXT,
            secenek4 TEXT,
            dogru_cevap TEXT
        )
        """)
        self.connection.commit()
