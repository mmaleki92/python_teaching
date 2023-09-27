from plugins.base_reader import BaseReader

class TxtReader(BaseReader):
    read_type = 'txt'
    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                print(f"Reading .txt file: {self.file_path}")
                print("File content:")
                print(content)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

