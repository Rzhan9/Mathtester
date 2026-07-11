def div(n1, n2):
    if type(n1) and type(n2) not in [int, float]:
        raise TypeError("Inputs must be numbers!")
    if n1 == 0 or n2 == 0:
        raise ValueError("Inputs cannot be zero!")
    return n1 / n2