class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = "game_log.txt"
        return cls._instance

    def log(self, message):
        with open(self._instance.log_file, "a") as log_file:
            log_file.write(f"{message}\n")

# Usage Example
logger = Logger()
logger.log("Player has started the game")
