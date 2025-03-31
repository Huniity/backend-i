import time
from log import audit


@audit
def sleepTime():
    time.sleep(1)

if __name__ == "__main__":
    sleepTime()