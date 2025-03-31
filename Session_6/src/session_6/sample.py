def add(a: int | float, b: int | float) -> int | float:
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Not int or float"
    assert all(isinstance(arg, (int, float)) for arg in [a,b]), "Not int or float"
    return a + b

def multiply(c, d):
    return c * d



def factorial(n):
    assert isinstance(n, (int, float)), "Not int or float"
    if n == 1:
       return n
    else:
       return n*factorial(n-1)

num = 7

if num < 0: raise Exception("Negative number")
if num == 0: raise Exception ("The factorial of 0 is 1")
print("The factorial of", num, "is", factorial(num))


