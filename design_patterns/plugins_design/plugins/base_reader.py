from abc import abstractmethod

class BaseReader:
    read_type = None
    def __init__(self, file_path):
        self.file_path = file_path
    # @abstractmethod
    def read(self):
        raise NotImplementedError("Subclasses must implement the read method.")
