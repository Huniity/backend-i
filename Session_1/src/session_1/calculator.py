import logging
logger = logging.getLogger('__init__')
logging.basicConfig(format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")

def calculator():
    print("Welcome to your calculator.")
    userChoice = input("What would you like to do? (sum, subtract, divide, multiply, fibonacci): ")

    match userChoice:
        case "sum":
            x,y = askTwoNum()
            print(f"Very Good! The sum of {x}+{y} is {sum(x,y)}")

        case "subtract":
            x,y = askTwoNum()
            print(f"Very Good! The subtraction of {x}-{y} is {subtract(x, y)}")

        case "divide":
            x,y = askTwoNum()
            print(f"Very Good! The rest of {x}/{y} is {divide(x, y)}")

        case "multiply":
            x,y = askTwoNum()
            print(f"Very Good! The multiplication of {x}*{y} is {multiply(x, y)}")

        case "fibonacci":
            z = askOneNum()
            print(f"Very Good! The fibonacci number of {z} is {fibonacci(z)}")
        
        case _:
            logger.warning("Please insert a valid choice (sum, substract, divide, multiply)!")
            return calculator()
            

def askOneNum():
    try:   
        z = int(input("What would be your number: "))
        return z
    except ValueError:
        logging.error("Not a number\n")
        return calculator()

def askTwoNum():
    try:   
        x = int(input("What would be your first number: "))
        y = int(input("What would be second first number: "))
        return x, y
    except ValueError:
        logging.error("Not a number\n")
        return calculator()
    
def sum(x, y):
    return x+y

def subtract(x, y):
    return x-y

def divide(x, y):
    return x/y

def multiply(x, y):
    return x*y

def fibonacci(z):
    if (z == 0): return 0
    if (z == 1): return 1
    return fibonacci(z-2) + fibonacci(z-1)

calculator()