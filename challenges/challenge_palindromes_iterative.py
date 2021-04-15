def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    new_word = word[::-1]
    return True if new_word == word else False
