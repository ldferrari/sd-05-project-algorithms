def is_palindrome_recursive(word, low, high):
    if len(word) == 0:
        return False
    tam = high - low
    if tam <= 0:
        return True
    if word[low] != word[high]:
        return False
    result = is_palindrome_recursive(word, low + 1, high - 1)
    return result
