class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = "log.txt"
        return cls._instance

    def log(self, message):
        with open(self._instance.log_file, "a") as log_file:
            log_file.write(f"{message}\n")

# Usage
logger1 = Logger()
logger2 = Logger()
logger1.log("Test Message 1")
logger2.log("Test Message 2")
assert logger1 is logger2  # True
