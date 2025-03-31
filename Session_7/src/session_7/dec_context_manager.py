import logging
import time
import sys
from contextlib import contextmanager


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(funcName)s at %(pathname)s %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

user_database = {}

@contextmanager
def user_registration(username, email, password):
    start_time = time.perf_counter()
    logger.info(f"Starting registration for user: {username}")

    try:
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username can't be empty")
        if username in user_database:
            raise ValueError(f"Username '{username}' is already registered.")
    except ValueError as e:
        logger.error(e)


    user_data = {"email": email, "password": password}

    try:
        yield user_data               
    finally:
        user_database[username] = user_data
        logger.info(f"User '{username}' registered successfully.")
        elapsed = time.perf_counter() - start_time
        logger.info(f"Execution time: {elapsed:.7f} seconds")

if __name__ == "__main__":   
    with user_registration("Huniity", "huniity.1234@gmail.com", "*Aa1234567890") as user:
        logger.info("Creating user with givenattributes: %s", user)

    logger.info("Current user database: %s", user_database)
