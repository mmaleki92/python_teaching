class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def get_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user
        raise ValueError(f"User with name '{name}' not found")

user_repo = UserRepository()
user_repo.add_user(User("Alice"))
user_repo.add_user(User("Bob"))

print(user_repo.get_user_by_name("Alice").name)
print(user_repo.get_user_by_name("Bob").name)