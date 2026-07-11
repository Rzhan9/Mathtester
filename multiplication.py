def mult(n1, n2):
    if type(n1) and type(n2) not in [int, float]:
        raise TypeError("Inputs must be numbers!")
    return n1 * n2