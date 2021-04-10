def is_palindrome_recursive(word, low=0, high=0):
    if not word:
        return False

    high = len(word) - 1

    if (len(word) == 1) or (len(word) == 2 and low == high):
        return True

    if word[low] == word[high]:
        return is_palindrome_recursive(word[low + 1:high])
    else:
        return False
