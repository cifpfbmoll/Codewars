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