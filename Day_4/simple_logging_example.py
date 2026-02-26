import logging

logging.basicConfig(level=logging.DEBUG, filename="simple_logging.log", 
                    format="%(asctime)s: %(name)s: %(levelname)s: %(process)d: %(msg)s")

log = logging.getLogger(__name__)
log.debug("this is debug message")
log.warning("This is a warning message")
log.error("This is an error message")
