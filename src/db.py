from os import path
import sqlite3

BASE_DIR = path.dirname(path.realpath(__file__))
DATABASE = path.join(BASE_DIR, '../db/db.db')

def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute('''PRAGMA foreign_keys = ON''')

    cur.execute('''CREATE TABLE IF NOT EXISTS aulas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description VARCHAR(150) NOT NULL,
                        dt_registration TIMESTAMP DEFAULT (DATETIME('now', 'localtime')))''')

    conn.commit()
    conn.close()
