from BL.user import User

class UserDL:
    def __init__(self):
        self.Users = []  
    def sign_up(self, username, password, role):
        for existing_user in self.Users:
            if existing_user.username == username:  
                print("This User Already Exists")
                return False

        new_user = User(username, password, role)
        self.Users.append(new_user)
        print("New User Signed Up Successfully")
        return True

    def sign_in(self, username, password):
        for existing_user in self.Users:
            if existing_user.username == username: 
                if existing_user.password == password:
                    print(f"Welcome Back {username}!")
                    return existing_user
                else:
                    print("Incorrect Password")
                    return None
        print("Username not Found!")
        return None

    def show_users(self):
        if not self.Users:
            print("No users found")
        else:
            for user in self.Users:
                print(f"Username: {user._username}, Role: {user._role}")


