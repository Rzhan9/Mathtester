from math import factorial as fac

def factorial(n: int):
    if type(n) is not int:
        raise ValueError("Inputs must be integers!!!")
    if n < 0:
        raise ValueError("Inputs must be non-negative!!!")
    return fac(n)