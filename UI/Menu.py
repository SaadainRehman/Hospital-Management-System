from DL.UserDL import UserDL
from BL.user import User

class Menu:
    def __init__(self):
        self.user_dl = UserDL()

    def menu_print(self):
        print("Welcome")
        name = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role: ")

        user = User(name, password, role)
        return user

    def main_menu(self):
        while True:
            print("\n--- Hospital Management System ---")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Show All Users (Admin)")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n--- Sign Up ---")
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                role = input("Enter your role: ")
                self.user_dl.sign_up(username, password, role)
            elif choice == "2":
                print("\n--- Sign In ---")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.user_dl.sign_in(username, password)
            elif choice == "3":
                print("\n--- Registered Users ---")
                self.user_dl.show_users()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
