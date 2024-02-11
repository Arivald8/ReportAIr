import sqlite3

class DB:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(self.name)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()
