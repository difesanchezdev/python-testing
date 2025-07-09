def sum (a, b):
    """
    >>> sum(5, 7)
    12
    >>> sum(-1, 1)
    0
    """
    return a + b

def subtract(a, b):
    """Returns the difference of a and b.
    >>> subtract(10, 5)
    5
    >>> subtract(5, 10)
    -5
    >>> subtract(10, 10)
    0
    """
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: Cannot divide by zero
    >>> divide(5, 0)
    Traceback (most recent call last):
    ValueError: Cannot divide by zero"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
