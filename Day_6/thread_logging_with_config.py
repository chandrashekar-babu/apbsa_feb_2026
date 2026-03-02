import logging
import logging.config

from threading import Thread

logging.config.fileConfig("thread_logging_test.ini")

logger = logging.getLogger(__name__)

def testfn():
    for i in range(5):
        logger.debug(f"counting {i}")
    

if __name__ == "__main__":
    logger.info("Starting the main thread")
    t1 = Thread(target=testfn)
    t2 = Thread(target=testfn)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logger.info("Finished the main thread")
