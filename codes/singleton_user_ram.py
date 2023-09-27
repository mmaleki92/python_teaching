class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.data = {}

    def add_data(self, user, data):
        self.data[user] = data

    def get_data(self, user):
        return self.data.get(user)

class User:
    def __init__(self, name):
        self.name = name

# Usage example:
if __name__ == "__main__":
    # Create User objects
    user1 = User("User 1")
    user2 = User("User 2")

    # Initialize the DataManager (Singleton)
    data_manager = DataManager()

    # Add data for users
    data_manager.add_data(user1, "Data for User 1")
    data_manager.add_data(user2, "Data for User 2")

    # Attempt to create a new DataManager instance (will return the existing one)
    another_data_manager = DataManager()

    # Retrieve data for users
    user1_data = data_manager.get_data(user1)
    user2_data = data_manager.get_data(user2)

    print("User 1 Data:", user1_data)
    print("User 2 Data:", user2_data)

    # Check if both DataManager instances are the same
    print("Is data_manager the same instance as another_data_manager?", data_manager is another_data_manager)
