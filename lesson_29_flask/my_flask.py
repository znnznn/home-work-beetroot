import psycopg2
import datetime
import json
import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, redirect, g, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from lesson_29_flask.userLogin_flask import UserLogin
from lesson_29_flask.db_flask import DataBase
from lesson_29_flask.tradier_api import symbol_stocks
from lesson_29_flask.http_request import user_list
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
    user = UserLogin(user_id).user_db(user_id)
    return user


@app.route('/login', methods=["POST", "GET"])
def login_page():

    if current_user.is_authenticated:
        return redirect(url_for('user_page'))
    if request.method == 'POST':
        data_user = dict(request.form)
        user = DataBase(data_user)
        user_id = user.take_user()
        if user_id and check_password_hash(user_id['password'], data_user['password']):
            remember_me = True if data_user.get('remember') else False
            userLogin = UserLogin(user_id).user_id(user_id)
            login_user(userLogin, remember=remember_me)
            return redirect(url_for('user_page'))
        else:
            flash('Невірно введений email або пароль')
            return redirect(url_for('login_page'))
    return render_template('login.html', title='Авторизація')


@app.route('/contacts',  methods=['POST', 'GET'])
def contacts_page():
    if request.method == 'POST':
        data_user = dict(request.form)
        for key, values in data_user.items():
            data_user[key] = values.strip()
        if "" in data_user.values():
            flash('Всі поля мають бути заповненими')
            return redirect(url_for('contacts_page'))
        data_user['date'] = str(datetime.datetime.today())
        user = DataBase(data_user)
        message = user.add_message()
        if message:
            flash('Повідомлення успішно відправлено')
            return render_template('contacts.html', title='Контакти')
        flash("Сталась помилка з\'єднання з базою даних")
        return redirect(redirect(url_for('contacts_page')))
    return render_template('contacts.html', title='Контакти')


@app.route('/user', methods=['GET', 'POST'])
@login_required
def user_page():
    t1 = time.time()
    user_id = current_user.user_data()
    user_name = user_id.get('username')
    if request.method == 'POST':
        list_stock = stocks
    with open('stocks.json', 'r') as file_stocks:
        list_stocks = json.load(file_stocks)
        my_stocks = list_stocks['securities']['security']
        my_stocks = sorted(my_stocks, key=lambda symbol: symbol['symbol'])
    i = 0
    while i != 110:
        data_symbol = symbol_stocks(my_stocks[i]['symbol'])
        my_stocks[i]['quote'] = data_symbol['quotes']['quote']
        i += 1
    print(time.time()-t1, 555)
    return render_template('user.html',  title=f'{user_name}', stocks=my_stocks)


@app.route('/user/profile', methods=['GET', 'POST'])
@login_required
def profile_page():
    user_id = current_user.user_data()
    if request.method == 'POST':
        user = dict(request.form)
        if '' in user.values() or ' ' in user.values():
            flash('Поля мають бути заповненими')
            return redirect(url_for('profile_page'))
        elif not user['firstName'].isalpha() or not user['lastName'].isalpha():
            flash("Поле ім\'я або фамілія має містити лише букви")
            return redirect(url_for('profile_page'))
        elif '@' not in user['email'] or '.' not in user['email']:
            flash('Невірно введений формат електронної пошти')
            return redirect(url_for('profile_page'))
        elif user['password'] != user['password2']:
            flash('Введені паролі не рівні')
            return redirect(url_for('profile_page'))
        for key, values in user.items():  # треба дізнатись чи треба паролі стріпати
            user[key] = values.strip()
        user['id'] = user_id['id']
        user['password'] = generate_password_hash(user['password'])
        user.pop('password2')
        user['date'] = str(datetime.datetime.today())
        user_edit = DataBase(user)
        db_user = user_edit.edit_user()
        if db_user:
            flash(f"{user['username']}, Ви успішно змінили особисті дані")
            return redirect(url_for('user_page'))
        flash(f"Користувач з {user['email']} вже існує")
        return redirect(url_for('new_user_page'))
    return render_template('profile_user.html', title='Профіль', username=user_id)


@app.route('/user/profile/delete', methods=['GET', 'POST'])
@login_required
def del_profile_page():
    user_id = current_user.user_data()
    username = user_id.get('username')
    if request.method == 'POST':
        logout_user()
        del_user = DataBase(user_id).del_user()
        flash(f'Нажаль {username} вас видалено.')
        return redirect(url_for('main_page'))
    flash(f'Ви впевненні {username}, що хочете себе видалити')
    return render_template('delete_profile.html', title='Видалення профілю !!!', username=user_id)


@app.route('/new_user', methods=['POST', 'GET'])
def new_user_page():
    if current_user.is_authenticated:
        return redirect(url_for('user_page'))
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
            flash(f"{data_new_user['username']}, Ви успішно зареєструвались.")
            return redirect(url_for('login_page'))
        flash(f"Користувач з {data_new_user['email']} вже існує.")
        return redirect(url_for('new_user_page'))
    return render_template('new_user.html', title='Реєстрація')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout_page():
    user_id = current_user.user_data()
    username = user_id.get('username')
    logout_user()
    flash(f'{username}, Ви вийшли з кабінету.')
    return redirect(url_for('main_page'))


@app.teardown_appcontext
def close(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(401)
def error_page(error):
    flash('Авторизуйтесь будь ласка')
    return redirect(url_for('login_page')), 401


@app.errorhandler(404)
def error_page1(error):
    flash('Авторизуйтесь будь ласка')
    return render_template('login.html', title='Авторизація'), 404


app.run(host='0.0.0.0', port='5000', debug=True)



"""@app.after_request
@app.before_request
@app.before_first_request
@app.teardown_request"""