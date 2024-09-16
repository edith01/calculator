import math 
def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def square_root(x):
    """Square Root"""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number!")
    return math.sqrt(x)
  
if __name__ == "__main__":
    # Sample inputs
    a = 25
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    print(f"Square root of {a} = {square_root(a)}")
