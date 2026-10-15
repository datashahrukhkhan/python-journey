class User:
    def __init__(self, password):
        self.__password = password

    def verify_password(self, password):
        return self.__password == password


user = User("demo123")

print(user.verify_password("demo123"))
print(user.verify_password("wrong"))