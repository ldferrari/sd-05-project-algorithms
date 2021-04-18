def is_palindrome_iterative(word):
    if not word:
        return False

    invertido = ""
    for i in range(len(word)-1, -1, -1):
        invertido += word[i]

    if (invertido == word):
        return True
    return False
