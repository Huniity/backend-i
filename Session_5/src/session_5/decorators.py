import logging
from datetime import datetime
import sys

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(funcName)s at %(pathname)s %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)


def log_calls(func):
    """A decorator that logs function call details."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        logger.info(f"Executed at {datetime.now()}")
        result = func(*args, **kwargs)
        logger.info(f"Finished at {datetime.now()}")
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

print("Result of add:", add(3, 4))