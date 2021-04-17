def is_palindrome_recursive(word, low, high):
    if not word or word[low] is not word[high]:
        return False
    return True if low == high else (
        is_palindrome_recursive(word, low + 1, high - 1)
    )
