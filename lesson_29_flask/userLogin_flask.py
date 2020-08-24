import json


class UserLogin:

    def user_db(self, user_id, db):
        self.user = db.get_user(user_id)
        return self

    def user(self, user):
        self.user = user
        return self

    def is_autheticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user['id'])

