import logging

logging.basicConfig(
    filename="app.log",
    format="%(asctime)s: %(filename)s:%(name)s: %(levelname)s: %(message)s",
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.error("This is an error message")
logger.warning("This is a warning message")  # This will not be logged due to the log level
logger.info("This is an info message")  # This will not be logged due to the log level
logger.debug("This is a debug message")  # This will not be logged due to the log level
logger.critical("This is a critical message")
