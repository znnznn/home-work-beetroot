import json
from flask_login import UserMixin
from lesson_29_flask.db_flask import DataBase


class UserLogin(UserMixin, DataBase):

    def user_db(self, user):
        self.user = DataBase(user).take_user_id()
        return self

    def user_id(self, user):
        self.user = user
        return self

    def get_id(self):
        user = str(self.user['id'])
        return user

    def user_data(self):
        return self.user

