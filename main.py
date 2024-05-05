from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Устанавливаем соединение с Базой Данных
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
