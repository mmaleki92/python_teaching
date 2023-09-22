import psutil

class DataManager:
    # ... (same code as before)

if __name__ == "__main__":
    # Print initial RAM usage
    initial_ram = psutil.virtual_memory().used
    print(f"Initial RAM usage: {initial_ram} bytes")

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

    # Print RAM usage after creating instances and storing data
    final_ram = psutil.virtual_memory().used
    print(f"RAM usage after creating instances and storing data: {final_ram} bytes")

    # Check if both DataManager instances are the same
    print("Is data_manager the same instance as another_data_manager?", data_manager is another_data_manager)
