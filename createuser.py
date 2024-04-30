import sqlite3
import hashlib


def create_user(username, password):
    hash_psw = hashlib.sha256(password.encode('utf-8')).hexdigest()
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO users (
                username, password
                ) VALUES (?, ?)""", (username, hash_psw))
    conn.commit()
    conn.close()


create_user('zerg959', 'KX@Jan1982')
