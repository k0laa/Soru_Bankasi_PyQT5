import sqlite3


class Database:
    def __init__(self, db_name="data.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS sorular
                            (
                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,
                                soru
                                TEXT,
                                secenek1
                                TEXT,
                                secenek2
                                TEXT,
                                secenek3
                                TEXT,
                                secenek4
                                TEXT,
                                dogru_cevap
                                TEXT
                            )
                            """)
        self.connection.commit()

    def add_question(self, soru, secenek1, secenek2, secenek3, secenek4, dogru_cevap):
        self.cursor.execute("""
                            INSERT INTO sorular (soru, secenek1, secenek2, secenek3, secenek4, dogru_cevap)
                            VALUES (?, ?, ?, ?, ?, ?)
                            """, (soru, secenek1, secenek2, secenek3, secenek4, dogru_cevap))
        self.connection.commit()

    def delete_question(self, question_id):
        self.cursor.execute("DELETE FROM sorular WHERE id = ?", (question_id,))
        self.connection.commit()

    def get_all_questions(self):
        self.cursor.execute("SELECT * FROM sorular")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
