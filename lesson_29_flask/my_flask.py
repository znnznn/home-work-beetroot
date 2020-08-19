from flask import Flask, render_template, url_for

import oauthlib


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main_page():

    return render_template('index.html')


@app.route('/login')
def login_page():

    return render_template('login.html')


@app.route('/contacts')
def contacts_page():
    return render_template('contacts.html')


@app.route('/user')
def user_page():
    return render_template('user.html')


@app.route('/new_user')
def new_user_page():
    return render_template('new_user.html')


app.run(host='0.0.0.0', port='5000')