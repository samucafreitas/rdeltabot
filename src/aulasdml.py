from os import path
import sqlite3

BASE_DIR = path.dirname(path.realpath(__file__))
DATABASE = path.join(BASE_DIR, '../db/db.db')

def close_commit(func):
    def magic(*args):
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        sql = func(*args)
        cur.execute(sql[0], sql[1])
        conn.commit()
        conn.close()
    return magic

@close_commit
def create(desc):
    return 'INSERT INTO aulas(description) VALUES(?)', (desc,)

@close_commit
def remove(aid):
    return 'DELETE FROM aulas WHERE id = ?', (aid,)

@close_commit
def update(aid, desc):
    return 'UPDATE aulas SET description = ? WHERE id = ?', (desc, aid)

def read():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT description FROM aulas WHERE id = (SELECT seq FROM sqlite_sequence)')
    data = cur.fetchone()
    conn.commit()
    conn.close()

    return data
