def is_palindrome_recursive(word, low, high):
    if len(word) <= 1:
        return False
    elif word[low] != word[high]:
        return False
    elif low < high:
        return is_palindrome_recursive(word, low+1, high-1)
    else:
        return True
