from flask import (
    Flask, render_template,
    redirect, url_for, request,
    flash, session
    )
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (
    LoginManager, UserMixin,
    login_user, logout_user,
    login_requred, current_user
    )
from sqlalchemy import func
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = 'your_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'database.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

# Устанавливаем соединение с Базой Данных
# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
