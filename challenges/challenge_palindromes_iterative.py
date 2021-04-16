def is_palindrome_iterative(word):
    def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    for index in range((len(word)+1)//2):
        if word[index] != word[-index-1]:
            return False

    return True
