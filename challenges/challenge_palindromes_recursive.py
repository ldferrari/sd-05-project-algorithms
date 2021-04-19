def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    lenght = len(word)
    if lenght == 1:
        return True
    elif lenght == 0 or word[low] != word[high]:
        return False
    elif low > lenght:
        return True
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)
