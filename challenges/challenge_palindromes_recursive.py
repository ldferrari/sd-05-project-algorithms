def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if len(word) == 0 or word[low] != word[high]:
        return False
    if low > high:
        return True
    return is_palindrome_recursive(word, low + 1, high - 1)


if __name__ == "__main__":
    print(is_palindrome_recursive("SOCOS", 0, 4))
    print(is_palindrome_recursive("AGUA", 0, 3))
