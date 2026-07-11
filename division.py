def div(n1, n2):
    if type(n1) and type(n2) not in [int, float]:
        raise TypeError("Inputs must be numbers!")
    if n2 == 0:
        raise ZeroDivisionError("Divisor cannot be zero!")
    return n1 / n2