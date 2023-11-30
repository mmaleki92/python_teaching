import os
import importlib


class PluginManager:
    def __init__(self, plugin_directory):
        self.plugin_directory = plugin_directory
        self.plugins = {}

    def discover_plugins(self):
        # Iterate through files in the plugin directory
        for filename in os.listdir(self.plugin_directory):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                try:
                    # Import the module
                    module = importlib.import_module(f"{self.plugin_directory}.{module_name}")
                    for obj_name in dir(module):
                        obj = getattr(module, obj_name)
                        # read_type = getattr(obj, 'read_type', None)
                        # hasattr(obj, 'read_type')
                        if isinstance(obj, type) and obj.read_type:
                            print(obj)
                            self.plugins[obj.read_type] = obj
                    print(self.plugins)
                except ImportError as e:
                    print(f"Error loading plugin '{module_name}': {e}")

    def list_formats(self):
        return list(self.plugins.keys())

    def get_reader(self, file_format, file_path):
        if file_format in self.plugins:
            return self.plugins[file_format](file_path)
        else:
            raise ValueError(f"No plugin available for reading {file_format} files.")

def choose_format(manager):
    formats = manager.list_formats()
    if formats:
        print("Available formats:")
        for i, format in enumerate(formats):
            print(f"{i + 1}. {format}")
        choice = input("Choose a format (enter the number): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(formats):
                return formats[choice - 1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No formats available.")
    return None

if __name__ == "__main__":
    plugin_directory = "plugins"  # Change this to the path of your plugins directory
    manager = PluginManager(plugin_directory)
    manager.discover_plugins()

    chosen_format = choose_format(manager)
    if chosen_format:
        file_path = input("Enter the path of the file to read: ")
        reader = manager.get_reader(chosen_format, file_path)

        if reader:
            reader.read()
        else:
            print(f"No reader available for {chosen_format} format.")
