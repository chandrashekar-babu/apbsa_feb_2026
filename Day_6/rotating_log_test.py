import logging
logging.basicConfig(filename="rotating_log_test.log", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def testfn():
    for i in range(100_000):
        logger.debug(f"counting {i}")
    

if __name__ == "__main__":
   testfn()