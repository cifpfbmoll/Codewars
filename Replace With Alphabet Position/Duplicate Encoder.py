# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
def duplicate_encode(word):
    word = word.lower()
    Complete_string = ''
    for character in word:
        if word.count(character) != 1:
            Complete_string += ")"
        else:
            Complete_string += "("
    print(Complete_string)
    return Complete_string