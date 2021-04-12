def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word and word == word[::-1]:
        return True
    return False


print(is_palindrome_iterative("KAYAK"))
print(is_palindrome_iterative("BLA"))


# Without compulsary recursivity,
# you can just compare word and its reversed version
# https://www.askpython.com/python/array/reverse-an-array-in-python
