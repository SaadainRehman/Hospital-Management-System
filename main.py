from DL.UserDL import UserDL
from UI.Menu import Menu
b = UserDL()

user = Menu.Menu_print()
print(type(user))
c = b.add(user)
print(c)
# UserDL.show()

