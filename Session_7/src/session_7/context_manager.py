import logging
import time
import sys


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(funcName)s at %(pathname)s %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)


class UserRegistration:
    
    user_database = []

    def __init__(self, username, email, password):
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")
            
        self.username = username
        self.email = email
        self.password = password
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.perf_counter()
        logger.info(f"Registration starting for user {self.username} with email {self.email}.")
        
        if not self.username:
            raise ValueError("Username cannot be empty.")
        if not self.email:
            raise ValueError("Email cannot be empty.")
        if not self.password:
            raise ValueError("Password cannot be empty.")
            
        #import re
        #if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.email):
        #   raise ValueError("Invalid email format.")
        if self.username in UserRegistration.user_database:
            raise ValueError(f"Username '{self.username}' is already registered.")
        
        #if any(user['email'] == self.email for user in UserRegistration.user_database.values()):
        #    raise ValueError(f"Email '{self.email}' is already registered.")
            
        if self.username in UserRegistration.user_database:
            raise Exception(f"{self.username} is already in the database.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Registration finished for user {self.username} and e-mail {self.email}.")
         if exc_type is None:
            UserRegistration.user_database[self.username] = {
                'email': self.email,
                'password': self.password
            }
            logger.info(f"Registration completed for {self.username}.")
            print(f"{UserRegistration.user_database}")
            self.end = time.perf_counter()
            logging.info(f"Execution time: {self.end - self.start:.7f}ms")
        else:
            logger.error("Registration failed.", exc_info=True)
        
        return False #suppress?


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        with UserRegistration("Huniity", "huniity.1234@gmail.com", "*Aa1234567890") as u:
            logger.info("Creating user with given attributes.")
    except Exception as e:
        logger.error(f"Registration error: {e}")


# password verif with re match /search
#        if len(self.password) < 8:
 #           raise ValueError("Password must be at least 8 characters.")
  #      if not re.search(r'[A-Z]', self.password):
   #         raise ValueError("Password must contain at least one uppercase letter.")
    #    if not re.search(r'[a-z]', self.password):
     #       raise ValueError("Password must contain at least one lowercase letter.")
      #  if not re.search(r'\d', self.password):
       #     raise ValueError("Password must contain at least one digit.")
