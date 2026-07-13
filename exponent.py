def exp(n1, n2):
    if type(n1) not in [int, float] or type(n2) not in [int, float]:
        raise TypeError("Inputs must be numbers! MAKE THE INPUTS NUMBERS! NUMBERS I TELL YOU!")
    return n1 ** n2