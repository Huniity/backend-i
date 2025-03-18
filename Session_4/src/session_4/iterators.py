class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Use enumerate-like behaviour to track index and value
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration

numbers = [23,124,15,23,523,41,2334,125,334,12,3,2345,1234,1]

even_iterator = EvenIterator(numbers)
print("\n****************** Printing Even Numbers from [numbers] list ******************")
for num in even_iterator:
    print(num)

for index, number in enumerate(EvenIterator(numbers)):
    print(index, number)


# Using enumerate to show index-value pairs
items = ['apple', 'banana', 'cherry']
print("\n****************** Enumerate from [items] list ******************")
for index, item in enumerate(items):
    print(f"Index {index}: {item}")


def fibonacci(n):
    """Yield the Fibonacci sequence up to n terms.
    
    'yield' pauses the function saving its state, and produces a value
    on each iteration. This is memory efficient for large sequences.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibo_numbers = []
# Tutorial snippet: Generate and print first 10 Fibonacci numbers
print("\n****************** Printing Numbers from [fibo_numbers] list ******************")
for num in fibonacci(50):
    fibo_numbers.append(num)
    print("Fibonacci number:", num)


even_fibonacci = EvenIterator(fibo_numbers)
print("\n****************** Printing Even Numbers from [fibo_numbers] list. ******************")
for num in even_fibonacci:
    print(num)


def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


n,fib = 20,fibonacci()
print("\n****************** Generating Fibo Sequence with yield. Printing using next() ******************")
for _ in range(n):
    print(next(fib),end=", ")