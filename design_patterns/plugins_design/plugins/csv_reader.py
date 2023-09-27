from plugins.base_reader import BaseReader
import csv
class CsvReader(BaseReader):
    read_type = 'csv'
    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                print(f"Reading .csv file: {self.file_path}")
                print("CSV data:")
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
