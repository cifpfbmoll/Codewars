def alphabet_position(text):
    import string 
    #importo toda la libreria de string para poder usar string.puntuation y string.digits para comprobar que no esten como charachter, ya que no lo podria buscar en string.ascii_lowercase para ver el index y poder ver su posicion

    acumulador = ''
    for charachter in text.lower().replace(' ',''):
        if charachter not in (string.punctuation + string.digits):
            acumulador = acumulador + ' ' + str (string.ascii_lowercase.find(charachter) + 1 )
    return acumulador


if __name__ == '__main__':
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
