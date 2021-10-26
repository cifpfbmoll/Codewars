#Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
def invert(lst):
    lista=[]
    for number in lst:
        invert = number * -1
        lista.append(invert)
    return lista