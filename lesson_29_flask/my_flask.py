import psycopg2
import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, redirect, g, flash
from flask_login import LoginManager, login_required, login_user, logout_user

from lesson_29_flask.userLogin_flask import UserLogin
from lesson_29_flask.db_flask import DataBase
from lesson_29_flask.http_request import api_stock
import oauthlib
# @login_required для сторінок які лише авторизованим юзерам

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f51ab319da5bb46ec221f7da979833a35250c86e'

login_manager = LoginManager(app)

stocks = {
    'WMT': "Wal-Mart Stores, Inc.",
    "MCD": "McDonald’s Corp.",
    "JNJ": "Johnson & Johnson Inc.",
    "JPM": "JPMorgan Chase and Co.",
    "MSFT": "Microsoft Corp."
 }


@app.route('/')
@app.route('/index')
def main_page():

    return render_template('index.html', title='Головна сторінка')


@login_manager.user_loader
def load_user(user_id):
    return UserLogin(user_id).user_db(user_id)


@app.route('/login', methods=["POST", "GET"])
def login_page():

    if request.method == 'POST':

        data_user = dict(request.form)
        user = DataBase(data_user)
        user_id = user.take_user()
        print(data_user['password'])
        if user_id and check_password_hash(user_id['password'], data_user['password']):
            print(5)
            userLogin = UserLogin(user_id).user_id(user_id)
            login_user(userLogin)
            return redirect(url_for('user_page'))
        else:
            flash('Невірно введений email або пароль')
            return redirect(url_for('login_page'))
    print(10)
    return render_template('login.html', title='Авторизація')


@app.route('/contacts')
def contacts_page():
    return render_template('contacts.html', title='Контакти')


@app.route('/user', methods=['GET', 'POST'])
@login_required
def user_page(name=None):
    user_name = name
    if request.method == 'POST':
        pass
    list_stock = api_stock()

    return render_template('user.html',  title=f'{user_name}')


@app.route('/new_user', methods=['POST', 'GET'])
def new_user_page():
    if request.method == 'POST':
        data_new_user = dict(request.form)
        if '' in data_new_user.values() or ' ' in data_new_user.values():
            flash('Поля мають бути заповненими')
            return redirect(url_for('new_user_page'))
        elif not data_new_user['firstName'].isalpha() or not data_new_user['lastName'].isalpha():
            flash("Поле ім\'я або фамілія має містити лише букви")
            return redirect(url_for('new_user_page'))
        elif '@' not in data_new_user['email'] or '.' not in data_new_user['email']:
            flash('Невірно введений формат електронної пошти')
            return redirect(url_for('new_user_page'))
        elif data_new_user['password'] != data_new_user['password2']:
            flash('Введені паролі не рівні')
            return redirect(url_for('new_user_page'))
        for key, values in data_new_user.items():  # треба дізнатись чи треба паролі стріпати
            data_new_user[key] = values.strip()
        data_new_user['password'] = generate_password_hash(data_new_user['password'])
        data_new_user.pop('password2')
        data_new_user['date'] = str(datetime.datetime.today())
        new_user = DataBase(data_new_user)
        db_user = new_user.add_user()
        if db_user:
            flash('Ви успішно зареєструвались')
            return redirect(url_for('login_page'))
        flash(f"Користувач з такими даними вже існує")
        return redirect(url_for('new_user_page'))
    return render_template('new_user.html', title='Реєстрація')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout_page():
    logout_user()
    flash('Ви вийшли  кабінету')
    return redirect(url_for('main_page'))


@app.teardown_appcontext
def close(error):

    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def error_page(error):
    return render_template('error_page.html', title='Сторінку не знайдено'), 404


app.run(host='0.0.0.0', port='5000', debug=True)



"""@app.after_request
@app.before_request
@app.before_first_request
@app.teardown_request"""