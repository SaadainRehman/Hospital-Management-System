class User:
    def __init__(self , username , password , role):
        self._username = username 
        self._password = password 
        self._role = role

    def validate_pass(self , password):
        return self.password == password