from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3
import hashlib

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

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    error = None # обнуляем переменную ошибок 
    if request.method == 'POST':
        username = request.form['username'] # обрабатываем запрос с нашей формы который имеет атрибут name="username"
        password = request.form['password'] # обрабатываем запрос с нашей формы который имеет атрибут name="password"
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest() # шифруем пароль в sha-256

        # устанавливаем соединение с БД
        conn = get_db_connection() 
        user = conn.execute(
            """SELECT * FROM users WHERE username = ?""", (username,)
            ).fetchone()
        conn.close() 

        if user and user['password'] == hashed_password:
            session['user_id'] = user['id']
            return redirect(url_for('admin_panel'))
        else:
            error = 'Wrong username/password combination'

    return render_template('admin_logpage.html', error=error)

@app.route('/admin_panel')
def admin_panel():
    # делаем доп проверку если сессия авторизации была создана 
    if 'user_id' not in session:
        return redirect(url_for('admin_logpage'))
    return render_template('admin_panel.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
