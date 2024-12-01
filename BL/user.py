class User:
    def __init__(self, username, password, role):
        self._username = username  
        self._password = password
        self._role = role

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def role(self):
        return self._role


    def validate_password(self , password):
        return self._password == password