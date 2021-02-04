
from logging import exception


def addition(a, b):
   
    return a + b


def subtraction(a, b):
    
    return a-b


def multiplication(a, b):
    
    return  a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
