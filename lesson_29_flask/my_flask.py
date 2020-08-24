import psycopg2

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, session, redirect, g, flash
from flask_login import LoginManager, login_required, login_user

from lesson_29_flask.userLogin_flask import UserLogin
from lesson_29_flask.db_flask import DataBase
import oauthlib
# @login_required для сторінок які лише авторизованим юзерам

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f51ab319da5bb46ec221f7da979833a35250c86e'

#user_now = LoginManager(app)

stocks = {
    'WMT': "Wal-Mart Stores, Inc.",
    "MCD": "McDonald’s Corp.",
    "JNJ": "Johnson & Johnson Inc.",
    "JPM": "JPMorgan Chase and Co.",
    "MSFT": "Microsoft Corp."
 }


def data_base(user):
    if not hasattr(g, 'link_db'):
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                      user='postgres', password='postgres')
        cursor = connection.cursor()
        work_base = DataBase(connection, cursor, user)
        return work_base


@app.route('/')
@app.route('/index')
def main_page():

    return render_template('index.html', title='Головна сторінка')


@app.route('/login', methods=["POST", "GET"])
def login_page():
    print(1)
    if request.method == 'POST':
        print(2)
        data_user = {
            'email': request.form['email'],
            'password': request.form['inputPassword']
        }
        user = data_base(data_user).take_user()
        if user and check_password_hash(user['password'], data_user['password']):
            user_now = UserLogin().user(user)
            login_user(user_now)
            return redirect(url_for('user_page'))
        flash('Невірно введений emal або пароль')
    elif request.method == 'POST' and request.form['user'] == '1234@ukr.net' and request.form['inputPassword'] == '1234':
        print(3)
        session['user'] = request.form['user']
        return redirect(url_for('user_page', user=session['user']))
    print(4)
    return render_template('login.html', title='Авторизація')


@app.route('/contacts')
def contacts_page():
    return render_template('contacts.html', title='Контакти')


@app.route('/user', methods=['GET', 'POST'])
@login_required
def user_page(name=None):
    user_name = name
    #print(request.form)
    return render_template('user.html',  title=f'{user_name}')


@app.route('/new_user')
def new_user_page():
    return render_template('new_user.html', title='Регістрація')


@app.teardown_appcontext
def close(error):

    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def error_page(error):
    return render_template('error_page.html', title='Сторінку не знайдено'), 404


app.run(host='0.0.0.0', port='5000')


"""@app.after_request
@app.before_request
@app.before_first_request
@app.teardown_request"""