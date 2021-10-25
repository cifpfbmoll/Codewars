def is_square(n):
    resultado = n**(1/2)
    if n < 0:
        return False
    if resultado.is_integer:
        return True
    return False