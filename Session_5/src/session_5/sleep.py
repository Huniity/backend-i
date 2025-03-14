import logging
import time
import sys
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

def sleepTime():
    logger.info(f"Start at {datetime.now()}")
    time.sleep(1)
    logger.info(f"End at {datetime.now()}")

if __name__ == "__main__":
    sleepTime()