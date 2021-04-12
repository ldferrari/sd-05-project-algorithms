def is_palindrome_iterative(word):
    if len(word) <= 1:
        return False
    arraia = list(word)
    arraia_de_tras_pra_frente = arraia[::-1]
    return arraia == arraia_de_tras_pra_frente
