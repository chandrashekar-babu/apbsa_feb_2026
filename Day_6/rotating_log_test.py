import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(
    logging.handlers.RotatingFileHandler(
        "rotating_app.log", maxBytes=1024*1024, backupCount=3
    )
)


def testfn():
    for i in range(100_000):
        logger.debug(f"counting {i}")
    

if __name__ == "__main__":
   testfn()