def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    if word[low] != word[high]:
        return False
    if low > high:
        return True
    return is_palindrome_recursive(word, low+1, high-1)
