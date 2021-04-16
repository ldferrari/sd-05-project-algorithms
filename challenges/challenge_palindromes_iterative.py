def is_palindrome_iterative(word):
    tam = len(word)
    if tam == 0:
        return False
    for i in range(tam//2):
        if word[i] != word[tam-1-i]:
            return False
    return True