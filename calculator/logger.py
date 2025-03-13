import logging

# Configure logging settings
logging.basicConfig(
    filename="calculator.log",  # Log file name
    level=logging.INFO,         # Set log level (INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    filemode="a"                # Append mode (logs are added, not overwritten)
)

class Logger:
    @staticmethod
    def log_info(message):
        """Log an informational message."""
        logging.info(message)

    @staticmethod
    def log_error(message):
        """Log an error message."""
        logging.error(message)
        # TEST: Write a log to check if logging is working
if __name__ == "__main__":
    Logger.log_info("Logging system initialized successfully!")
