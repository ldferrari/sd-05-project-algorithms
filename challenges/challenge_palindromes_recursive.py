def is_palindrome_recursive(word=None, low=0, high=0):
    """ Faça o código aqui. """
    if word is None or word == '':
        return False
    if word[low] != word[high]:
        return False
    if high == low:
        return True
    return is_palindrome_recursive(word, low + 1, high - 1)
