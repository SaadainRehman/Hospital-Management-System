from BL.user import User
class UserDL:
    def __init__(self):
        self.Users = []

    def add(self,user):
        print(type(user))
        self.Users.append(user)
        return True

    def show(self):
        print(self.Users)
        