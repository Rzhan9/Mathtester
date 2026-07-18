from math import factorial as fac

def factorial(n: int):
    if type(n) is not int:
        raise ValueError("Inputs must be integers!")
    return fac(n)