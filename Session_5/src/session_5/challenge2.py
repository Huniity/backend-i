from functools import cache
import logging
import time
import sys
from datetime import datetime

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(funcName)s at %(pathname)s %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)


def log_calls(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        td = (end - start).total_seconds() * 10**3
        print(f"The time of execution of above program is : {td:.03f}ms")
        return result
    return wrapper

@log_calls
@cache
def exponential(n):
    return n ** n
    

print(exponential(50))
print(exponential(75))

# https://www.python-engineer.com/posts/functools-overview/
# https://www.geekster.in/articles/decorators-in-python/