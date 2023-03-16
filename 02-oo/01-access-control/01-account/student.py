class Account:
    def __init__(self, login, secret):
        self.login = login
        self.__secret = secret

    def is_correct_password(self, pw):
        return self.__secret == pw