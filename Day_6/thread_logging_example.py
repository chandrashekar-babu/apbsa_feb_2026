import logging
from threading import Thread

logging.basicConfig(
    filename="thread_app.log",
    format="%(asctime)s: %(threadName)s:%(funcName)s: %(levelname)s: %(message)s",
    level=logging.DEBUG
)

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
