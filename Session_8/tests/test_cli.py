import pytest
from typer.testing import CliRunner
from src.session_8.cli import app


#pytest tests/test_cli.py -s
#pytest tests/test_cli.py -v

# Initialize CliRunner
@pytest.fixture()
def runner():
    return CliRunner()


def test_hello_command(runner):
    """Hello Command - Happy Path"""
    result = runner.invoke(app, ["hello", "John"])
    assert result.exit_code == 0
    assert "Hello John" in result.stdout

def test_hello_command_empty_name(runner):
    """Hello Command - Sad Path"""
    result = runner.invoke(app, ["hello", ""])
    assert result.exit_code != 0
    assert "Name cannot be empty" in result.stdout

#==================================================#

def test_goodbye_command(runner):
    """Goodbye Command - Happy Path"""
    result = runner.invoke(app, ["goodbye", "John"])
    assert result.exit_code == 0
    assert "Bye John!" in result.stdout

def test_goodbye_command_formal(runner):
    """Goodbye Command - Sad Path"""
    result = runner.invoke(app, ["goodbye", "John", "--formal"])
    assert result.exit_code == 0
    assert "Goodbye Ms. John. Have a good day." in result.stdout

#==================================================#

def test_square_command(runner):
    """Square Command - Happy Path"""
    result = runner.invoke(app, ["square", "4"])
    assert result.exit_code == 0
    assert "The square of 4.0 is: 16.0" in result.stdout

def test_square_command_invalid_input(runner):
    """Square Command - Sad Path"""
    result = runner.invoke(app, ["square", "abc"])
    assert result.exit_code != 0
    assert "Invalid value" in result.stdout

#==================================================#

def test_add_command(runner):
    """Add Command - Happy Path"""
    result = runner.invoke(app, ["add", "1", "2", "3"])
    assert result.exit_code == 0
    assert "Sum: 6.0" in result.stdout

def test_add_command_insufficient_numbers(runner):
    """Add Command - Sad Path"""
    result = runner.invoke(app, ["add", "1"])
    assert result.exit_code != 0
    assert "You need to insert 2 numbers" in result.stdout

#==================================================#

def test_sub_command(runner):
    """Sub Command - Happy Path"""
    result = runner.invoke(app, ["sub", "10", "2", "3"])
    assert result.exit_code == 0
    assert "Subtraction: 5.0" in result.stdout

def test_sub_command_insufficient_numbers(runner):
    """Sub Command - Sad Path"""
    result = runner.invoke(app, ["sub", "10"])
    assert result.exit_code != 0
    assert "You need to insert 2 numbers" in result.stdout

#==================================================#

def test_div_command(runner):
    """Div Command - Happy Path"""
    result = runner.invoke(app, ["div", "10", "2", "2"])
    assert result.exit_code == 0
    assert "Division: 2.5" in result.stdout

def test_div_command_divide_by_zero(runner):
    """Div Command - Sad Path"""
    result = runner.invoke(app, ["div", "10", "0"])
    assert result.exit_code != 0
    assert "Can't divide by 0" in result.stdout

#==================================================#

def test_multi_command(runner):
    """Multi Command - Happy Path"""
    result = runner.invoke(app, ["multi", "2", "3", "4"])
    assert result.exit_code == 0
    assert "Multiplication: 24.0" in result.stdout

def test_multi_command_insufficient_numbers(runner):
    """Multi Command - Sad Path"""
    result = runner.invoke(app, ["multi", "2"])
    assert result.exit_code != 0
    assert "You need to insert 2 numbers" in result.stdout