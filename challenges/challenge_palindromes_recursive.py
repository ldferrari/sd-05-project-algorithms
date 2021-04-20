def is_palindrome_recursive(word, low, high):
    """ Verifica se a palavra é um palindromo. """

    # Retorna falso se for vazio, ou se a letra a direita é diferente
    # da letra a esquerda no indice correspondente.
    if not word or word[low] != word[high]:
        return False

    if low < high:
        return is_palindrome_recursive(word, low + 1, high - 1)

    return True
