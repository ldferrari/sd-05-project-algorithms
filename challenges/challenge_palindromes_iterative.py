def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word is None or len(word) == 0:
        return False

    low, high = 0, len(word) - 1

    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome_iterative("REVIVER"))
    print(is_palindrome_iterative("AGUA"))
    print(is_palindrome_iterative(""))
