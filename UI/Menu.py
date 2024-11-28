from DL.UserDL import UserDL
from BL.user import User
class Menu:
    def __init__(self):
        pass
    def Menu_print():
        print("Welcome")
        name = input("Enter USerNAme: " )  
        password = input("Enter USerNAme: " )                 
        role = input("Enter USerNAme: " )  

        user = User(name,password,role)
        return user
        
      


