def is_palindrome_recursive(word, low=0, high=False):
    if word == '':
        return False
    if not high:
        high = len(word) - 1
    if low >= high:
        return True
    elif word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    else:
        return False
