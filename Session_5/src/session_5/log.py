import logging
import sys
from datetime import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


def audit(func):
    def wrapper():
        logger.info(f"Start at {datetime.now()}")
        result = func()
        logger.info(f"End at {datetime.now()}")
        return result
    return wrapper