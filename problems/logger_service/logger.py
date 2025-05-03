from log_level import LogLevel
from datetime import datetime

class Logger:
    _instance = None

    # method for object creation
    def __new__(cls, log_file: str = None, level: LogLevel = LogLevel.INFO):    # using INFO as the defualt log level
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    # method for initializing a logger object
    def __init__(self, log_file: str = None, level: LogLevel = LogLevel.INFO):
        if self._initialized:   # if a logger object is already initialized, return existing object
            return
        self.log_file = log_file
        self.level = level
        self._initialized = True
    
    # decides if the message needs to be logged
    def _should_log(self, level):
        return level.value >= self.level.value

    # formats the message with the timestamp
    def _format_message(self, level, message):
        timestamp = datetime.now()
        return f"[{timestamp}] [{level.name}] [{message}]"

    # core log function
    def log(self, level: LogLevel, message: str):
        if self._should_log(level):
            formatted = self._format_message(level, message)
            if self.log_file:
                with open(self.log_file, 'a') as f:
                    f.write(formatted + '\n')
            else:
                print(formatted)

    # convenience test functions
    def debug(self, msg): 
        self.log(LogLevel.DEBUG, msg)
    
    def info(self, msg): 
        self.log(LogLevel.INFO, msg)
    
    def warning(self, msg): 
        self.log(LogLevel.WARNING, msg)
    
    def error(self, msg): 
        self.log(LogLevel.ERROR, msg)
    

# these two loggers are going to point to the same instance
logger1 = Logger(log_file="app.log", level=LogLevel.DEBUG)
logger2 = Logger()

logger1.debug("Debug message")
logger2.error("Error message")

print(logger1 is logger2)
