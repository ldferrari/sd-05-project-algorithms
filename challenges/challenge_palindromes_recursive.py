# "Um algoritmo recursivo deve obedecer três regras:
# 1/ Ter caso base: condição de parada do algoritmo recursivo
# e menor subproblema do problema;
# 2/ Mudar o seu estado e se aproximar do case base;
# 3/ Chamar a si mesmo recursivamente."

def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    # 1. Interpret given low, high: index of first and last letter
    # 2. Take care of conditions from exercise requirements
    if not word:
        return False
    # 3. Use recursivity to go until the center of the word
    # and return true each time low&high letters are the same
    if word[low] == word[high]:
        if low >= high:
            return True
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False


print(is_palindrome_recursive("KAYAK", 0, 4))
print(is_palindrome_recursive("BLA", 0, 2))
