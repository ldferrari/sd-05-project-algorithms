def is_palindrome_iterative(word):
    """ Verifica se a palavra é palindrome, de forma iterativa. """

    if word and word == word[::-1]:
        return True

    return False
