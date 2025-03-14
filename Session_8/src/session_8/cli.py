from typer import Typer, Argument, BadParameter
import logging 
import sys
from typing import List

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] | [%(funcName)s] [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

app = Typer() #(help="CLI Calculator") -> add help info

"""Name validation"""
def validate_name(name: str):
    if not name.strip():
        raise BadParameter("Name cannot be empty")
    return name

"""Args validation"""
def validate_numbers(numbers: List[float]):
    if len(numbers) < 2:
        raise BadParameter("You need to insert 2 numbers")
    return numbers


@app.command()
def hello(name: str = Argument(..., callback=validate_name)):
    """Say hello to a user"""
    try:
        print(f"Hello {name}")
        logger.info("Greetings to user")
    except Exception as e:
         logger.error(f"Hello - Error: {e}")
         raise


@app.command()
def goodbye(
    name: str = Argument(..., callback=validate_name),
    formal: bool = False):
    """Say goodbye to a user"""
    try:
        if formal:
            print(f"Goodbye Ms. {name}. Have a good day.")
        else:
            print(f"Bye {name}!")
        logger.info(f"Goodbye to user")
    except Exception as e:
        logger.error(f"Goodbye - Error: {e}")
        raise
   

@app.command()
def square(num: float):
    """Calculate square with given args"""
    try:
        assert num >= 0, "Number can't be negative"
        result = num**2
        print(f"The square of {num} is: {result}")
        logger.info(f"Square: {num} = {result}")
    except AssertionError as e:
        logger.error(f"Square - Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Square - Error {e}")
        raise

        
@app.command()
def add(numbers: List[float] = Argument(..., callback=validate_numbers)):
    """Calculate addition with given args"""
    try:
        result = sum(numbers)
        print(f"Sum: {result}")
        logger.info(f"Addition: {numbers} = {result}")
    except Exception as e:
        logger.error(f"Addition - Error: {e}")
        raise


@app.command()
def sub(numbers: List[float] = Argument(..., callback=validate_numbers)):
    """Calculate subtraction with given args"""
    try:
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print(f"Subtraction: {result}")
        logger.info(f"Subtraction: {numbers} = {result}")
    except Exception as e:
        logger.error(f"Subtraction - Error: {e}")
        raise
             

@app.command()
def div(numbers: List[float] = Argument(..., callback=validate_numbers)):
    """Calculate division with given args - Zero Division Avoided"""
    try:
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                raise ZeroDivisionError("Can't divide by 0")
            result /= num
        print(f"Division: {result}")
        logger.info(f"Division: {numbers} = {result}")
    except ZeroDivisionError as zero_div:
        logger.error("Can't divide by 0")
        raise BadParameter(zero_div.args[0]) from zero_div
    except Exception as e:
        logger.error(f"Division - Error: {e}")
        raise

@app.command()
def multi(
    numbers: List[float] = Argument(..., callback=validate_numbers)
):
    """Calculate multiplication with given args"""
    try:
        result = 1
        for num in numbers:
            result *= num
        print(f"Multiplication: {result}")
        logger.info(f"Division: {numbers} = {result}")
    except Exception as e:
        logger.error(f"Multiplication error: {e}")
        raise


if __name__ == "__main__":
    app()