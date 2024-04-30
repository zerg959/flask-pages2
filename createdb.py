import sqlite3
conn = sqlite3.connect('database.db')

# Создание курсора
cur = conn.cursor()

# Создание таблицы Posts
cur.execute('''CREATE TABLE IF NOT EXISTS posts (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             img TEXT,
             title TEXT,
             content TEXT,
             author TEXT,
             timestampdata DATETIME)''')

# Создание таблицы Users
cur.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT,
             password TEXT)''')

# Закрытие соединения с базой данных
conn.close()